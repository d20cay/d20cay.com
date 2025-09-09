<script>
	import {currentPage, Pages} from "../../../stores";
	import {onMount} from "svelte";
	import {intelliJShortcuts, chromeOsShortcuts, googleDocsShortcuts} from "./data";
	import {updateUrl as _updateUrl} from "../../../global";

	currentPage.set(Pages.PROGRAMS);

	const Section = {
		CSP: 0,
		INTELLIJ: 1,
		CHROME_OS: 2,
		GOOGLE_DOCS: 3
	};

	const SectionMap = new Map([
		['csp', Section.CSP],
		['intellij', Section.INTELLIJ],
		['chrome-os', Section.CHROME_OS],
		['googled-docs', Section.GOOGLE_DOCS]
	]);

	const SectionReversemap = new Map([
		[Section.CSP, 'csp'],
		[Section.INTELLIJ, 'intellij'],
		[Section.CHROME_OS, 'chrome-os'],
		[Section.GOOGLE_DOCS, 'google-docs']
	]);

	let linkSection;
	let section;

	onMount(() => {
		const urlParams = window.location.search;
		const params = new URLSearchParams(urlParams);
		linkSection = section = SectionMap.get(params.get('section'));
	});

	function updateSectionState(s) {
		if (section === s) {
			section = undefined;
		} else {
			section = s;
		}
		updateUrl(section);
	}

	function updateUrl(section) {
		const params = section !== undefined ? [
			['section', SectionReversemap.get(section)]
		] : [];
		_updateUrl(params);
	}
</script>

<style>
	.path {
		color: black;
	}
</style>

<svelte:head>
	<title>d20cay | Programs Cheatsheet</title>
</svelte:head>

<h1 class="uk-text-center">
	Programs Cheatsheet
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			An assortment of commands that might be useful to others or maybe even my if I it's even
			possible for me not to use an IDE for 24 hours.
		</p>
	</div>
</div>
<ul id="accordion" uk-accordion>
	<li class:uk-open={linkSection === Section.CSP} on:click={() => updateSectionState(Section.CSP)}>
		<!-- svelte-ignore a11y-missing-attribute -->
		<a class="uk-accordion-title">Clip Studio Paint</a>
		<div class="uk-accordion-content">
			<div uk-grid>
				<div class="uk-width-1-3@m uk-width-1-2@s">
					<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
						<h3 class="uk-card-title">Canvas Rotation and movement</h3>
						<div class="uk-overflow-auto">
							<table class="uk-table uk-table-hover uk-table-small">
								<thead>
									<tr>
										<th class="uk-table-expand">Description</th>
										<th class="uk-table-shrink">Shortcut</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Turn cursor into hand temporarily</td>
										<td><kbd>Space</kbd></td>
									</tr>
									<tr>
										<td>Turn cursor into zoom tool temporarily</td>
										<td><kbd>Ctrl+Space</kbd></td>
									</tr>
									<tr>
										<td>Turn cursor into rotate tool temporarily</td>
										<td><kbd>Shift+Space</kbd></td>
									</tr>
									<tr>
										<td>Reset rotation</td>
										<td><kbd>Shift+Space+double_click</kbd></td>
									</tr>
									<tr>
										<td>Fit to screen</td>
										<td><kbd>Ctrl+0</kbd></td>
									</tr>
									<tr>
										<td>Flip canvas</td>
										<td><kbd>Alt V V H</kbd></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
					<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
						<h3 class="uk-card-title">Tool shortcuts</h3>
						<div class="uk-overflow-auto">
							<table class="uk-table uk-table-hover table-small">
								<thead>
									<tr>
										<th class="uk-table-expand">Description</th>
										<th class="uk-table-shrink">Shortcut</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Blend tool</td>
										<td><kbd>J</kbd></td>
									</tr>
									<tr>
										<td>Switch between painting with color and opacity</td>
										<td><kbd>J</kbd></td>
									</tr>
									<tr>
										<td>Turn tool into color picker temporarily</td>
										<td><kbd>Alt</kbd></td>
									</tr>
									<tr>
										<td>Lasso transformation tool</td>
										<td><kbd>M</kbd></td>
									</tr>
									<tr>
										<td>Deselect</td>
										<td><kbd>Ctrl+D</kbd></td>
									</tr>
									<tr>
										<td>Add to selection</td>
										<td><kbd>Ctrl+selection</kbd></td>
									</tr>
									<tr>
										<td>Remove to selection</td>
										<td><kbd>Shift+selection</kbd></td>
									</tr>
									<tr>
										<td>Transform selection</td>
										<td><kbd>Ctrl+T</kbd></td>
									</tr>
									<tr>
										<td>Transform selection w/ mesh</td>
										<td><kbd>Alt E A M</kbd></td>
									</tr>
									<tr>
										<td>Move tool</td>
										<td><kbd>K</kbd></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
				<div class="uk-width-1-3@l uk-width-1-2@s">
					<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
						<h3>
							Tool property modification
						</h3>
						<div class="uk-overflow-auto">
							<table class="uk-table uk-table-hover table-small">
								<thead>
									<tr>
										<th class="uk-table-expand">Description</th>
										<th class="uk-table-shrink">Shortcut</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Modify brush size</td>
										<td><kbd>Ctrl+Alt+mouse-movement</kbd></td>
									</tr>
									<tr>
										<td>Decrease brush size</td>
										<td><kbd>[</kbd></td>
									</tr>
									<tr>
										<td>Increase brush size</td>
										<td><kbd>]</kbd></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
					<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
						<h3 class="uk-card-title">Misc</h3>
						<div class="uk-overflow-auto">
							<table class="uk-table uk-table-hover table-small">
								<thead>
									<tr>
										<th class="uk-table-expand">Description</th>
										<th class="uk-table-shrink">Shortcut</th>
										<th class="uk-table-shrink">Path</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Convert brightness to opacity</td>
										<td><kbd>Alt E B</kbd></td>
										<td><code class="path">Edit > Convert brightness to
											opacity</code></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
				<div class="uk-width-1-3@m uk-width-1-2@s">
					<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
						<h3 class="uk-card-title">Brush management palettes</h3>
						<h4>Quick Access</h4>
						<kbd>Gear icon on tool property tab</kbd>
						<p>All settings of selected tool</p>
					</div>
					<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
						<h3 class="uk-card-title">Layer tools</h3>
						<div class="uk-overflow-auto">
							<table class="uk-table uk-table-hover table-small">
								<thead>
									<tr>
										<th class="uk-table-expand">Description</th>
										<th class="uk-table-shrink">Name</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Only allow changes on non-transparent pixels</td>
										<td><code class="path">Lock transparent pixels</code></td>
									</tr>
									<tr>
										<td>Only shows changes on pixels overlapping with layer
											below
										</td>
										<td><code class="path">Clip to layer below</code></td>
									</tr>
									<tr>
										<td>Only shows changes on pixels overlapping with opaque
											pixels on
											mask
										</td>
										<td><code class="path">Create layer mask</code></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</li>
	<li class:uk-open={linkSection === Section.INTELLIJ}
	    on:click={() => updateSectionState(Section.INTELLIJ)}>
		<!-- svelte-ignore a11y-missing-attribute -->
		<a class="uk-accordion-title">IntelliJ</a>
		<div class="uk-accordion-content">
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover uk-table-small">
					<thead>
						<tr>
							<th>Default Shortcut</th>
							<th>Recommended Remapping</th>
							<th>Description</th>
						</tr>
					</thead>
					<tbody>
						{#each intelliJShortcuts as s}
							<tr>
								<td><kbd>{s.shortcut}</kbd></td>
								<td><kbd>{s.better_shortcut}</kbd></td>
								<td>{s.description}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	</li>
	<li class:uk-open={linkSection === Section.CHROME_OS}
	    on:click={() => updateSectionState(Section.CHROME_OS)}>
		<!-- svelte-ignore a11y-missing-attribute -->
		<a class="uk-accordion-title">ChromeOS</a>
		<div class="uk-accordion-content">
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover uk-table-small">
					<thead>
						<tr>
							<th>Default Shortcut</th>
							<th>Description</th>
						</tr>
					</thead>
					<tbody>
						{#each chromeOsShortcuts as s}
							<tr>
								<td><kbd>{s.shortcut}</kbd></td>
								<td>{s.description}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	</li>
	<li class:uk-open={linkSection === Section.GOOGLE_DOCS}
	    on:click={() => updateSectionState(Section.GOOGLE_DOCS)}><!-- svelte-ignore a11y-missing-attribute -->
		<a class="uk-accordion-title">Google Docs</a>
		<div class="uk-accordion-content">
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover uk-table-small">
					<thead>
						<tr>
							<th>Default Shortcut</th>
							<th>Description</th>
						</tr>
					</thead>
					<tbody>
						{#each googleDocsShortcuts as s}
							<tr>
								<td><kbd>{s.shortcut}</kbd></td>
								<td>{s.description}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	</li>
</ul>