<script>
    import {onMount} from 'svelte';
    import {currentPage, ProjectPages} from "../../../stores";
    import {
	    NotificationPosition,
	    NotificationStatus,
	    NotificationTimeout,
	    notify
    } from "../../../global";
    import {AccentChar, GreekChar, UmlautChar} from "./character-helper";

    currentPage.set(ProjectPages.UMLAUT);

    const ReferrerMap = new Map([
        ['ae', UmlautChar.AE.LOWERCASE],
        ['oe', UmlautChar.OE.LOWERCASE],
        ['ue', UmlautChar.UE.LOWERCASE]
    ]);

    onMount(() => {
        const urlParams = window.location.search;
        const params = new URLSearchParams(urlParams);
        const char = ReferrerMap.get(params.get('referrer'));
        if (char) {
            overwriteClipboard(char);
        }
    });

    export function overwriteClipboard(string) {
	    const el = document.createElement('textarea');
	    el.setAttribute("class", "copy-text-holder");
	    el.value = string;

	    document.body.appendChild(el);
	    el.select();
	    document.execCommand('copy');
	    document.body.removeChild(el);

	    notify(`Copied "${string}" to clipboard.`,
			    NotificationStatus.SUCCESS,
			    NotificationPosition.BOTTOM_LEFT,
			    NotificationTimeout.FLASH);
    }
</script>

<style>
    .copy-text-holder {
        visibility: hidden;
    }
</style>

<svelte:head>
	<title>d20cay | Umlaut Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Special Characters
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			Some special characters I don't have on my keyboard but need occasionally.
		</p>
	</div>
</div>

<div uk-grid>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">German Umlauts</h3>
			<div uk-grid>
				{#each Object.entries(UmlautChar) as [key, value]}
					<div class="uk-width-1-3">
						<h4 class="uk-text-center">{value.UPPERCASE} {value.LOWERCASE}</h4>
						<div class="uk-flex uk-flex-center">
							<button on:click={() => overwriteClipboard(value.UPPERCASE)}
							        uk-icon="arrow-up"
							        uk-tooltip="Copy uppercase"
							        class="uk-icon-button uk-margin-small-right">
							</button>
							<button on:click={() => overwriteClipboard(value.LOWERCASE)}
							        uk-icon="arrow-down"
							        uk-tooltip="Copy Lowercase"
							        class="uk-icon-button uk-margin-small-right">
							</button>
						</div>
					</div>
				{/each}
			</div>
		</div>
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">French Accent's</h3>
			<div uk-grid>
				{#each Object.entries(AccentChar) as [key, value]}
					<div class="uk-width-1-3">
						<h4 class="uk-text-center">{value.UPPERCASE} {value.LOWERCASE}</h4>
						<div class="uk-flex uk-flex-center">
							<button on:click={() => overwriteClipboard(value.UPPERCASE)}
							        uk-icon="arrow-up"
							        uk-tooltip="Copy uppercase"
							        class="uk-icon-button uk-margin-small-right">
							</button>
							<button on:click={() => overwriteClipboard(value.LOWERCASE)}
							        uk-icon="arrow-down"
							        uk-tooltip="Copy Lowercase"
							        class="uk-icon-button uk-margin-small-right">
							</button>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
	<div class="uk-width-1-2@l">
		<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
			<h3 class="uk-card-title">Greek Alphabet</h3>
			<div uk-grid>
				{#each Object.entries(GreekChar) as [key, value]}
					<div class="uk-width-1-6@l uk-width-1-5@m uk-width-1-4@s uk-width-1-3">
						<h4 class="uk-text-center">{value.UPPERCASE} {value.LOWERCASE}</h4>
						<div class="uk-flex uk-flex-center">
							<button on:click={() => overwriteClipboard(value.UPPERCASE)}
							        uk-icon="arrow-up"
							        uk-tooltip="Copy uppercase"
							        class="uk-icon-button uk-margin-small-right">
							</button>
							<button on:click={() => overwriteClipboard(value.LOWERCASE)}
							        uk-icon="arrow-down"
							        uk-tooltip="Copy Lowercase"
							        class="uk-icon-button uk-margin-small-right">
							</button>
							{#if value.ALT}
								<button on:click={() => overwriteClipboard(value.ALT)}
								        uk-icon="star"
								        uk-tooltip="Copy Alt"
								        class="uk-icon-button uk-margin-small-right">
								</button>
							{/if}
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>