<script>
	import {currentPage, ProjectPages} from "../../../stores";
	import {onDestroy, onMount} from "svelte";
	import {generatePoints} from "./pi.js";

	currentPage.set(ProjectPages.PI);

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
	let bulkSize = 10;

	let pi = 0;
	let pointsCount = 0;
	let piPointsCount = 0;

	let interval;

	onMount(() => {
		context = canvas.getContext('2d');
		prepareCanvas();
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
		pointsCount = 0;
		piPointsCount = 0;
		prepareCanvas();
	}

	function updatePi() {
		const newPoints = generatePoints(bulkSize);
		const newPointsInCircle = newPoints.filter(p => Math.sqrt(Math.pow(p.x, 2) + Math.pow(p.y, 2)) <= 1);
		const newPointsOutsideCircle = newPoints.filter(p => !newPointsInCircle.includes(p));

		pointsCount += newPoints.length;
		piPointsCount += newPointsInCircle.length;

		pi = 4 * piPointsCount / pointsCount;

		updateCanvas(newPointsInCircle, newPointsOutsideCircle);
	}

	function updateCanvas(pointsInCircle, pointsOutsideCircle) {
		pointsInCircle.map(p => mapPointToCanvas(p)).forEach(p => {
			context.fillStyle = 'red';
			context.fillRect(p.x, p.y, 1, 1);
			context.fillStyle = 'black';
		});
		pointsOutsideCircle.map(p => mapPointToCanvas(p)).forEach(p => context.fillRect(p.x, p.y, 1, 1));
	}

	function prepareCanvas() {
		context.beginPath();
		context.clearRect(0, 0, canvasSize, canvasSize);
		context.arc(canvasSize / 2, canvasSize / 2, canvasSize / 2, 0, 7);
		context.stroke();
	}

	// Canvas UTIL

	function mapPointToCanvas(p) {
		return {x: (p.x + 1) * (canvasSize / 2), y: (p.y + 1) * (canvasSize / 2)};
	}

	// over-the-top UX UTIL

	let runButtonTooltip = 'Run calculation';

	function updateRunButtonTooltip(delay) {
		if (delay === Math.floor(delay) && bulkSize === Math.floor(bulkSize)) {
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
			Once you press the button to start the calculation random values between -1 and 1 are generated, combined
			into points and input into the canvas you can see below. If the points are in/on the circle they are added
			to an array of values called <code>piPoints</code>. All points are added to the array
			called<code>points</code>. Every time a new point is added you can calculate an approximation of pi with the
			formula 4 * piPoints / points.
		</p>
		<div class="uk-grid-small" uk-grid>
			<div class="uk-width-expand">
				<div class="uk-margin">
					<label for="delay-input" class="uk-form-label">
						Delay (ms)
						<span class="uk-margin-small-right pointer-cursor"
						      uk-icon="info"
						      uk-tooltip="How often a point(s) should be added"></span>
					</label>
					<input id="delay-input"
					       type="number"
					       min="0"
					       step="1"
					       bind:value={delay}
					       placeholder="1"
					       class="uk-input uk-border-rounded"
					       class:uk-form-danger={delay !== Math.floor(delay)}
					       uk-tooltip={delay !== Math.floor(delay) ? 'Delay must be an integer' : undefined}>
				</div>

				<div class="uk-margin">
					<label for="bulk-size-input" class="uk-form-label">
						Bulk size
						<span class="uk-margin-small-right pointer-cursor"
						      uk-icon="info"
						      uk-tooltip="How many points should be added at once"></span>
					</label>
					<input id="bulk-size-input"
					       type="number"
					       min="0"
					       step="1"
					       bind:value={bulkSize}
					       placeholder="10"
					       class="uk-input uk-border-rounded"
					       class:uk-form-danger={bulkSize !== Math.floor(bulkSize)}
					       uk-tooltip={bulkSize !== Math.floor(bulkSize) ? 'Bulk size must be an integer' : undefined}>
				</div>
			</div>
			<div class="uk-width-auto">
				{#if calculationStarted}
					<label for="alignment-hack">&nbsp;<br></label>
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
			Value of pi: {pi}<br>
			<code>points</code> count: {pointsCount}<br>
			<code>piPoints</code> count: {piPointsCount}<br>
		</p>
	</div>
</div>