<script>
	import {currentPage, Page} from "../../stores";
	import {
		isDevInstance,
		isProdInstance,
		LoadingStatus,
		NotificationPosition as Pos,
		NotificationStatus as Status,
		NotificationTimeout as Timeout,
		notify,
		overwriteClipboard,
		updateUrl
	} from "../../global";
	import {onMount} from "svelte";

	currentPage.set(Page.HY_STATS);

	const USER_INEXISTENT_ERROR = {code: -2, message: 'User doesn\'t have bedwars stats.'};
	const USER_MISSING_ERROR = {code: -3, message: 'User doesn\'t exist.'};
	const STATS_MISSING_ERROR = {code: -4, message: 'Stats not found for this user.'};

	let loadingStatus = LoadingStatus.IDLE;

	let username = '';
	let isolatedUsername = '';
	let expectedError = true;
	let uuid = '';
	let stats = {};

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
		return await fetch(isProdInstance() ? prodApiUrl : devApiUrl, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		}).then(response => response.json()).then(data => {
			if ('error' in data) {
				if (data.error === 'Bedwars stats not found.') {
					throw USER_INEXISTENT_ERROR;
				}
				if (data.error === 'Player not found.') {
					throw USER_MISSING_ERROR;
				}
				if (data.error === 'Stats not found.') {
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

	function vo(value) {
		return value ? value : 'NaN';
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
				<a class="uk-accordion-title normal-text" href="#">Mod</a>
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
			{/if}
			{#if loadingStatus === LoadingStatus.LOADING}
				<span uk-tooltip="Loading..."
				      class="uk-icon-button uk-animation-fade uk-animation-fast"><div
						uk-spinner></div></span>
			{/if}
		</div>
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
		<h4>
			{stats.playername}'s Hypixel Bedwars Statistics
		</h4>
		<div uk-grid>
			<div class="uk-width-1-4@l uk-width-1-2@s">
				<div class="uk-overflow-auto">
					<table class="uk-table uk-table-small uk-table-divider">
						<tbody>
							<tr>
								<td><span class="uk-margin-small-right" uk-icon="star"></span></td>
								<td>{vo(stats.bedwars.level)}</td>
							</tr>
							<tr>
								<td>Games Played</td>
								<td>{vo(stats.bedwars.games_played)}</td>
							</tr>
							<tr>
								<td>Beds Broken</td>
								<td>{vo(stats.bedwars.beds_broken)}</td>
							</tr>
							<tr>
								<td>Beds Lost</td>
								<td>{vo(stats.bedwars.beds_lost)}</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
			<div class="uk-width-1-4@l uk-width-1-2@s">
				<div class="uk-overflow-auto">
					<table class="uk-table uk-table-small uk-table-divider">
						<tbody>
							<tr>
								<td>Wins</td>
								<td>{vo(stats.bedwars.wins)}</td>
							</tr>
							<tr>
								<td>Losses</td>
								<td>{vo(stats.bedwars.losses)}</td>
							</tr>
							<tr>
								<td>W/L</td>
								<td><b>{vo(Math.round(stats.bedwars.wl_ratio * 100) / 100)}</b>
									<span class="uk-margin-small-right pointer-cursor"
									      uk-icon="info"
									      uk-tooltip={vo(stats.bedwars.wl_ratio)}></span></td>
							</tr>
							<tr>
								<td>Winstreak</td>
								<td>{vo(stats.bedwars.winstreak)}</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
			<div class="uk-width-1-4@l uk-width-1-2@s">
				<div>
					<table class="uk-table uk-table-small uk-table-divider">
						<tbody>
							<tr>
								<td>Kills</td>
								<td>{vo(stats.bedwars.kills)}</td>
							</tr>
							<tr>
								<td>Deaths</td>
								<td>{vo(stats.bedwars.deaths)}</td>
							</tr>
							<tr>
								<td>K/D</td>
								<td><b>{vo(Math.round(stats.bedwars.kd_ratio * 100) / 100)}</b>
									<span class="uk-margin-small-right pointer-cursor"
									      uk-icon="info"
									      uk-tooltip={vo(stats.bedwars.kd_ratio)}></span></td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
			<div class="uk-width-1-4@l uk-width-1-2@s">
				<div>
					<table class="uk-table uk-table-small uk-table-divider">
						<tbody>
							<tr>
								<td>Final Kills</td>
								<td>{vo(stats.bedwars.final_kills)}</td>
							</tr>
							<tr>
								<td>Final Deaths</td>
								<td>{vo(stats.bedwars.final_deaths)}</td>
							</tr>
							<tr>
								<td>Final K/D</td>
								<td><b>{vo(Math.round(stats.bedwars.final_kd_ratio * 100) /
									100)}</b>
									<span class="uk-margin-small-right pointer-cursor"
									      uk-icon="info"
									      uk-tooltip={vo(stats.bedwars.final_kd_ratio)}></span></td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
		<ul uk-accordion>
			<li>
				<a class="uk-accordion-title" href="#">More stats</a>
				<div class="uk-accordion-content">
					<div uk-grid>
						<div class="uk-width-1-4@l uk-width-1-2@s">
							<table class="uk-table uk-table-small uk-table-divider">
								<tbody>
									<tr>
										<td>Resources Collected</td>
										<td>{vo(stats.bedwars.resources_collected)}</td>
									</tr>
									<tr>
										<td>Iron Collected</td>
										<td>{vo(stats.bedwars.iron_collected)}</td>
									</tr>
									<tr>
										<td>Gold Collected</td>
										<td>{vo(stats.bedwars.gold_collected)}</td>
									</tr>
									<tr>
										<td>Diamonds Collected</td>
										<td>{vo(stats.bedwars.diamonds_collected)}</td>
									</tr>
									<tr>
										<td>Emeralds Collected</td>
										<td>{vo(stats.bedwars.emeralds_collected)}</td>
									</tr>
									<tr>
										<td>Items purchased</td>
										<td>{vo(stats.bedwars.items_purchased)}</td>
									</tr>
								</tbody>
							</table>
						</div>
						<div class="uk-width-3-4@l uk-width-1-2@s">
							<p class="uk-text-center">
								Do you think anything's missing? <a href="../../contact/">Let me
								know</a> and I'll add it!
							</p>
						</div>
					</div>
				</div>
			</li>
		</ul>
	{:else}
		<p class="uk-text-center uk-margin-medium">
			Nothing here yet. Search for a player to show their stats here.
		</p>
	{/if}
</div>