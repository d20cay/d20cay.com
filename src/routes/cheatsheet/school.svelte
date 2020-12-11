<script>
	import {currentPage, Page} from "../../stores";

	currentPage.set(Page.CS_SCHOOL);
</script>

<svelte:head>
	<title>d20cay | School Cheatsheets</title>
</svelte:head>

<h1 class="uk-text-center">
	School
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Cheatsheets to some of the topics where I felt like making one. Some of the information may be
			wrong or useless to you and if you'd like to improve some of the documents by
			<a href="../../contact/">shooting me a message</a> I would greatly appreciate that.
		</p>
		<p>
			I write most of my cheatsheets in <a href="https://typora.io/">Typora</a>, just to make my life
			easy and so I don't have to write LaTeX and I can just smack down some formulas. If you download
			the Markdown files I would recommend to open them in <a href="https://typora.io/">Typora</a> or
			some other markdown editor that supports MathJax, since that's what <a
				href="https://typora.io/">Typora</a> uses.
		</p>
		<div class="uk-alert-danger" uk-alert>
			Here goes the typical disclaimer I feel like I have to make: I am in no way liable for anything
			that may occur to you or anyone else because you read the information in the cheatsheets linked
			on this page.
		</div>
	</div>
</div>
<div class="uk-child-width-1-3@m" uk-grid>
	<div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Math</h3>
			<p>
				Bear in mind that this is translated from German, so some of the terms might not be correct.
			</p>
			<a href="resources/cheatsheets/school/math/math_cheatsheet.pdf"
			   class="uk-icon-button uk-margin-small-right"
			   uk-icon="file-pdf"></a>
			<a href="resources/cheatsheets/school/math/math_cheatsheet.md"
			   class="uk-icon-button uk-margin-small-right"
			   uk-icon="file-text" uk-tooltip="Markdown file" download></a>
		</div>
	</div>
	<div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Physics</h3>
			<p>
				This is written in German and I can't be bothered to translate it myself.
			</p>
			<a href="resources/cheatsheets/school/physics/physics_cheatsheet.pdf"
			   class="uk-icon-button uk-margin-small-right"
			   uk-icon="file-pdf"></a>
			<a href="resources/cheatsheets/school/physics/physics_cheatsheet.md"
			   class="uk-icon-button uk-margin-small-right"
			   uk-icon="file-text" uk-tooltip="Markdown file" download></a>
		</div>
	</div>
	<div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">BPMN</h3>
			<p>
				Bear in mind that this is translated from German, so some of the terms might not be correct.
			</p>
			<a href="resources/cheatsheets/school/bpmn/bpmn_summary.pdf"
			   class="uk-icon-button uk-margin-small-right"
			   uk-icon="file-pdf"></a>
			<a href="resources/cheatsheets/school/bpmn/bpmn_summary.md"
			   class="uk-icon-button uk-margin-small-right"
			   uk-icon="file-text" uk-tooltip="Markdown file" download></a>
		</div>
	</div>
</div>