<script>
	import {currentPage, Page} from "../../stores";

	currentPage.set(Page.MC_COMMAND);
</script>

<svelte:head>
	<title>d20cay | MC Commands</title>
</svelte:head>

<h1 class="uk-text-center">
	Minecraft Command Cheatsheet
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Some important commands for servers I run that I should remember.
		</p>
	</div>
</div>
<div uk-grid>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Ultimate AutoRestart</h3>
			<a href="https://www.spigotmc.org/resources/1-8-1-15-ultimateautorestart-need-an-autorestart-plugin-grab-the-best-one-today.64414/?__cf_chl_jschl_tk__=9a9d2ee786dbe277aea3072467b06875fe2eeb75-1590831480-0-AWEy9zH9GMlLvmKkfK4wm-i8-8zHoqJsGa4THB31zv3CP1iaxN39w3UFZfunh_xDr-k_fK-4N79WaIHAL5WiPpkEBIx-eiF0FX3NVUMc64fLAkmZif1Xdea8ubZg0opDtJOVNCKd75vDd7Yw0BRv1V9U6AYlz9oNmYxGkixe8GxvnhUQEMz1Evs_rAZ9q2OiUB1GIIhHeWk-HFGKVNQo-HmOqFVaf6ewP5qGpi4yBlXNr0Z6ZcX6SxnCELVOqTH1DElkfBiVb4mbrQqf3sLq_eoxCpnOiPewGRBmsBYBM4ekBt0yxLKk2p-2IkwK5jIKEMQ0hpOc3s4Uodh0QuEIXxa4C-dzHjcl1cw9OlBCaRzWXRchEBGq4og55p7NBMKDWnjUicqfH1HWAuOKoW8eP8g">Spigot
				page</a>
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover table-small">
					<thead>
						<tr>
							<th class="uk-table-expand">Action</th>
							<th class="uk-table-shrink">Command</th>
							<th class="uk-table-shrink">Example</th>
							<th class="uk-table-shrink">Role</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>
								Restart server in specified amount of seconds
							</td>
							<td>
								<code>
									/autorestart now [interval]
								</code>
							</td>
							<td>
								<code uk-tooltip="Restarts server in 120 seconds">
									/autorestart now 120
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>
								Prevent scheduled autorestart
							</td>
							<td>
								<code>
									/autorestart stop
								</code>
							</td>
							<td>
								<code uk-tooltip="Prevents scheduled autorestart">
									/autorestart stop
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>
								Show time left until next restart
							</td>
							<td>
								<code>
									/autorestart time
								</code>
							</td>
							<td>
								<code uk-tooltip="Shows time left until next restart">
									/autorestart time
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>
								Show time left until next restart
							</td>
							<td>
								<code>
									/autorestart
								</code>
							</td>
							<td>
								<code uk-tooltip="Shows time left until next restart">
									/autorestart
								</code>
							</td>
							<td><code>User</code></td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">CraftyController</h3>
			<a href="https://craftycontrol.com/">Site</a>
			<h4>CLI Commands</h4>
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover table-small">
					<thead>
						<tr>
							<th class="uk-table-expand">Description</th>
							<th class="uk-table-shrink">Command</th>
							<th class="uk-table-shrink">Example</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>
								Change web port
							</td>
							<td>
								<code>
									change_web_port [port]
								</code>
							</td>
							<td>
								<code uk-tooltip="Changes web port to 8001">
									change_web_port 8001
								</code>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">CoreProtect</h3>
			<a href="https://www.spigotmc.org/resources/coreprotect.8631/">Spigot page</a><br>
			<a href="https://www.minerealm.com/community/viewtopic.php?f=32&t=6781">External command
				overview</a>
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover table-small">
					<thead>
						<tr>
							<th class="uk-table-expand">Action</th>
							<th class="uk-table-shrink">Command</th>
							<th class="uk-table-shrink">Example</th>
							<th class="uk-table-shrink">Role</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>Display help information</td>
							<td><code>/co help</code></td>
							<td>
								<code uk-tooltip="Displays help information">
									/co help
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>Toggle inspector</td>
							<td><code>/co inspect</code></td>
							<td>
								<code uk-tooltip="Toggles inspector">
									/co inspect
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>Lookup changes</td>
							<td><code>/co l [parameters]</code></td>
							<td>
								<code uk-tooltip="Looks up changes by d20cay in the last 5 minutes">
									/co l u:d20cay t:5m
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>Rollback changes</td>
							<td><code>/co rollback [parameters]</code></td>
							<td>
								<code uk-tooltip="Rolls back changes by d20cay from the last 5 minutes in a 50 block radius">
									/co rollback u:d20cay t:5m r:50
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
						<tr>
							<td>Undo rollback</td>
							<td><code>/co undo</code></td>
							<td>
								<code uk-tooltip="Undoes last rollback">
									/co undo
								</code>
							</td>
							<td><code>Admin</code></td>
						</tr>
					</tbody>
				</table>
			</div>

			<h4>Parameters</h4>
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover table-small">
					<thead>
						<tr>
							<th class="uk-table-expand">Parameter</th>
							<th class="uk-table-shrink">label</th>
							<th>Options</th>
							<th class="uk-table-shrink">Example</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>Username</td>
							<td><code>u:</code></td>
							<td>Any username</td>
							<td><code>u:d20cay</code></td>
						</tr>
						<tr>
							<td>Time</td>
							<td><code>t:</code></td>
							<td>
								<code>[x]w</code>, <code>[x]d</code>, <code>[x]h</code>,
								<code>[x]m</code>,
								<code>[x]s</code>
							</td>
							<td><code>t:1w2d3h4m5s</code></td>
						</tr>
						<tr>
							<td>Radius</td>
							<td><code>r:</code></td>
							<td>Any positive integer</td>
							<td><code>r:50</code></td>
						</tr>
						<tr>
							<td>Action</td>
							<td><code>a:</code></td>
							<td>One of the actions listed below</td>
							<td><code>a:kill</code></td>
						</tr>
						<tr>
							<td>Block</td>
							<td><code>b:</code></td>
							<td>
								<a href="https://minecraft-ids.grahamedgecombe.com/">Block id</a> of
								the blocks
								that should be rolled back
							</td>
							<td><code>b:1</code></td>
						</tr>
						<tr>
							<td>Exclude</td>
							<td><code>e:</code></td>
							<td>
								<a href="https://minecraft-ids.grahamedgecombe.com/">Block id</a> of
								the blocks
								that should <i>not</i> be rolled back
							</td>
							<td><code>e:1,1:2</code></td>
						</tr>
						<tr>
							<td>Additional actions</td>
							<td><code>#</code></td>
							<td>
								<code>preview</code>, <code>count </code>, <code>verbose</code>,
								<code>silent</code>
							</td>
							<td><code>#preview</code></td>
						</tr>
					</tbody>
				</table>
			</div>

			<h5>Actions</h5>
			<div class="uk-overflow-auto">
				<table class="uk-table uk-table-hover table-small">
					<thead>
						<tr>
							<th class="uk-table-expand">Description</th>
							<th class="uk-table-shrink">Action</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>Block placed/broken</td>
							<td><code>block</code></td>
						</tr>
						<tr>
							<td>Block placed</td>
							<td><code>+block</code></td>
						</tr>
						<tr>
							<td>Block broken</td>
							<td><code>-block</code></td>
						</tr>
						<tr>
							<td>Player interaction</td>
							<td><code>click</code></td>
						</tr>
						<tr>
							<td>Items added or removed from chest or other container</td>
							<td><code>container</code></td>
						</tr>
						<tr>
							<td>Items added to chests or other containers</td>
							<td><code>+container</code></td>
						</tr>
						<tr>
							<td>Items removed from chests or other containers</td>
							<td><code>-container</code></td>
						</tr>
						<tr>
							<td>Mobs killed</td>
							<td><code>kill</code></td>
						</tr>
						<tr>
							<td>Message sent in chat</td>
							<td><code>chat</code></td>
						</tr>
						<tr>
							<td>Commands performed</td>
							<td><code>command</code></td>
						</tr>
						<tr>
							<td>Player login/logout</td>
							<td><code>session</code></td>
						</tr>
						<tr>
							<td>Player login</td>
							<td><code>+session</code></td>
						</tr>
						<tr>
							<td>Player logout</td>
							<td><code>-session</code></td>
						</tr>
						<tr>
							<td>Username changes</td>
							<td><code>username</code></td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</div>