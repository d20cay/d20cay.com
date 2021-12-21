<script>
	import {currentPage, ProjectPages} from "../../../stores";
	import {
		downloadableFileName,
		isProdInstance,
		LoadingStatus,
		NotificationPosition as Pos,
		NotificationStatus as Status,
		NotificationTimeout as Timeout,
		notify
	} from "../../../global";
	import {getPlaylistShareString, getSongShareString} from "./util";
	import DuplicatesTable from "./DuplicatesTable.svelte";

	currentPage.set(ProjectPages.YTM_LIB);

	const INCORRECT_PAYLOAD = {code: -5, message: 'POST body in incorrect format.'};
	const MAX_DEFAULT_PLAYLIST_ITEM_COUNT = 30;
	const PLAYLIST_ITEM_INCREMENT = 50;
	const WAIT_TIME_FOR_LONG_LOAD_INDICATION = 5 * 1000;

	let loadingStatus = LoadingStatus.IDLE;
	let loadTakingLong = false;

	let cookie;
	let x_goog_user = 1;
	let excludeAll = true;
	let excludeForeign = false;
	let username;
	let library;
	let analysis;

	$: downloadableAnalysis =
			"data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify({library, analysis}));

	$: excludeForeign = username !== undefined && username !== null && username !== "";

	// Stores current amount of songs displayed for each playlist in the library overview.
	$: playlistItemDisplayCount =
			library === undefined ?
					undefined :
					new Array(library.playlists.length + 1).fill(MAX_DEFAULT_PLAYLIST_ITEM_COUNT);

	function downloadFileName() {
		return downloadableFileName("", "ytm_analysis", new Date())
	}

	function inputsValid() {
		return cookie !== "" && x_goog_user !== "";
	}

	async function requestLibData() {
		const prodApiUrl = `https://api.d20cay.com/ytm/lib`;
		const devApiUrl = `http://localhost:8000/ytm/lib`;

		loadingStatus = LoadingStatus.LOADING;
		const loadTakingLongTimeout = setTimeout(() => loadTakingLong = true, WAIT_TIME_FOR_LONG_LOAD_INDICATION)
		await fetch(isProdInstance() ? prodApiUrl : devApiUrl, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				cookie,
				x_goog_user,
				excludeAllPlaylist: excludeAll,
				excludeForeignPlaylists: excludeForeign,
				username
			})
		}).then(response => {
			clearTimeout(loadTakingLongTimeout);
			loadTakingLong = false;
			if (response.status === 422) {
				throw INCORRECT_PAYLOAD;
			}
			return response.json();
		}).then(data => {
			loadingStatus = LoadingStatus.IDLE;
			library = data.library;
			analysis = data.analysis;
			console.log(data);
			notify('Successfully fetched library contents and analysis data.',
					Status.SUCCESS,
					Pos.BOTTOM_LEFT,
					Timeout.QUICK);
		}).catch(() => {
			loadingStatus = LoadingStatus.IDLE;
			notify('Error fetching library contents and analysis data.',
					Status.DANGER,
					Pos.BOTTOM_LEFT,
					Timeout.CRITICAL);
		});
	}

	function increasePlaylistItemDisplayCount(index) {
		let newPlaylistItemDisplayCount = [...playlistItemDisplayCount]
		newPlaylistItemDisplayCount[index] += PLAYLIST_ITEM_INCREMENT;
		playlistItemDisplayCount = newPlaylistItemDisplayCount
	}
</script>

<style>
	.more-li {
		list-style: none;
	}
</style>

<svelte:head>
	<title>d20cay | YT Music Library Analysis Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Music Library Analysis
</h1>

<p class="uk-text-center">
	Tool to analyze and clean up your YTM library.
</p>

<p>
	For Chrome users: To operate this tool open a new tab, press F12 and open the Network tab. Now navigate to <a
		href="https://music.youtube.com">music.youtube.com</a> and filter the requests by typing
	<code>/browse</code> in
	the <q>Filter</q> field. Click on any of the requests that show up and navigate to the <q>Request Headers</q>
	section, where you will copy the text after <q>:cookie:</q> and <q>:x-goog-user:</q> into their respective
	fields.
</p>

<div class="uk-alert-danger uk-border-rounded" uk-alert>
	<p>Make sure you trust this website before entering your credentials! Yes, I am warning you of my own website.
		Once you enter your credentials I could potentially store them and wreak complete havoc on your YTM library.
		I will not, because I don't care to be this destructive. You should just be aware of this.</p>
	<p>If you're worried I might have stolen your credentials you can log out of your YTM account from the machine
		you got the credentials from, which will invalidate those credentials. You can also take a look at all of
		the code on my GitHub. You can find the link to my GitHub on the homepage.</p>
</div>

<div uk-grid class="uk-grid-small">
	<div class="uk-width-auto@m uk-width-1-1@s">
		<label for="cookie-input" class="uk-form-label">
			cookie
		</label>
		<input id="cookie-input"
		       type="text"
		       bind:value={cookie}
		       class="uk-input uk-border-rounded">
	</div>

	<div class="uk-width-auto@m uk-width-1-1@s">
		<label for="authuser-input" class="uk-form-label">
			x-goog-authuser
		</label>
		<input id="authuser-input"
		       type="text"
		       bind:value={x_goog_user}
		       class="uk-input uk-border-rounded">
	</div>
	<div class="uk-width-auto">
		<div class="uk-margin">
			<label for="alignment-hack">&nbsp;<br></label>
			<button on:click={requestLibData}
			        class="uk-button uk-button-primary uk-border-rounded"
			        disabled={!inputsValid()}>
				{#if loadingStatus === LoadingStatus.IDLE || loadingStatus === LoadingStatus.FAILED}
					Run
				{:else if loadingStatus === LoadingStatus.LOADING}
					<span uk-tooltip="Loading..."
					      class="uk-animation-fade uk-animation-fast"><div
							uk-spinner></div></span>
				{/if}
			</button>
		</div>
	</div>
	{#if analysis !== undefined && library !== undefined}
		<div class="uk-width-auto">
			<label for="alignment-hack">&nbsp;<br></label>
			<div class="uk-flex-bottom">
				<a href={downloadableAnalysis}
				   download={downloadFileName()}
				   uk-tooltip="Download analysis result"
				   class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
				   uk-icon="download"></a>
			</div>
		</div>
	{/if}
</div>

<ul uk-accordion>
	<li>
		<a class="uk-accordion-title normal-text" href="#">Advanced</a>
		<div class="uk-accordion-content">
			<div uk-grid class="uk-grid-small">
				<div class="uk-width-1-3@m uk-width-1-1@s">
					<input id="exclude-all-checkbox"
					       type="checkbox"
					       bind:checked={excludeAll}
					       class="uk-checkbox uk-border-rounded">
					<label for="exclude-all-checkbox" class="uk-form-label">
						Exclude any playlists named "All" from analysis. (case-sensitive)
					</label><br>

					<input id="exclude-foreign-checkbox"
					       disabled
					       type="checkbox"
					       bind:checked={excludeForeign}
					       class="uk-checkbox uk-border-rounded">
					<label for="exclude-foreign-checkbox" class="uk-form-label">
						Ignore playlists not created by `username`. This is automatically enabled as soon as you write
						something in the username field.
					</label>
				</div>

				<div class="uk-width-auto@m uk-width-1-1@s">
					<label for="username-input" class="uk-form-label">
						Username
					</label>
					<input id="username-input"
					       type="text"
					       bind:value={username}
					       class="uk-input uk-border-rounded">
				</div>
			</div>
		</div>
	</li>
</ul>


{#if library !== undefined}
	<ul uk-accordion>
		<li>
			<!-- svelte-ignore a11y-invalid-attribute -->
			<a class="uk-accordion-title" href="#">Library Contents Summary</a>
			<!--Adds padding only on the left side to create an indent for every category.-->
			<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
				<ol>
					<li>Library Songs ({library.songs.length} items)
						<ol type="a">
							{#each library.songs as song, i}
								{#if i < playlistItemDisplayCount[0]}
									<li><a href={getSongShareString(song.videoId)}>{song.title}</a></li>
								{/if}
								{#if i ===
								playlistItemDisplayCount[0] - 1 &&
								playlistItemDisplayCount[0] <
								library.songs.length}
									<li class="more-li"><a
											on:click={() => increasePlaylistItemDisplayCount(0)}>+{library.songs.length -
									playlistItemDisplayCount[0]} more</a>
									</li>
								{/if}
							{/each}
						</ol>
					</li>
					{#each library.playlists as playlist, i}
						<li>
							<a href={getPlaylistShareString(playlist.id)}>{playlist.title}</a> ({playlist.tracks.length}
							items)
							<ol type="a">
								{#each playlist.tracks as song, j}
									{#if j < playlistItemDisplayCount[i]}
										<li><a href={getSongShareString(song.videoId)}>{song.title}</a></li>
									{/if}
									{#if j ===
									playlistItemDisplayCount[i] - 1 &&
									playlistItemDisplayCount[i] <
									library.songs.length}
										<li class="more-li"><a
												on:click={() => increasePlaylistItemDisplayCount(i)}>+{playlist.tracks.length -
										playlistItemDisplayCount[i]} more</a>
										</li>
									{/if}
								{/each}
							</ol>
						</li>
					{/each}
				</ol>
			</div>
		</li>
		<li>
			<!-- svelte-ignore a11y-invalid-attribute -->
			<a class="uk-accordion-title" href="#">Duplicate analysis</a>
			<!--Adds padding only on the left side to create an indent for every category.-->
			<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
				<p>
					Possible duplicates are categorized in four ways:
				</p>
				<ol>
					<li>ID Duplicates: The exact same song is duplicated.</li>
					<li>Artist & Title Duplicates: The title and artist of the two songs are exactly the same, but
						the ID
						isn't.
					</li>
					<li>Title Duplicates: The title of the two songs are exactly the same, but the artist and ID are
						different. These may simply be covers.
					</li>
					<li>Simplified Title Duplicates: The title, after removing anything in parentheses is exactly
						the same, but the ID is different. The artist may be the same. These could be two different
						versions from the same artist, e.g. it was created in a collaboration with another artist or
						it's the acoustic version.
					</li>
				</ol>

				<ul uk-accordion="multiple: true">
					<li>
						<!-- svelte-ignore a11y-invalid-attribute -->
						<a class="uk-accordion-title" href="#">Library Song Duplicates
							({analysis.duplicates.library.totalDuplicateCount})</a>
						<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
							<ul uk-accordion="multiple: true">
								{#if analysis.duplicates.library.idDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">ID Duplicates
											({analysis.duplicates.library.idDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable duplicates={analysis.duplicates.library.idDuplicates}/>
										</div>
									</li>
								{/if}
								{#if analysis.duplicates.library.titleArtistDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">Title & Artist Duplicates
											({analysis.duplicates.library.titleArtistDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.library.titleArtistDuplicates}/>
										</div>
									</li>
								{/if}
								{#if analysis.duplicates.library.titleDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">Title Duplicates
											({analysis.duplicates.library.titleDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.library.titleDuplicates}/>
										</div>
									</li>
								{/if}
								{#if analysis.duplicates.library.simpleTitleDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">Simplified Title Duplicates
											({analysis.duplicates.library.simpleTitleDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.library.simpleTitleDuplicates}/>
										</div>
									</li>
								{/if}
							</ul>
						</div>
					</li>
					<li>
						<!-- svelte-ignore a11y-invalid-attribute -->
						<a class="uk-accordion-title" href="#">Playlist Duplicates
							({analysis.duplicates.playlists.totalDuplicateCount})</a>
						<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
							<ul uk-accordion="multiple: true">
								{#if analysis.duplicates.playlists.idDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">ID Duplicates
											({analysis.duplicates.playlists.idDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.idDuplicates}/>
										</div>
									</li>
								{/if}
								{#if analysis.duplicates.playlists.titleArtistDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">Title & Artist Duplicates
											({analysis.duplicates.library.titleArtistDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.titleArtistDuplicates}/>
										</div>
									</li>
								{/if}
								{#if analysis.duplicates.playlists.titleDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">Title Duplicates
											({analysis.duplicates.playlists.titleDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.titleDuplicates}/>
										</div>
									</li>
								{/if}
								{#if analysis.duplicates.playlists.simpleTitleDuplicates.length !== 0}
									<li>
										<!-- svelte-ignore a11y-invalid-attribute -->
										<a class="uk-accordion-title" href="#">Simplified Title Duplicates
											({analysis.duplicates.playlists.simpleTitleDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.simpleTitleDuplicates}/>
										</div>
									</li>
								{/if}
							</ul>
						</div>
					</li>
				</ul>
			</div>
		</li>
	</ul>
{:else}
	{#if loadTakingLong}
		<div class="uk-alert-primary uk-border-rounded" uk-alert>
			<p>The loading duration of this tool might be quite extensive. My library contains about 1500 items, which
				results in an output file of 2 MB, which has to be processed in approximately 3.8 * 10^6
				comparisons. Depending on the amount of duplicates the output file might even double and needs to be
				sent from the backend to the frontend. Trust me when I tell you that you can't write the analysis in
				javascript. I tried. I really did.</p>
			<p>In my case the whole run takes about <i>40 seconds</i> from the small sample I took.</p>
		</div>
	{/if}
	<p class="uk-text-center uk-margin-medium">
		Nothing here yet. Enter your credentials to show information and options here.
	</p>
{/if}
