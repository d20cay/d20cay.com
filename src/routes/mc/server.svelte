<script>
	import {currentPage, Pages} from "../../stores";

	currentPage.set(Pages.SERVER);
</script>

<svelte:head>
	<title>d20cay | MC Servers</title>
</svelte:head>

<h1 class="uk-text-center">
	Minecraft Servers
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Some server configs and other stuff I'd like to remember.
		</p>
	</div>
</div>

<div uk-grid>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Servers</h3>
			<table class="uk-table uk-table-hover table-small">
				<thead>
					<tr>
						<th>Version</th>
						<th>Type</th>
						<th>Mods</th>
						<th>Configs</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>
							1.16.1
						</td>
						<td>
							<a href="https://fabricmc.net/use/">Fabric</a>
						</td>
						<td>
							Fabric API (<a
								href="https://www.curseforge.com/minecraft/mc-mods/fabric-api/files">Download</a>)<br>
							Carpet (<a href="https://www.curseforge.com/minecraft/mc-mods/carpet/files">Download</a>,
							<a href="https://github.com/gnembon/fabric-carpet">GitHub</a>)<br>
							Lithium (<a
								href="https://www.curseforge.com/minecraft/mc-mods/lithium/files">Download</a>,
							<a href="https://github.com/jellysquid3/lithium-fabric">GitHub</a>)
						</td>
						<td>Carpet <a href="resources/mc/server/config/1_16_1/carpet.conf"
						              class="uk-icon-button uk-margin-small-right"
						              uk-icon="download" download></a></td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
	<div class="uk-width-1-2@l">
	</div>
</div>