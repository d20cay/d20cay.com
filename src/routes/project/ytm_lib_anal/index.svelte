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

	currentPage.set(ProjectPages.YTM_LIB);

	const INCORRECT_PAYLOAD = {code: -5, message: 'POST body in incorrect format.'};

	let loadingStatus = LoadingStatus.IDLE;

	let cookie;
	let x_goog_user;
	let library;

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
			library = data;
			notify('Successfully fetched library contents.',
					Status.SUCCESS,
					Pos.BOTTOM_LEFT,
					Timeout.QUICK);
		}).catch(() => notify('Error fetching library contents.', Status.DANGER, Pos.BOTTOM_LEFT, Timeout.CRITICAL));
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
</div>

