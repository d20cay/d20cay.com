<script>
    import {currentPage, ProjectPages} from "../../../stores";

    currentPage.set(ProjectPages.YTM_LIB);
</script>

<svelte:head>
	<title>d20cay | YT Music Library Analysis Project</title>
</svelte:head>

<h1 class="uk-text-center">
	YT Music Library Analysis
</h1>

<div class="uk-width-2-3@m uk-align-center">
	<p class="uk-text-center">
		A tool to analyze and clean up your YTM library.
	</p>

	<p>
		For Chrome users:To operate this tool open a new tab, press F12 and open the Network tab. Now navigate to <a
			href="https://music.youtube.com">music.youtube.com</a> and filter the requests by typing <code>/browse</code> in
		the <q>Filter</q> field. Click on any of the requests that show up and navigate to the <q>Request Headers</q>
		section, where you will copy the text after <q>:cookie:</q> and <q>x-goog-user</q> into their respective fields.
	</p>
</div>

