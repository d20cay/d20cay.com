<script>
	import {currentPage, Page} from "../../../stores";
	import Caesar from "./Caesar.svelte";
	import Vigenere from "./Vigenere.svelte";
	import {onMount} from "svelte";
	import {updateUrl as _updateUrl} from "../../../global";

	currentPage.set(Page.CRYPTO);

	const Cipher = {
		CAESAR: 0,
		VIGENERE: 1,
		SCYTALE: 2,
		TRANSPOSITION: 3
	};

	const CipherMap = new Map([
		['caesar', Cipher.CAESAR],
		['vigenere', Cipher.VIGENERE],
		['scytale', Cipher.SCYTALE],
		['transposition', Cipher.TRANSPOSITION]
	]);

	const CipherReversemap = new Map([
		[Cipher.CAESAR, 'casar'],
		[Cipher.VIGENERE, 'vigenere'],
		[Cipher.SCYTALE, 'scytale'],
		[Cipher.TRANSPOSITION, 'transposition']
	]);

	let linkCipher;
	let cipher;

	onMount(() => {
		const urlParams = window.location.search;
		const params = new URLSearchParams(urlParams);
		linkCipher = cipher = CipherMap.get(params.get('cipher'));
	});

	function updateCipherState(s) {
		cipher = s;
		updateUrl(cipher);
	}

	function updateUrl(cipher) {
		const params = cipher !== undefined ? [
			['cipher', CipherReversemap.get(cipher)]
		] : [];
		_updateUrl(params);
	}
</script>

<svelte:head>
	<title>d20cay | Cryptography Project</title>
</svelte:head>

<h1 class="uk-text-center">
	Cryptography
</h1>
<div uk-grid>
	<div class="uk-width-2-3@m uk-align-center">
		<p>
			While reading Simon Singh's Code Book I got inspired to implement some of the ciphers
			mentioned in the practical form of a website.
		</p>
		<p>
			Feel free to use this cipher to calculate your deepest darkest secrets. All of the
			processing is done client-side and no data is sent to any servers. Unless your machine
			itself is compromised this encryption should be completely safe.
		</p>
	</div>
</div>

<div class="uk-card uk-card-default uk-card-body uk-margin uk-border-rounded">
	<ul uk-tab>
		<li class:uk-active={linkCipher === Cipher.CAESAR}>
			<a href="#" on:click={() => updateCipherState(Cipher.CAESAR)}>Caesar</a>
		</li>
		<li class:uk-active={linkCipher === Cipher.VIGENERE}>
			<a href="#" on:click={() => updateCipherState(Cipher.VIGENERE)}>Vigenère</a></li>
		<li class:uk-active={linkCipher === Cipher.SCYTALE}>
			<a href="#" on:click={() => updateCipherState(Cipher.SCYTALE)}>Scytale</a></li>
		<li class:uk-active={linkCipher === Cipher.TRANSPOSITION}>
			<a href="#" on:click={() => updateCipherState(Cipher.TRANSPOSITION)}>Transposition</a>
		</li>
	</ul>
	<ul class="uk-switcher uk-margin">
		<li>
			<Caesar/>
		</li>
		<li>
			<Vigenere/>
		</li>
		<li>
			<h5 class="uk-text-center uk-margin-top">
				Coming soon!
			</h5>
		</li>
		<li>
			<h5 class="uk-text-center uk-margin-top">
				Coming soon!
			</h5>
		</li>
	</ul>
</div>