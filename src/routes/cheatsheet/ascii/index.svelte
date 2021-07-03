<script>
	import {currentPage, Pages} from "../../../stores";
	import {asciiCharacter} from "./data";
	import {overwriteClipboard} from "../../../global";

	currentPage.set(Pages.ASCII);

	const notACharacterCharCodes = [129, 141, 143, 144, 157];
</script>

<style>
	.table-small th,
	.table-small td {
		padding: 3px 5px;
	}
</style>

<svelte:head>
	<title>d20cay | Ascii Table</title>
</svelte:head>

<h1 class="uk-text-center">
	Ascii Table
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Quick reference for ASCII characters, taken from <a href="http://asciitable.com">asciitable.com</a>
			and
			<a href="http://websitebuilders.com/tools/html-codes/ascii/">websitebuilders.com</a>.
		</p>
	</div>
</div>

<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
	<h3 class="uk-card-title">ASCII</h3>
	<div class="uk-overflow-auto">
		<table class="uk-table uk-table-hover table-small">
			<thead>
				<tr>
					<th>Decimal</th>
					<th>Hex</th>
					<th>Oct</th>
					<th>Html</th>
					<th>Character</th>
					<th></th>
					<th>Description</th>
				</tr>
			</thead>
			<tbody>
				{#each asciiCharacter as character}
					<tr>
						<td>{character.dec}</td>
						<td>{character.hex}</td>
						<td>{character.oct}</td>
						{#if (character.dec - 1) >= 32 && (character.dec - 1) <= 256}
							<td>{character.html}</td>
							{#if !notACharacterCharCodes.includes(character.dec)}
								<td>
									<span id="{`char${character.dec}`}">{@html `&#${character.dec};`}</span>
								</td>
								<td>
									<a on:click={() => overwriteClipboard(String.fromCharCode(character.dec))}
									   uk-tooltip="Copy character"
									   class="uk-icon-button uk-margin-small-right"
									   uk-icon="copy"></a>
								</td>
							{:else}
								<td></td>
								<td></td>
							{/if}
						{:else}
							<td></td>
							<td></td>
							<td></td>
						{/if}
						<td>{character.desc}</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>