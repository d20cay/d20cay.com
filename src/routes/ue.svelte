<script>
	import {onMount} from 'svelte';
	import {goto} from '@sapper/app';

	onMount(() => {
		const params = new URLSearchParams();
		params.set('referrer', 'ue');
		goto(`/project/umlaut?${params.toString()}`);
	});
</script>