<script>
	import SudokuGrid from "./SudokuGrid.svelte";
	import {defaultBoard} from "./sudoku";

	let board = defaultBoard;

	function solve(b) {


	}

	function boardValid(b) {
		return b.flatMap(r => r.filter(f => f === undefined || (f > 0 && f < 10))).length === 9 ** 2;
	}
</script>

<SudokuGrid bind:board/>

<button on:click={solve(board)} disabled={!boardValid(board)} class="uk-button uk-button-primary uk-border-rounded">
	Solve
</button>