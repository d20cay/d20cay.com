<script>
    import DuplicateTableRow from "./DuplicateTableRow.svelte";

    export let duplicates;
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
	{#each duplicates as duplicate}
		<DuplicateTableRow {duplicate}/>
	{/each}
	</tbody>
</table>