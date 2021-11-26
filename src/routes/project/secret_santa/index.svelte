<script>
    import {currentPage, ProjectPages} from "../../../stores";

    currentPage.set(ProjectPages.SECRET_SANTA);

    let names = ["", ""];

    function adminRun() {
        // TODO(d20cay): Add functionality.
    }

    function participantRun() {
        // TODO(d20cay): Add functionality.
    }

    function updateNamesArray() {
        if (names.filter(n => n === "").length === 0) {
            names = [...names, ""];
        }
    }

    function nameValid(name) {
        return names.includes(name);
    }

    function namesValid() {
        return names.map(n => nameValid(n)).filter(v => v).length > 0;
    }
</script>

<svelte:head>
	<title>d20cay | Secret Santa Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Secret Santa
</h1>

<p class="uk-text-center">
	Some secret santa utilities to pair people for the secret santa activity. You can either run it in admin mode, which
	will let you see who is paired to who, or in participant mode, where you don't get to see all matches so you can
	participate yourself.
</p>


<div uk-grid>
	{#each names as name, i}
		<div class="uk-width-auto">
			<label for={`name-${i}-input`} class="uk-form-label">
				Name
			</label>
			<input id="input-input"
			       type="text"
			       bind:value={names[i]}
			       on:keydown={updateNamesArray}
			       placeholder="Jimmy"
			       class="uk-input uk-border-rounded"
			       class:uk-form-danger={!nameValid(names[i])}
			       uk-tooltip={nameValid(names[i]) ? undefined : 'Name must be unique'}>
		</div>
	{/each}
</div>

<div class="uk-width-auto uk-margin">
	<button on:click={adminRun}
	        class="uk-button uk-button-primary uk-border-rounded"
	        disabled={!namesValid()}>
		Run as administrator
	</button>
	<button on:click={participantRun}
	        class="uk-button uk-button-primary uk-border-rounded"
	        disabled={!namesValid()}>
		Run as participant
	</button>
</div>