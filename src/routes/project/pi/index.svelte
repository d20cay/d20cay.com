<script>
	import {currentPage, Page} from "../../../stores";
	import {onMount} from "svelte";

	currentPage.set(Page.PI);

	const Status = {
		RUNNING: 0,
		IDLE: 1,
	};

	let canvas;
	let context;
	let status = Status.IDLE;
	let calculationStarted = false;
	let delay = 10;
	let pi = 0;

	onMount(() => {
		context = canvas.getContext('2d');
	});

	function calc() {
		status = Status.RUNNING;
		calculationStarted = true;
	}

	function pauseCalc() {
		status = Status.IDLE;
	}

	function stopCalc() {
		status = Status.IDLE;
		calculationStarted = false;
	}
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

<p class="uk-text-center">Calculate pi using a very simple ratio concept.</p>

<div uk-grid>
	<div class="uk-width-1-3@m uk-width-1-1@s">
		<canvas bind:this={canvas} width="500" height="500"></canvas>
	</div>
	<div class="uk-width-2-3@m uk-width-1-1@s">

		<div class="uk-grid-small" uk-grid>
			<div class="uk-width-expand">
				<label for="username-input" class="uk-form-label">Delay</label>
				<input type="number"
				       min="0"
				       step="1"
				       bind:value={delay}
				       class="uk-input uk-border-rounded">
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
					      uk-tooltip="{calculationStarted ? 'Continue' : 'Run'} calculation"
					      class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
					      uk-icon="play-circle"></span>
				{:else if status === Status.RUNNING}
					<span on:click={pauseCalc}
					      uk-tooltip="Pause calculation"
					      class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
					      uk-icon="pause-circle"></span>
				{/if}
			</div>
		</div>
		<p>
			{pi}
		</p>
	</div>
</div>