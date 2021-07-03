<script>
	import {currentPage, Pages} from "../../../stores";
	import {calculateFactors, calculatePrimes} from "./prime_factorization";

	currentPage.set(Pages.PRIME_FACT);

	let input;
	let resultInput;
	let allPrimes = [];
	let factors = [];

	function calculate() {
		if (input === undefined) {
			return;
		}
		allPrimes = calculatePrimes(Math.floor(Math.sqrt(input)));
		factors = calculateFactors(input, allPrimes);
		resultInput = input;
	}

	function inputValid(input) {
		if (input === undefined) {
			return true;
		}
		return input === Math.floor(input);
	}
</script>

<style>
	/** Changes the mouse cursor into a point (hand) when hovering over objects with this class. */
	.pointer-cursor:hover {
		cursor: pointer;
	}
</style>

<svelte:head>
	<title>d20cay | Prime Factorization Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Prime Factorization
</h1>

<p class="uk-text-center">
	Calculate the prime factors of a given integer.
</p>

<div uk-grid>
	<div class="uk-width-expand">
		<label for="input-input" class="uk-form-label">
			Input
			<span class="uk-margin-small-right pointer-cursor"
			      uk-icon="info"
			      uk-tooltip="The number you would like to get the prime factors of"></span>
		</label>
		<input id="input-input"
		       type="number"
		       min="0"
		       step="1"
		       bind:value={input}
		       placeholder="923849"
		       class="uk-input uk-border-rounded"
		       class:uk-form-danger={!inputValid(input)}
		       uk-tooltip={inputValid(input) ? undefined : 'Input must be an integer'}>
	</div>
	<div class="uk-width-auto">
		<label for="alignment-hack">&nbsp;<br></label>
		<button on:click={calculate}
		        class="uk-button uk-button-primary uk-border-rounded"
		        disabled={!inputValid(input)}>
			Calculate
		</button>
	</div>
</div>

{#if allPrimes.length !== 0 && factors.length !== 0}
	<div class="uk-grid" uk-grid>
		<div class="uk-width-1-2">
			<h2>Relevant primes:</h2>
			{#each allPrimes as p}
				<div class="uk-card uk-card-default uk-card-small uk-card-body uk-margin-small uk-border-rounded">
					{p}
				</div>
			{/each}
		</div>
		<div class="uk-width-1-2">
			<h2>Factors of {resultInput}:</h2>
			{#each factors as f}
				<div class="uk-card uk-card-default uk-card-small uk-card-body uk-margin-small uk-border-rounded">
					{f}
				</div>
			{/each}
		</div>
	</div>
{/if}