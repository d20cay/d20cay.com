<script>
	import DuplicateTableRow from "./DuplicateTableRow.svelte";

	export let duplicates;

	const MAX_DEFAULT_ISSUE_COUNT = 30;
	const ISSUE_ITEM_INCREMENT = 50;

	let issueItemCount = MAX_DEFAULT_ISSUE_COUNT;
</script>

<table class="uk-table uk-table-overflow-auto">
	<thead>
		<tr>
			<th>Song Title</th>
			<th>Duplicate Song Title</th>
			<th>Artists</th>
			<th>Duplicate Artists</th>
			<th>Playlist</th>
			<th>Duplicate Playlist</th>
		</tr>
	</thead>
	<tbody>
		{#each duplicates as duplicate, i}
			{#if i < issueItemCount}
				<DuplicateTableRow {duplicate}/>
			{/if}
			{#if i === issueItemCount - 1 && issueItemCount < duplicates.length}
				<li class="more-li"><a on:click={() => issueItemCount += ISSUE_ITEM_INCREMENT}>+{duplicates.length -
				issueItemCount} more</a>
				</li>
			{/if}
		{/each}
	</tbody>
</table>