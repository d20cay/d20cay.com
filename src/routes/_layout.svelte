<script>
	import {currentPage, Page} from "../stores";
	import Navbar from '../components/Navbar.svelte';
	import Footer from '../components/Footer.svelte';
	import {onDestroy} from "svelte";

	let currentPageValue;

	const unsubscribeCurrentPage = currentPage.subscribe(value => currentPageValue = value);
	onDestroy(() => unsubscribeCurrentPage());
</script>

<style>
	.spacer {
		margin-bottom: 300px;
	}
</style>

{#if currentPageValue !== Page.UNKNOWN && currentPageValue !== Page.HOME}
	<Navbar currentPage={currentPageValue}/>
{/if}

<main class="uk-container uk-container-xlarge uk-margin-large-top uk-margin-large-bottom">
	<slot></slot>
</main>
{#if currentPageValue !== Page.UNKNOWN && currentPageValue !== Page.HOME}
	<div class="spacer"></div>
	<Footer/>
{/if}