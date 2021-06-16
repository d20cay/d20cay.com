<script>
	import {currentPage, Page} from "../../../stores";
	import {onDestroy, onMount} from "svelte";

	currentPage.set(Page.PI);

	const Status = {
		RUNNING: 0,
		IDLE: 1,
	};

	const canvasSize = 1000;
	let canvas;
	let context;

	let status = Status.IDLE;
	let calculationStarted = false;

	let delay = 1;
	let delayValid = true;

	let pi = 0;
	let points = [];
	let piPoints = [];

	let interval;

	onMount(() => {
		context = canvas.getContext('2d');
		drawCircle();
	});

	onDestroy(() => {
		clearInterval(interval);
	});

	function calc() {
		if (delay !== Math.floor(delay)) {
			return;
		}
		status = Status.RUNNING;
		calculationStarted = true;
		drawCircle();
		updatePi();
		interval = setInterval(updatePi, delay);
	}

	function pauseCalc() {
		status = Status.IDLE;
		clearInterval(interval);
	}

	function stopCalc() {
		status = Status.IDLE;
		calculationStarted = false;
		clearInterval(interval);
		pi = 0;
		points = [];
		piPoints = [];
		context.clearRect(0, 0, canvasSize, canvasSize);
	}

	function updatePi() {
		const x = (Math.random() - 0.5) * 2;
		const y = (Math.random() - 0.5) * 2;

		points.push({x, y});
		const isInCircle = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)) <= 1;
		if (isInCircle) {
			piPoints.push({x, y});
		}
		pi = 4 * piPoints.length / points.length;

		updateCanvas(x, y, isInCircle)
	}

	function updateCanvas(x, y, isInCircle) {
		const xPixel = (x + 1) * (canvasSize / 2)
		const yPixel = (y + 1) * (canvasSize / 2);
		if (isInCircle) {
			context.fillStyle = 'red';

		}
		context.fillRect(xPixel, yPixel, 1, 1);
		context.fillStyle = 'black';
	}

	function drawCircle() {
		context.beginPath();
		context.arc(canvasSize / 2, canvasSize / 2, canvasSize / 2, 0, 7);
		context.stroke();
	}

	// over-the-top UX UTIL

	let runButtonTooltip = 'Run calculation';

	function updateRunButtonTooltip(delay) {
		if (delay === Math.floor(delay)) {
			if (calculationStarted) {
				runButtonTooltip = 'Continue calculation';
			} else {
				runButtonTooltip = 'Run calculation';
			}
		} else {
			runButtonTooltip = 'Cannot run calculation with floating point delay'
		}
	}

	$: updateRunButtonTooltip(delay)
</script>

<style>
	/** Changes the mouse cursor into a point (hand) when hovering over objects with this class. */
	.pointer-cursor:hover {
		cursor: pointer;
	}

	canvas {
		border: 1px solid #000000;
	}
</style>

<svelte:head>
	<title>d20cay | Pi Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Pi
</h1>

<p class="uk-text-center">
	Calculate pi using a very simple ratio concept.
</p>

<div uk-grid>
	<div class="uk-width-2-3@m uk-width-1-1@s">
		<canvas bind:this={canvas} width={canvasSize} height={canvasSize} class="uk-border-rounded">
			Your browser does not support the canvas tag. Please switch to a newer browser or update the current one you
			are using.
		</canvas>
	</div>
	<div class="uk-width-1-3@m uk-width-1-1@s">
		<p>
			Once you press the button to start the calculation random values
			between -1 and 1 are generated, combined into points and input into the canvas you can see below. If the points are
			in/on the circle they are added to an array of values called piPoints. All points are added to the array called
			points. Every time a new point is added you can calculate an approximation of pi with the formula 4 * piPoints /
			points.
		</p>
		<div class="uk-grid-small" uk-grid>
			<div class="uk-width-expand">
				<label for="username-input" class="uk-form-label">Delay (ms)</label>
				<input type="number"
				       min="0"
				       step="1"
				       bind:value={delay}
				       class="uk-input uk-border-rounded"
				       class:uk-form-danger={delay !== Math.floor(delay)}
				       uk-tooltip={delay !== Math.floor(delay) ? 'Delay must be an integer' : undefined}>
			</div>
			<div class="uk-width-auto">
				{#if calculationStarted}
					<label htmlFor="alignment-hack">&nbsp;<br></label>
					<span on:click={stopCalc}
					      uk-tooltip="Pause calculation"
					      class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
					      uk-icon="stop-circle"></span>
				{/if}
			</div>
			<div class="uk-width-auto">
				<label for="alignment-hack">&nbsp;<br></label>
				{#if status === Status.IDLE}
					<span on:click={calc}
					      uk-tooltip={runButtonTooltip}
					      class="uk-icon-button uk-animation-fade uk-animation-fast"
					      uk-icon="play-circle"
					      disabled={delay !== Math.floor(delay)}
					      class:pointer-cursor={delay === Math.floor(delay)}></span>
				{:else if status === Status.RUNNING}
					<span on:click={pauseCalc}
					      uk-tooltip="Pause calculation"
					      class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
					      uk-icon="pause-circle"></span>
				{/if}
			</div>
		</div>
		<p>
			Value of pi: {pi}
		</p>
	</div>
</div>