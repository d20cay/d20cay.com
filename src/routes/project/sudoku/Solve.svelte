<script>
	import SudokuGrid from "./SudokuGrid.svelte";

	let board;

	function solve(b) {

	}
</script>

<SudokuGrid {board}/>

<button on:click={solve(board)} class="uk-button uk-button-primary uk-border-rounded">Solve</button>