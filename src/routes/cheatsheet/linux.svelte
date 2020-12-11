<script>
	import {currentPage, Page} from "../../stores";

	currentPage.set(Page.CS_LINUX);
</script>

<svelte:head>
	<title>d20cay | Linux Cheatsheet</title>
</svelte:head>

<h1 class="uk-text-center">
	Linux commands
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Some important commands that I keep forgetting.
		</p>
	</div>
</div>

<div uk-grid>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Uncomplicated Firewall</h3>
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover table-small">
					<thead>
						<tr>
							<th class="uk-table-expand">Description</th>
							<th class="uk-table-shrink">Command</th>
							<th class="uk-table-shrink">Example</th>
							<th class="uk-table-shrink">Requires root</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>List ports</td>
							<td><code>ufw status</code></td>
							<td><code uk-tooltip="Lists ufw status">ufw status</code></td>
							<td>Yes</td>
						</tr>
						<tr>
							<td>Enable firewall</td>
							<td><code>ufw enable</code></td>
							<td><code uk-tooltip="Enables the firewall">ufw enable</code></td>
							<td>Yes</td>
						</tr>
						<tr>
							<td>Disable firewall</td>
							<td><code>ufw disable</code></td>
							<td><code uk-tooltip="Disables the firewall">ufw disable</code></td>
							<td>Yes</td>
						</tr>
						<tr>
							<td>Open ports</td>
							<td><code>ufw allow [port]</code></td>
							<td>
								<code uk-tooltip="Allows requests through the port 3292">ufw allow 3292</code>
							</td>
							<td>Yes</td>
						</tr>
						<tr>
							<td>Close ports</td>
							<td><code>ufw deny [port]</code></td>
							<td><code uk-tooltip="Denies requests through the port 3292">ufw deny 3292</code>
							</td>
							<td>Yes</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Process Management</h3>
			<h4>Kill process blocking port</h4>
			<code>netstat -tupal | grep -i [port]</code>
			<code>sudo kill -15 [process_id]</code>
		</div>
	</div>
</div>