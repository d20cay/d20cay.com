<script>
	import {currentPage, Page} from "../../../stores";
	import {onMount} from "svelte";
	import {updateUrl as _updateUrl} from "../../../global";
	import Generate from "./Generate.svelte";
	import Solve from "./Solve.svelte";

	currentPage.set(Page.SUDOKU);

	const Tab = {
		SOLVE: 0,
		GENERATE: 1,
	};

	const TabMap = new Map([
		['solve', Tab.SOLVE],
		['generate', Tab.GENERATE],
	]);

	const TabReversemap = new Map([
		[Tab.SOLVE, 'caesar'],
		[Tab.GENERATE, 'generate'],
	]);

	let linkTab;
	let tab;

	onMount(() => {
		const urlParams = window.location.search;
		const params = new URLSearchParams(urlParams);
		linkTab = tab = TabMap.get(params.get('tab'));
	});

	function updateTabState(s) {
		tab = s;
		updateUrl(tab);
	}

	function updateUrl(tab) {
		const params = tab !== undefined ? [
			['tab', TabReversemap.get(tab)]
		] : [];
		_updateUrl(params);
	}
</script>

<svelte:head>
	<title>d20cay | Sudoku Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Sudoku
</h1>

<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Since I got back into Sudoku recently (at the time of writing this) I sometimes got frustrated and felt like
			writing a few sudoku-related things instead of solving one. So here you go with a solver and a generator.
		</p>
	</div>
</div>

<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
	<ul uk-tab>
		<li class:uk-active={linkTab === Tab.SOLVE}>
			<a href="#" on:click={() => updateTabState(Tab.SOLVE)}>Solve</a>
		</li>
		<li class:uk-active={linkTab === Tab.GENERATE}>
			<a href="#" on:click={() => updateTabState(Tab.GENERATE)}>Generate</a>
		</li>
	</ul>
	<ul class="uk-switcher uk-margin">
		<li>
			<Solve/>
		</li>
		<li>
			<Generate/>
		</li>
	</ul>
</div>