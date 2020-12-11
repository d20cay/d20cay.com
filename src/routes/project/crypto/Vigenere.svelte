<script>
	import {
		isLetter,
		isPunctuation,
		isSpace,
		shiftFromLetter,
		substituteChar,
		generateAlphabet,
		generateRepeatedKey,
		validVigenereKey,
		currentVigenereShift,
	} from "./util";

	let plainText;
	let keyType;
	let key;
	let encryptedText;
	let keyPlaceholder;
	let encrypt = true;
	let allLettersUppercase = true;
	let keepSpace = false;
	let keepPunctuation = false;
	let lowPerf = false;

	function substitute(key,
						plainText,
						encrypt,
						allLettersUppercase,
						keepSpace,
						keepPunctuation) {
		if (!validVigenereKey(key) || !plainText || plainText.length < 1) {
			return '';
		}
		let encryptedText = '';
		let keyWordIndex = 0;

		for (let i = 0; i < plainText.length; i++) {
			let shift = currentVigenereShift(key, keyWordIndex);
			shift = encrypt ? shift : -shift;

			let currentChar = plainText.charAt(i);
			if (isLetter(currentChar)) {
				if (allLettersUppercase) {
					currentChar = currentChar.toUpperCase();
				}
				encryptedText += substituteChar(currentChar, shift);

				// Move one letter along in the keyword here to avoid incorrectly encrypting characters that aren't letters.
				keyWordIndex += 1;
			} else if (isSpace(currentChar) && keepSpace) {
				encryptedText += currentChar;
			} else if (isPunctuation(currentChar) && keepPunctuation) {
				encryptedText += currentChar;
			} else {
				encryptedText += '';
			}
		}
		return encryptedText;
	}
</script>

<style>
	/** Changes the mouse cursor into a point (hand) when hovering over objects with this class. */
	.pointer-cursor:hover {
		cursor: pointer;
	}

	.table-small th,
	.table-small td {
		margin: 3px;
		padding: 3px;
	}

	.monospace-font {
		font-family: "Courier New", serif;
	}
</style>

<div class="uk-form-horizontal">
	<div class="uk-margin">
		<label class="uk-form-label" for="vigenere-key-text">Key</label>
		<div class="uk-form-controls">
			<input bind:value={key}
			       id="vigenere-key-text"
			       class="uk-input uk-border-rounded"
			       class:uk-form-danger={!validVigenereKey(key) && key}
			       placeholder="king"
			       type="text">
		</div>
	</div>
	{#if !lowPerf}
		<div class="uk-margin">
			<label class="uk-form-label" for="vigenere-key-text">Substitution</label>
			<div class="uk-form-controls">
				<div class="uk-overflow-auto">
					<table class="uk-table table-small uk-overflow-auto">
						<tbody>
							<tr>
								<th>Alphabet</th>
								{#each generateAlphabet() as letter}
									<td class="monospace-font">{letter}</td>
								{/each}
							</tr>
							<tr>
								<th>Key Letters</th>
								{#each generateRepeatedKey(key) as letter}
									<td class="monospace-font">{letter}</td>
								{/each}
							</tr>
							<tr>
								<th>Encrypted alphabet</th>
								{#each substitute(validVigenereKey(key) ? key : 'a',
									generateAlphabet().join(''),
									encrypt,
									allLettersUppercase,
									keepSpace,
									keepPunctuation).split('') as letter}
									<td class="monospace-font">{letter}</td>
								{/each}
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	{/if}
	<div class="uk-margin">
		<div class="uk-form-label"></div>
		<div class="uk-form-controls">
			<ul uk-accordion>
				<li>
					<a class="uk-accordion-title" style="font-size: medium" href="#">Vigenère
						Square</a>
					<div class="uk-accordion-content">
						<table class="uk-table table-small uk-overflow-auto">
							<thead>
								<tr>
									<th>Shift</th>
									<th colspan="26">Alphabet</th>
								</tr>
							</thead>
							<tbody>
								{#each generateAlphabet() as baseLetter}
									<tr>
										<td class="monospace-font">
											{shiftFromLetter(baseLetter)}
										</td>
										{#each substitute(validVigenereKey(key) ? key : baseLetter,
											generateAlphabet().join(''),
											true,
											true,
											false,
											false).split('') as letter}
											<td class="monospace-font">{letter}</td>
										{/each}
									</tr>
								{/each}
							</tbody>
						</table>
					</div>
				</li>
			</ul>
		</div>
	</div>
	<div class="uk-margin">
		<div class="uk-form-label">More options</div>
		<div class="uk-form-controls">
			<label><input bind:checked={encrypt} class="uk-checkbox" type="checkbox">
				Encrypt</label>
			<span class="uk-margin-small-right pointer-cursor"
			      uk-icon="info"
			      uk-tooltip="Defines whether you want to encrypt or decrypt the text."></span><br>
			<label><input bind:checked={allLettersUppercase} class="uk-checkbox" type="checkbox">
				Make all letters uppercase</label>
			<span class="uk-margin-small-right pointer-cursor"
			      uk-icon="info"
			      uk-tooltip="Improves security"></span><br>
			<label><input bind:checked={keepSpace} class="uk-checkbox" type="checkbox"> Keep spaces
				and line breaks in encrypted text</label>
			<span class="uk-margin-small-right pointer-cursor"
			      uk-icon="info"
			      uk-tooltip="Improves security"></span><br>
			<label><input bind:checked={keepPunctuation} class="uk-checkbox" type="checkbox"> Keep
				punctuation in encrypted text</label>
			<span class="uk-margin-small-right pointer-cursor"
			      uk-icon="info"
			      uk-tooltip="Improves security"></span><br>
			<label><input bind:checked={lowPerf}
			              on:click={() => encryptedText = substitute(keyType, key, plainText, encrypt, allLettersUppercase, keepSpace, keepPunctuation)}
			              class="uk-checkbox"
			              type="checkbox"> Ultra low-performance mode</label>
			<span class="uk-margin-small-right pointer-cursor"
			      uk-icon="info"
			      uk-tooltip="Disables the constant recalculation of the encrypted text. Will require you to press the encrypt button to encrypt."></span>
		</div>
	</div>
	<div class="uk-margin">
		<label class="uk-form-label" for="vigenere-in-textarea">Text input</label>
		<div class="uk-form-controls">
			<textarea bind:value={plainText}
			          id="vigenere-in-textarea"
			          class="uk-textarea uk-border-rounded"
			          placeholder="Lorem ipsum dolor sit amet..."
			          cols="30"
			          rows="10"></textarea>
		</div>
	</div>
	{#if lowPerf}
		<div class="uk-margin">
			<div class="uk-form-controls">
				<button on:click={() => encryptedText = substitute(keyType, key, plainText, encrypt, allLettersUppercase, keepSpace, keepPunctuation)}
				        class="uk-button uk-button-default uk-border-rounded">
					Encrypt
				</button>
			</div>
		</div>
	{/if}
	<div class="uk-margin">
		<label class="uk-form-label" for="vigenere-out-textarea">Encrypted text</label>
		<div class="uk-form-controls">
			{#if lowPerf}
				<textarea bind:value={encryptedText} id="vigenere-out-textarea"
				          disabled
				          class="uk-textarea uk-border-rounded"
				          cols="30"
				          rows="10"></textarea>
			{:else}
				<textarea value={substitute(
					key,
					plainText,
					encrypt,
					allLettersUppercase,
					keepSpace,
					keepPunctuation)} id="vigenere-out-textarea"
				          disabled
				          class="uk-textarea uk-border-rounded"
				          cols="30"
				          rows="10"></textarea>
			{/if}
		</div>
	</div>
</div>