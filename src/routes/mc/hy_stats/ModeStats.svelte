<script>
	import {LoadingStatus} from "../../../global";

	export let stats;
	export let loadingStatus;
	export let expectedError;
	export let isolatedUsername;
	export let mode;

	function vo(value) {
		return value ? value : 'NaN';
	}

	function ratio(positive, negative) {
		if (negative === 0 && positive === 0) {
			return 0;
		} else if (negative === 0) {
			return 'infinity'
		}
		return positive / negative;
	}

	function roundedRatio(positive, negative) {
		if (negative === 0 && positive === 0) {
			return 0;
		} else if (negative === 0) {
			return '&infin;'
		}
		return Math.round(positive / negative * 100) / 100;
	}
</script>

<style>
    /** Changes the mouse cursor into a point (hand) when hovering over objects with this class. */
    .pointer-cursor:hover {
        cursor: pointer;
    }
</style>



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
							<td>{vo(stats.bedwars[mode].wl.wins +
								stats.bedwars[mode].wl.losses)}</td>
						</tr>
						<tr>
							<td>Beds Broken</td>
							<td>{vo(stats.bedwars[mode].bbbl.beds_broken)}</td>
						</tr>
						<tr>
							<td>Beds Lost</td>
							<td>{vo(stats.bedwars[mode].bbbl.beds_lost)}</td>
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
							<td>{vo(stats.bedwars[mode].wl.wins)}</td>
						</tr>
						<tr>
							<td>Losses</td>
							<td>{vo(stats.bedwars[mode].wl.losses)}</td>
						</tr>
						<tr>
							<td>W/L</td>
							<td><b>{@html roundedRatio(stats.bedwars[mode].wl.wins,
								stats.bedwars[mode].wl.losses)}</b>
								<span class="uk-margin-small-right pointer-cursor"
								      uk-icon="info"
								      uk-tooltip={ratio(stats.bedwars[mode].wl.wins, stats.bedwars[mode].wl.losses)}></span>
							</td>
						</tr>
						<tr>
							<td>Winstreak</td>
							<td>{vo(stats.bedwars.ws[mode])}</td>
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
							<td>{vo(stats.bedwars[mode].kd.kills)}</td>
						</tr>
						<tr>
							<td>Deaths</td>
							<td>{vo(stats.bedwars[mode].kd.deaths)}</td>
						</tr>
						<tr>
							<td>K/D</td>
							<td><b>{@html roundedRatio(stats.bedwars[mode].kd.kills,
								stats.bedwars[mode].kd.deaths)}</b>
								<span class="uk-margin-small-right pointer-cursor"
								      uk-icon="info"
								      uk-tooltip={ratio(stats.bedwars[mode].kd.kills, stats.bedwars[mode].kd.deaths)}></span>
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
							<td>{vo(stats.bedwars[mode].fkd.final_kills)}</td>
						</tr>
						<tr>
							<td>Final Deaths</td>
							<td>{vo(stats.bedwars[mode].fkd.final_deaths)}</td>
						</tr>
						<tr>
							<td>Final K/D</td>
							<td><b>{@html roundedRatio(stats.bedwars[mode].fkd.final_kills,
								stats.bedwars[mode].fkd.final_deaths)}</b>
								<span class="uk-margin-small-right pointer-cursor"
								      uk-icon="info"
								      uk-tooltip={ratio(stats.bedwars[mode].fkd.final_kills, stats.bedwars[mode].fkd.final_deaths)}></span>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>