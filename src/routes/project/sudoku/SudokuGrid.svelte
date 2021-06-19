<script>
	export let board = [
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
		[undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined],
	];

	function boardRightSize(b) {
		return b.length === 9 && b.filter(r => r.length === 9).length;
	}

	$: console.log(board);
</script>

<style>
	table {
		position: relative;
		width: 40%;
		height: 0;
		padding-bottom: 40%;
	}

	td {
		border: 1px solid;
	}

	td:first-child {
		border-left: solid;
	}

	td:nth-child(3n) {
		border-right: solid;
	}

	tr:first-child {
		border-top: solid;
	}

	tr:nth-child(3n) td {
		border-bottom: solid;
	}
</style>

{#if boardRightSize(board)}
	<table class="uk-table uk-table-small uk-table-middle uk-text-center uk-overflow-auto">
		<tbody>
			{#each board as row}
				<tr>
					{#each row as field}
						<td class="uk-table-shrink">
							<input type="number" class="uk-input uk-form-blank uk-form-width-xsmall" bind:value={field}>
						</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>
{:else }
	<div class="uk-alert-danger" uk-alert>
		<p>The sudoku board doesn't have the right length. This is a bug. Please <a href="/contact/">contact me</a>, so
			I can fix this.</p>
	</div>
{/if}