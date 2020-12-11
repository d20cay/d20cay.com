<script>
	import {currentPage, Page} from "../stores";

	currentPage.set(Page.HOME);
</script>

<svelte:head>
	<title>d20cay</title>
</svelte:head>

<h1 class="uk-text-center">
	d20cay
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Hi there,<br>
			I'm d20cay, pronounced "decay", and I do stuff. You'll find stuff below.
		</p>
	</div>
</div>

<div uk-grid>
	<div class="uk-width-1-3@m uk-width-1-2@s">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Cheatsheets</h3>
			<p>
				I'm a software engineer so I like to do a lot of stuff with keyboard shortcuts and while I
				learn them I like to write them down in case I forget them at a later date.
			</p>
			<a href="cheatsheet/programs/">Programs</a><br>
			<a href="cheatsheet/linux/">Linux (Ubuntu)</a><br>
			<a href="cheatsheet/school/">School</a><br>
			<a href="cheatsheet/ascii/">Ascii Table</a>
		</div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Projects</h3>
			<p>
				Some small projects I did for fun
			</p>
			<a href="project/umlaut/">Umlaut</a><br>
			<a href="project/crypto/">Cryptography</a>
		</div>
	</div>
	<div class="uk-width-1-3@m uk-width-1-2@s">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Gallifreyan</h3>
			<p>
				I'm a big fan of the BBC show Doctor Who, which introduced me to the world of Gallifreyan.
				Gallifreyan is the language the so-called timelords use. The language is actually not
				created by the BBC but by the Doctor Who community. Read more about it at
				<a href="https://gallifreyan.info/">gallifreyan.info</a>.
			</p>
		</div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Minecraft</h3>
			<p>
				The only game I really play consistently is Minecraft. I have tried other games but I always
				seem to come back to it. Because I can, I also administrate all of my servers myself but
				sometimes it's hard to keep track of all the setup I do for them so this page serves as
				reminder for me of what's around if I forget and it might come in handy for someone else as
				well.
			</p>
			<a href="mc/command/">Server Commands</a><br>
			<a href="mc/server/">Server Overview</a><br>
			<a href="mc/hy_stats/">Hypixel Bedwars Stats</a>
		</div>
	</div>
	<div class="uk-width-1-3@m uk-width-1-2@s">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Social Media</h3>
			<a href="https://www.youtube.com/channel/UCbFegF_v_6ywmP6EOkdnFIA"
			   class="uk-icon-button  uk-margin-small-right" uk-icon="youtube"></a>
			<a href="https://www.reddit.com/user/d20cay" class="uk-icon-button  uk-margin-small-right"
			   uk-icon="reddit"></a>
			<a href="https://twitter.com/d20cay" class="uk-icon-button  uk-margin-small-right"
			   uk-icon="twitter"></a>
			<h4>One of my videos</h4>
			<iframe height="100%" src="https://www.youtube.com/embed/5kVhs0jq6UI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
		</div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Contact d20cay</h3>
			<p>
				Have any questions or feel like chatting? <a href="contact/">Shoot me a message</a>.
			</p>
		</div>
	</div>
</div>