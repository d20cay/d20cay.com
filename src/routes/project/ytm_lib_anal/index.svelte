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
	import {test} from "./test";
	import {duplicateAnalysis} from "./analysis";
	import DuplicateTableRow from "./DuplicateTableRow.svelte";
	import DuplicatesTable from "./DuplicatesTable.svelte";

	currentPage.set(ProjectPages.YTM_LIB);

	const INCORRECT_PAYLOAD = {code: -5, message: 'POST body in incorrect format.'};

	let loadingStatus = LoadingStatus.IDLE;

	let cookie;
	let x_goog_user;
	let library;
	let analysis;

	$: analysis = analyze(library);

	function inputsValid() {
		return cookie !== "" && x_goog_user !== "";
	}

	async function requestLibData() {
		const prodApiUrl = `https://api.d20cay.com/ytm/lib`;
		const devApiUrl = `http://localhost:8000/ytm/lib`;

		// TODO: remove for prod
		library = test;
		return;

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
			library = data;
			notify('Successfully fetched library contents.',
					Status.SUCCESS,
					Pos.BOTTOM_LEFT,
					Timeout.QUICK);
		}).catch(() => {
			loadingStatus = LoadingStatus.IDLE;
			notify('Error fetching library contents.', Status.DANGER, Pos.BOTTOM_LEFT, Timeout.CRITICAL);
		});
	}

	function analyze(library) {
		if (library === undefined) {
			return undefined;
		}
		// TODO: Remove for prod
		return {'duplicates': duplicateAnalysis(library)};
	}
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
		For Chrome users: To operate this tool open a new tab, press F12 and open the Network tab. Now navigate to <a
			href="https://music.youtube.com">music.youtube.com</a> and filter the requests by typing
		<code>/browse</code> in
		the <q>Filter</q> field. Click on any of the requests that show up and navigate to the <q>Request Headers</q>
		section, where you will copy the text after <q>:cookie:</q> and <q>:x-goog-user:</q> into their respective
		fields.
	</p>

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

					<ul uk-accordion>
						<li>
							<a class="uk-accordion-title" href="#">Library Song Duplicates
								({analysis.duplicates.library.totalDuplicates})</a>
							<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">ID Duplicates
											({analysis.duplicates.library.idDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable duplicates={analysis.duplicates.library.idDuplicates}/>
										</div>
									</li>
								</ul>
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">Title & Artist Duplicates
											({analysis.duplicates.library.titleArtistDuplicates.length})</a>
										<div class="uk-accordion-content">
											<DuplicatesTable
													duplicates={analysis.duplicates.library.titleArtistDuplicates}/>
										</div>
									</li>
								</ul>
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">Title Duplicates
											({analysis.duplicates.library.titleDuplicates.length})</a>
										<div class="uk-accordion-content">
											<DuplicatesTable duplicates={analysis.duplicates.library.titleDuplicates}/>
										</div>
									</li>
								</ul>
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">Simplified Title Duplicates
											({analysis.duplicates.library.simpleTitleDuplicates.length})</a>
										<div class="uk-accordion-content">
											<DuplicatesTable
													duplicates={analysis.duplicates.library.simpleTitleDuplicates}/>
										</div>
									</li>
								</ul>
							</div>
						</li>
						<li>
							<a class="uk-accordion-title" href="#">Playlist Duplicates
								({analysis.duplicates.playlists.totalDuplicates})</a>
							<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">ID Duplicates
											({analysis.duplicates.playlists.idDuplicates.length})</a>
										<div class="uk-accordion-content uk-padding uk-padding-remove-top uk-padding-remove-right uk-padding-remove-bottom">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.idDuplicates}/>
										</div>
									</li>
								</ul>
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">Title & Artist Duplicates
											({analysis.duplicates.library.titleArtistDuplicates.length})</a>
										<div class="uk-accordion-content">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.titleArtistDuplicates}/>
										</div>
									</li>
								</ul>
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">Title Duplicates
											({analysis.duplicates.playlists.titleDuplicates.length})</a>
										<div class="uk-accordion-content">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.titleDuplicates}/>
										</div>
									</li>
								</ul>
								<ul uk-accordion>
									<li>
										<a class="uk-accordion-title" href="#">Simplified Title Duplicates
											({analysis.duplicates.playlists.simpleTitleDuplicates.length})</a>
										<div class="uk-accordion-content">
											<DuplicatesTable
													duplicates={analysis.duplicates.playlists.simpleTitleDuplicates}/>
										</div>
									</li>
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

