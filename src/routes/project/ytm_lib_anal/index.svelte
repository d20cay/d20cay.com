<script>
	import {currentPage, ProjectPages} from "../../../stores";
	import {
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

	let loadingStatus = LoadingStatus.IDLE;

	let cookie;
	let x_goog_user;
	let library;
	let analysis;

	function inputsValid() {
		return cookie !== "" && x_goog_user !== "";
	}

	async function requestLibData() {
		const prodApiUrl = `https://api.d20cay.com/ytm/lib`;
		const devApiUrl = `http://localhost:8000/ytm/lib`;

		loadingStatus = LoadingStatus.LOADING;
		await fetch(isProdInstance() ? prodApiUrl : devApiUrl, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({cookie, x_goog_user})
		}).then(response => {
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
			notify('Error fetching library contents and analysis data.', Status.DANGER, Pos.BOTTOM_LEFT, Timeout.CRITICAL);
		});
	}
</script>

<svelte:head>
	<title>d20cay | YT Music Library Analysis Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Music Library Analysis
</h1>

<div class="uk-width-2-3@m uk-align-center">
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

	<div class="uk-alert-danger" uk-alert>
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

	{#if library !== undefined}
		<ul uk-accordion>
			<li>
				<!-- svelte-ignore a11y-invalid-attribute -->
				<a class="uk-accordion-title" href="#">Library Contents Summary</a>
				<!--Adds padding only on the left side to create an indent for every category.-->
				<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
					<ol>
						<li>Library Songs
							<ol type="a">
								{#each library.songs as song}
									<li><a href={getSongShareString(song.videoId)}>{song.title}</a></li>
								{/each}
							</ol>
						</li>
						{#each library.playlists as playlist}
							<li>
								<a href={getPlaylistShareString(playlist.id)}>{playlist.title}</a>
								<ol type="a">
									{#each playlist.tracks as song}
										<li><a href={getSongShareString(song.videoId)}>{song.title}</a></li>
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
		<p class="uk-text-center uk-margin-medium">
			Nothing here yet. Enter your credentials to show information and options here.
		</p>
	{/if}

</div>

