<script>
	import {onMount} from 'svelte';
	import {goto} from '@sapper/app';

	onMount(() => {
		const params = new URLSearchParams();
		params.set('referrer', 'oe');
		goto(`/project/umlaut?${params.toString()}`);
	});
</script>