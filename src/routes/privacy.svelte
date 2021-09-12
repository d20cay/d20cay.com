<script>
	import {currentPage, Pages} from "../stores";
	import Privacy from "../components/Privacy.svelte";

	currentPage.set(Pages.PRIVACY);
</script>

<svelte:head>
	<title>Privacy Policy</title>
</svelte:head>


<div class="uk-container uk-container-small uk-margin">
	<h1>Privacy Policy</h1>

	<Privacy/>
</div>