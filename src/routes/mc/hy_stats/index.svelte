<script>
	import {currentPage, MinecraftPages} from "../../../stores";
	import {
		downloadableFileName,
		isProdInstance,
		LoadingStatus,
		NotificationPosition as Pos,
		NotificationStatus as Status,
		NotificationTimeout as Timeout,
		notify,
		updateUrl
	} from "../../../global";
	import {onMount} from "svelte";
	import ModeStats from "./ModeStats.svelte";

	currentPage.set(MinecraftPages.HY_STATS);

	const USER_INEXISTENT_ERROR = {code: -2, message: 'User doesn\'t have bedwars stats.'};
	const USER_MISSING_ERROR = {code: -3, message: 'User doesn\'t exist.'};
	const STATS_MISSING_ERROR = {code: -4, message: 'Stats not found for this user.'};

	const Mode = {
		GLOBAL: 0,
		EIGHT_ONE: 1,
		EIGHT_TWO: 3,
		FOUR_THREE: 4,
		FOUR_FOUR: 5,
		TWO_FOUR: 6,
	};

	const ModeMap = new Map([
		['global', Mode.GLOBAL],
		['8_1', Mode.EIGHT_ONE],
		['8_2', Mode.EIGHT_TWO],
		['4_3', Mode.FOUR_THREE],
		['4_4', Mode.FOUR_FOUR],
		['2_4', Mode.TWO_FOUR],
	]);

	const ModeReversemap = new Map([
		[Mode.GLOBAL, 'global'],
		[Mode.EIGHT_ONE, '8_1'],
		[Mode.EIGHT_TWO, '8_2'],
		[Mode.FOUR_THREE, '4_3'],
		[Mode.FOUR_FOUR, '4_4'],
		[Mode.TWO_FOUR, '2_4'],
	]);

	let loadingStatus = LoadingStatus.IDLE;

	let username = '';
	let isolatedUsername = '';
	let expectedError = true;
	let uuid = '';
	let stats = {};
	$: downloadableStats =
			"data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(stats));

	function downloadFileName() {
		return downloadableFileName(stats.playername, "hypixel_stats", new Date())
	}

	let linkMode;
	let mode;

	onMount(() => {
		const urlParams = window.location.search;
		const params = new URLSearchParams(urlParams);
		username = params.get('username');
		if (username) {
			getStats(username);
		}
	});

	async function getStats(username) {
		const prodApiUrl = `https://api.d20cay.com/hypixel/stats/${username}`;
		const devApiUrl = `http://localhost:8000/hypixel/stats/${username}`;

		expectedError = true;
		loadingStatus = LoadingStatus.LOADING;
		await fetch(isProdInstance() ? prodApiUrl : devApiUrl, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		}).then(response => response.json()).then(data => {
			if ('error' in data) {
				if (data.error === USER_INEXISTENT_ERROR.code) {
					throw USER_INEXISTENT_ERROR;
				}
				if (data.error === USER_MISSING_ERROR.code) {
					throw USER_MISSING_ERROR;
				}
				if (data.error === STATS_MISSING_ERROR.code) {
					throw STATS_MISSING_ERROR;
				}
			}
			loadingStatus = LoadingStatus.IDLE;
			stats = data;
			notify(`Successfully fetched stats. ${status}`,
					Status.SUCCESS,
					Pos.BOTTOM_LEFT,
					Timeout.QUICK);
		}).catch(status => {
			loadingStatus = LoadingStatus.FAILED;
			if (status ===
					USER_INEXISTENT_ERROR ||
					status ===
					USER_MISSING_ERROR ||
					status ===
					STATS_MISSING_ERROR) {
				isolatedUsername = username;
				expectedError = true;
			} else {
				expectedError = false;
			}
			notify(`Error fetching stats. ${'message' in status ? status.message : status}`,
					expectedError ? Status.WARNING : Status.DANGER,
					Pos.BOTTOM_LEFT,
					Timeout.CRITICAL);
		});
	}

	function keyPressed(e) {
		updateUrl([['username', username]]);
		if (e.key === 'Enter') {
			getStats(username);
		}
	}
</script>

<style>
	/** Changes the mouse cursor into a point (hand) when hovering over objects with this class. */
	.pointer-cursor:hover {
		cursor: pointer;
	}
</style>

<svelte:head>
	<title>d20cay | Hy BW Stats</title>
</svelte:head>

<h1 class="uk-text-center">
	Hypixel Bedwars Stats
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			A quicker way to look at your Hypixel Bedwars stats than <a href="https://plancke.io">plancke.io</a>.
		</p>
		<div class="uk-alert-warning" uk-alert>
			<p>Since there is no good documentation on the Hypixel API and the data provided by the
				API is ambiguous at times (e.g. nearly duplicate keys with different values) this
				page may not display the right information. I can't do anything about this because
				Hypixel won't reply to my posts. If enough people complain they might do something
				eventually so what you could do is create a post on the forums asking for an
				amendment.</p>
		</div>

		<ul uk-accordion>
			<li>
				<a class="uk-accordion-title normal-text">Mod</a>
				<div class="uk-accordion-content">
					<p>
						I created a mod to go along with this page. It allows you to open this page
						with the username of the player you want the stats from prefilled. To show
						the stats of a player enter the commend <code>/hybwstats d20cay</code>. You
						can also use the aliases <code>bwstats</code> or <code>bs</code> instead
						of<code>hybwstats</code> to shorten the command. <br>
						You're also not limited to only entering a single name. Just list all of the
						names of the players you want the stats of like this <code>/hybwstats d20cay
						d20ca</code>.
					</p>

					<h4>Example uses</h4>
					<ul>
						<li><code>/hybwstats d20cay</code></li>
						<li><code>/bwstats d20cay</code></li>
						<li><code>/bs d20cay</code></li>
						<li><code>/bs d20cay d20ca</code></li>
						<li><code>/bs d20cay d20cay gamerboy80 Chazm</code></li>
					</ul>

					<h4>Download the mod</h4>
					<div class="uk-flex uk-flex-center">
						<a href="resources/mc/hy_stats/hybwstats-1.1.0.jar"
						   class="uk-icon-button uk-margin-small-right"
						   uk-tooltip="Download HyBwStats mod"
						   uk-icon="download" download></a>
					</div>
				</div>
			</li>
		</ul>
	</div>
</div>

<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
	<div class="uk-grid-small" uk-grid>
		<div class="uk-width-expand">
			<label for="username-input" class="uk-form-label">Username</label>
			<input type="text"
			       bind:value={username}
			       on:keyup={keyPressed}
			       id="username-input"
			       placeholder="d20cay"
			       class="uk-input uk-border-rounded">
		</div>
		<div class="uk-width-auto">
			<label for="alignment-hack">&nbsp;<br></label>
			{#if loadingStatus === LoadingStatus.IDLE || loadingStatus === LoadingStatus.FAILED}
				<div class="uk-flex-bottom">
					<span on:click={() => getStats(username)}
					      uk-tooltip="Load stats"
					      class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
					      uk-icon="search"></span>
				</div>
			{:else if loadingStatus === LoadingStatus.LOADING}
				<span uk-tooltip="Loading..."
				      class="uk-icon-button uk-animation-fade uk-animation-fast"><div
						uk-spinner></div></span>
			{/if}
		</div>
		{#if Object.keys(stats).length}
			<div class="uk-width-auto">
				<label for="alignment-hack">&nbsp;<br></label>
				<div class="uk-flex-bottom">
					<a href={downloadableStats}
					   download={downloadFileName()}
					   uk-tooltip="Download stats"
					   class="uk-icon-button pointer-cursor uk-animation-fade uk-animation-fast"
					   uk-icon="download"></a>
				</div>
			</div>
		{/if}
		{#if username}
			<div class="uk-width-auto">
				<label for="alignment-hack">&nbsp;<br></label>
				<div class="uk-flex-bottom">
					<a href={`https://plancke.io/hypixel/player/stats/${username}#BedWars`}
					   target="_blank"
					   uk-tooltip="See on plancke.io"
					   class="uk-icon-button pointer-cursor"
					   uk-icon="external-link"></a>
				</div>
			</div>
		{/if}
	</div>


	{#if loadingStatus === LoadingStatus.LOADING}
		<div class="uk-text-center">
			<span class="uk-margin-top" uk-spinner="ratio: 3"></span>
		</div>
	{:else if loadingStatus === LoadingStatus.FAILED && expectedError}
		<div class="uk-alert-warning" uk-alert>
			<p>No bedwars stats found for the player {isolatedUsername}. This probably indicates
				that the player doesn't exist, hasn't played on Hypixel or played Bedwars on
				Hypixel. If you're certain that is not the case <a href="contact/">let me know</a>
				so I can fix the issue.</p>
		</div>
	{:else if loadingStatus === LoadingStatus.FAILED}
		<div class="uk-alert-danger" uk-alert>
			<p>Something bad happened. Some of my code probably broke. Please <a href="contact/">report
				this incident</a> with any details you have. Thank you!</p>
		</div>
	{:else if Object.keys(stats).length}
		<ul uk-tab>
			<li class:uk-active={linkMode === Mode.GLOBAL}>
				<a>Global</a>
			</li>
			<li class:uk-active={linkMode === Mode.EIGHT_ONE}>
				<a>Solo</a>
			</li>
			<li class:uk-active={linkMode === Mode.EIGHT_TWO}>
				<a>Doubles</a>
			</li>
			<li class:uk-active={linkMode === Mode.FOUR_THREE}>
				<a>Threes</a>
			</li>
			<li class:uk-active={linkMode === Mode.FOUR_FOUR}>
				<a>Fours</a>
			</li>
			<li class:uk-active={linkMode === Mode.TWO_FOUR}>
				<a>4v4</a>
			</li>
		</ul>
		<ul class="uk-switcher uk-margin">
			<li>
				<ModeStats {stats}
				           {loadingStatus}
				           {expectedError}
				           {isolatedUsername}
				           mode="global"/>
			</li>
			<li>
				<ModeStats {stats} {loadingStatus} {expectedError} {isolatedUsername} mode="8_1"/>
			</li>
			<li>
				<ModeStats {stats} {loadingStatus} {expectedError} {isolatedUsername} mode="8_2"/>
			</li>
			<li>
				<ModeStats {stats} {loadingStatus} {expectedError} {isolatedUsername} mode="4_3"/>
			</li>
			<li>
				<ModeStats {stats} {loadingStatus} {expectedError} {isolatedUsername} mode="4_4"/>
			</li>
			<li>
				<ModeStats {stats} {loadingStatus} {expectedError} {isolatedUsername} mode="2_4"/>
			</li>
		</ul>
	{:else}
		<p class="uk-text-center uk-margin-medium">
			Nothing here yet. Search for a player to show their stats here.
		</p>

	{/if}
</div>