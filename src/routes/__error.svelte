<script context="module">
	/** @type {import('@sveltejs/kit').ErrorLoad} */
	export function load({error, status}) {
		return {
			props: {
				error,
				status
			}
		};
	}
</script>

<script>
	import {dev} from '$app/env';

	export let error;
	export let status;
</script>

<style>
	h1, p {
		margin: 0 auto;
	}

	h1 {
		font-size: 2.8em;
		font-weight: 700;
		margin: 0 0 0.5em 0;
	}

	p {
		margin: 1em auto;
	}

	@media (min-width: 480px) {
		h1 {
			font-size: 4em;
		}
	}
</style>

<svelte:head>
	<title>{status}</title>
</svelte:head>

<h1>{status}</h1>

<p>{error.message}</p>
<p>Something either went terribly wrong, in which case I'm sorry for the inconvenience, or you
	caused this error yourself. If this is your doing, you can <a href="/">see yourself out</a>.</p>

{#if dev && error.stack}
	<pre>{error.stack}</pre>
{/if}
