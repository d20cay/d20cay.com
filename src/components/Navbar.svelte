<script>
    import {CheatsheetPages, LabelMap, MinecraftPages, Pages, ProjectPages, UriMap} from "../stores";

    export let currentPage;
</script>

<div uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky"
     class="uk-visible@m">
	<nav class="uk-navbar-container uk-margin" uk-navbar>
		<div class="uk-navbar-left">
			<a class="uk-navbar-item uk-logo" href={UriMap.get(Pages.HOME)}>
				<img data-src="img/d20cay_logo_square.png"
				     height="70"
				     width="70"
				     alt="d20cay logo"
				     uk-img>
			</a>

			<ul class="uk-navbar-nav">
				<li>
					<a href="#">Cheatsheets <span uk-icon="chevron-down"></span></a>
					<div class="uk-navbar-dropdown uk-width-auto">
						<ul class="uk-nav uk-navbar-dropdown-nav">
							{#each Object.entries(CheatsheetPages) as [_, p]}
								<li class:uk-active={currentPage === p}>
									<a href={UriMap.get(p)}>{LabelMap.get(p)}</a>
								</li>
							{/each}
						</ul>
					</div>
				</li>
				<li>
					<a href="#">Minecraft <span uk-icon="chevron-down"></span></a>
					<div class="uk-navbar-dropdown uk-width-auto">
						<ul class="uk-nav uk-navbar-dropdown-nav">
							{#each Object.entries(MinecraftPages) as [_, p]}
								<li class:uk-active={currentPage === p}>
									<a href={UriMap.get(p)}>{LabelMap.get(p)}</a>
								</li>
							{/each}
						</ul>
					</div>
				</li>
				<li>
					<a href="#">Projects <span uk-icon="chevron-down"></span></a>
					<div class="uk-navbar-dropdown uk-width-auto">
						<ul class="uk-nav uk-navbar-dropdown-nav">
							{#each Object.entries(ProjectPages) as [_, p]}
								<li class:uk-active={currentPage === p}>
									<a href={UriMap.get(p)}>{LabelMap.get(p)}</a>
								</li>
							{/each}
						</ul>
					</div>
				</li>
				<li>
					<a href="https://gallifreyan.info/">Gallifreyan</a>
				</li>
			</ul>
		</div>
		<div class="uk-navbar-right">
			<ul class="uk-navbar-nav">
				<li class:uk-active={currentPage === Pages.CONTACT}>
					<a href={UriMap.get(Pages.CONTACT)}>
						<span class="uk-margin-small-right"
						      uk-icon="icon: mail"></span>
						Contact me
					</a>
				</li>
			</ul>
		</div>
	</nav>
</div>

<div uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky" class="uk-hidden@m">
	<nav class="uk-navbar-container uk-margin" uk-navbar>
		<div class="uk-navbar-left">
			<button uk-toggle="target: #sidenav;"
			        class="uk-button uk-button-text uk-navbar-toggle"
			        type="button">
				<span uk-navbar-toggle-icon></span> <span class="uk-margin-small-left">Menu</span>
			</button>
		</div>
		<div class="uk-navbar-center">
			<a class="uk-navbar-item uk-logo" href={UriMap.get(Pages.HOME)}>
				<img data-src="img/d20cay_logo_square.png"
				     height="70"
				     width="70"
				     alt="d20cay logo"
				     uk-img></a>
		</div>
		<div id="sidenav" uk-offcanvas="overlay: true">
			<div class="uk-offcanvas-bar uk-flex uk-flex-column">
				<button class="uk-offcanvas-close" type="button" uk-close></button>

				<ul class="uk-nav uk-nav-primary uk-nav-center uk-margin-auto-vertical">
					<li class="uk-parent">
						<a>Cheatsheets</a>
						<ul class="uk-nav-sub">
							{#each Object.entries(CheatsheetPages) as [_, p]}
								<li class:uk-active={currentPage === p}>
									<a href={UriMap.get(p)}>{LabelMap.get(p)}</a>
								</li>
							{/each}
						</ul>
					</li>
					<li class="uk-parent">
						<a>Minecraft</a>
						<ul class="uk-nav-sub">
							{#each Object.entries(MinecraftPages) as [_, p]}
								<li class:uk-active={currentPage === p}>
									<a href={UriMap.get(p)}>{LabelMap.get(p)}</a>
								</li>
							{/each}
						</ul>
					</li>
					<li class="uk-parent">
						<a>Projects</a>
						<ul class="uk-nav-sub">
							{#each Object.entries(ProjectPages) as [_, p]}
								<li class:uk-active={currentPage === p}>
									<a href={UriMap.get(p)}>{LabelMap.get(p)}</a>
								</li>
							{/each}
						</ul>
					</li>
					<li>
						<a href="https://gallifreyan.info/">Gallifreyan</a>
					</li>
					<li class="uk-nav-divider"></li>
					<li class:uk-active={currentPage === Pages.CONTACT}>
						<a href={UriMap.get(Pages.CONTACT)}>
							<span class="uk-margin-small-right"
							      uk-icon="icon: mail"></span>
							Contact me
						</a>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</div>