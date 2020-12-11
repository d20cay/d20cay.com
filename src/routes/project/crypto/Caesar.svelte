<script>
	import {
		isLetter,
		isPunctuation,
		isSpace,
		shiftFromLetter,
		substituteChar,
		generateAlphabet,
		fittingKeyType,
		validCaesarKey,
		getKeyPlaceholder,
		KeyType,
		ReadableKeyType
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

	function substitute(keyType,
						key,
						plainText,
						encrypt,
						allLettersUppercase,
						keepSpace,
						keepPunctuation) {
		if (!validCaesarKey(keyType, key) || !plainText || plainText.length < 1) {
			return '';
		}
		let shift;
		let encryptedText = '';

		if (keyType === KeyType.LETTER) {
			shift = shiftFromLetter(key);
		} else if (keyType === KeyType.SHIFT) {
			shift = key % 26;
		} else {
			console.error(`keyType variable (${keyType}) doesn't match any expected value`);
		}

		shift = encrypt ? shift : -shift;

		for (let i = 0; i < plainText.length; i++) {
			let currentChar = plainText.charAt(i);
			if (isLetter(currentChar)) {
				if (allLettersUppercase) {
					currentChar = currentChar.toUpperCase();
				}
				encryptedText += substituteChar(currentChar, shift);
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
		padding: 3px;
	}

	.monospace-font {
		font-family: "Courier New", serif;
	}
</style>

<div class="uk-form-horizontal">
	<div class="uk-margin">
		<label class="uk-form-label" for="caesar-key-type-select">Key type</label>
		<div class="uk-form-controls">
			<select bind:value={keyType}
			        class="uk-select uk-border-rounded"
			        id="caesar-key-type-select">
				{#each Object.entries(KeyType) as key, value}
					<option value="{value}">{ReadableKeyType.get(value)}</option>
				{/each}
			</select>
		</div>
	</div>
	<div class="uk-margin">
		<label class="uk-form-label" for="caesar-key-text">Key</label>
		<div class="uk-form-controls">
			<input bind:value={key}
			       on:keyup={() => keyType = fittingKeyType(key, keyType)}
			       id="caesar-key-text"
			       class="uk-input uk-border-rounded"
			       class:uk-form-danger={!validCaesarKey(keyType, key) && key}
			       placeholder={getKeyPlaceholder(keyType)}
			       type="text">
		</div>
	</div>
	{#if !lowPerf}
		<div class="uk-margin">
			<label class="uk-form-label" for="caesar-key-text">Substitution</label>
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
								<th>Encrypted alphabet</th>
								{#each generateAlphabet() as letter}
									<td class="monospace-font">{substitute(validCaesarKey(keyType,
										key) ?
										keyType :
										KeyType.SHIFT,
										validCaesarKey(keyType, key) ? key : 0,
										letter,
										encrypt,
										allLettersUppercase,
										keepSpace,
										keepPunctuation)}</td>
								{/each}
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	{/if}
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
		<label class="uk-form-label" for="caesar-in-textarea">Text input</label>
		<div class="uk-form-controls">
			<textarea bind:value={plainText}
			          id="caesar-in-textarea"
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
		<label class="uk-form-label" for="caesar-out-textarea">Encrypted text</label>
		<div class="uk-form-controls">
			{#if lowPerf}
				<textarea bind:value={encryptedText} id="vigenere-out-textarea"
				          disabled
				          class="uk-textarea uk-border-rounded"
				          cols="30"
				          rows="10"></textarea>
			{:else}
				<textarea value={substitute(keyType,
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