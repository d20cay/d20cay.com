<script>
	import {Page} from "../stores";

	export let currentPage;
</script>

<div uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky"
     class="uk-visible@m">
	<nav class="uk-navbar-container uk-margin" uk-navbar>
		<div class="uk-navbar-left">
			<a class="uk-navbar-item uk-logo" href="/">
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
							<li class:uk-active={currentPage === Page.CS_PROGRAMS}>
								<a href="cheatsheet/programs/">Programs</a></li>
							<li class:uk-active={currentPage === Page.CS_LINUX}>
								<a href="cheatsheet/linux/">Linux (Ubuntu)</a></li>
							<li class:uk-active={currentPage === Page.CS_SCHOOL}>
								<a href="cheatsheet/school/">School</a></li>
							<li class:uk-active={currentPage === Page.ASCII}>
								<a href="cheatsheet/ascii/">Ascii Table</a></li>
						</ul>
					</div>
				</li>
				<li>
					<a href="#">Minecraft <span uk-icon="chevron-down"></span></a>
					<div class="uk-navbar-dropdown uk-width-auto">
						<ul class="uk-nav uk-navbar-dropdown-nav">
							<li class:uk-active={currentPage === Page.MC_COMMAND}>
								<a href="mc/command/">Minecraft Commands</a></li>
							<li class:uk-active={currentPage === Page.MC_SERVER}>
								<a href="mc/server/">Minecraft Servers</a></li>
							<li class:uk-active={currentPage === Page.HY_STATS}>
								<a href="mc/hy_stats/">Hypixel Bedwars Stats</a></li>
						</ul>
					</div>
				</li>
				<li>
					<a href="#">Projects <span uk-icon="chevron-down"></span></a>
					<div class="uk-navbar-dropdown uk-width-auto">
						<ul class="uk-nav uk-navbar-dropdown-nav">
							<li class:uk-active={currentPage === Page.UMLAUT}>
								<a href="project/umlaut/">Umlaut</a></li>
							<li class:uk-active={currentPage === Page.CRYPTO}>
								<a href="project/crypto/">Cryptography</a></li>
							<li class:uk-active={currentPage === Page.PI}>
								<a href="project/pi/">Pi</a></li>
							<li class:uk-active={currentPage === Page.PRIME_FACT}>
								<a href="project/prime_factorization/">Prime Factorization</a></li>
							<li class:uk-active={currentPage === Page.SUDOKU}>
								<a href="project/sudoku/">Sudoku</a></li>
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
				<li class:uk-active={currentPage === Page.CONTACT}><a href="contact/"><span
						class="uk-margin-small-right"
						uk-icon="icon: mail"></span>Contact
					me</a></li>
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
			<a class="uk-navbar-item uk-logo" href="/">
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
							<li class:uk-active={currentPage === Page.CS_PROGRAMS}>
								<a href="cheatsheet/programs/">Programs</a></li>
							<li class:uk-active={currentPage === Page.CS_LINUX}>
								<a href="cheatsheet/linux/">Linux (Ubuntu)</a></li>
							<li class:uk-active={currentPage === Page.CS_SCHOOL}>
								<a href="cheatsheet/school/">School</a></li>
							<li class:uk-active={currentPage === Page.ASCII}>
								<a href="cheatsheet/ascii/">Ascii Table</a></li>
						</ul>
					</li>
					<li class="uk-parent">
						<a>Minecraft</a>
						<ul class="uk-nav-sub">
							<li class:uk-active={currentPage === Page.MC_COMMAND}>
								<a href="mc/command/">Minecraft Commands</a></li>
							<li class:uk-active={currentPage === Page.MC_SERVER}>
								<a href="mc/server/">Minecraft Servers</a></li>
							<li class:uk-active={currentPage === Page.HY_STATS}>
								<a href="mc/hy_stats/">Hypixel Bedwars Stats</a></li>
						</ul>
					</li>
					<li class="uk-parent">
						<a>Projects</a>
						<ul class="uk-nav-sub">
							<li class:uk-active={currentPage === Page.UMLAUT}>
								<a href="project/umlaut/">Umlaut</a></li>
							<li class:uk-active={currentPage === Page.CRYPTO}>
								<a href="project/crypto/">Cryptography</a></li>
						</ul>
					</li>
					<li>
						<a href="https://gallifreyan.info/">Gallifreyan</a>
					</li>
					<li class="uk-nav-divider"></li>
					<li class:uk-active={currentPage === Page.CONTACT}>
						<a href="contact/"><span class="uk-margin-small-right"
						                         uk-icon="icon: mail"></span>Contact
							me</a></li>
				</ul>
			</div>
		</div>
	</nav>
</div>