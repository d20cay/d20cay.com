<script>
	import {currentPage, Pages} from "../stores";
	import {changelog, Type, TypeMap, TypeTextMap} from "../changelog";

	currentPage.set(Pages.CHANGELOG);

	function checkPlusVersion(versionString) {
		return versionString.match(/\d{4}\.\d{1,2}.\d{1,}\+/);
	}
</script>

<style>
	.table-small th,
	.table-small td {
		padding: 3px 5px;
	}

	/** Changes the mouse cursor into a point (hand) when hovering over objects with this class. */
	.pointer-cursor:hover {
		cursor: pointer;
	}
</style>

<div class="uk-container uk-container-xsmall">
	<h1 class="uk-text-center">Changelog</h1>

	{#each changelog as changeday}
		<h2 class="uk-margin-small-bottom">
			{changeday.date}
		</h2>
		<h5 class="uk-margin-small-top uk-margin-small-bottom">
			{changeday.version}
			{#if checkPlusVersion(changeday.version)}
				<span class="uk-margin-small-right pointer-cursor"
				      uk-icon="info"
				      uk-tooltip="Changes were committed after week in version name concluded. Usually because of a complicated release."></span>
			{/if}
		</h5>

		<table class="uk-table uk-table-hover table-small uk-margin-small-top">
			<thead class="uk-invisible">
				<tr>
					<th class="uk-width-small"></th>
					<th></th>
				</tr>
			</thead>
			<tbody>
				{#each changeday.changes as change}
					<tr>
						<td>
						<span class="uk-label uk-label-{TypeMap.get(change.type)} uk-text-center uk-width-small">{TypeTextMap.get(
							change.type)}</span>
						</td>
						<td>{@html change.text}</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/each}
</div>