const LETTER_MATCHING_REGEX = /^[A-Za-z]$/;
const AT_LEAST_ONE_LETTER_MATCHING_REGEX = /^[A-Za-z]+$/;
const NUMBER_MATCHING_REGEX = /^\d+$/;
const CHARCODE_UPPERCASE_A = 65;
const CHARCODE_LOWERCASE_A = 97;
const ALPHABET_LENGTH = 26;
const SPACE_REGEX = /\s/;
const PUCTUATION_REGEX = /[\.,;:!\?<>\/\\'"\[\]{}\-_=\+\)\(\*&\^%\$#@~`]/;

export const KeyType = {
	LETTER: 0,
	SHIFT: 1
};

export const ReadableKeyType = new Map([
	[KeyType.LETTER, 'Letter'],
	[KeyType.SHIFT, 'Shift']
]);

function isUppercase(char) {
	return char === char.toUpperCase();
}

function isLowercase(char) {
	return char === char.toLowerCase();
}

export function isLetter(char) {
	return LETTER_MATCHING_REGEX.test(char);
}

export function isSpace(char) {
	return SPACE_REGEX.test(char);
}

export function isPunctuation(char) {
	return PUCTUATION_REGEX.test(char);
}

export function shiftFromLetter(letter) {
	if (isUppercase(letter)) {
		return letter.charCodeAt(0) - CHARCODE_UPPERCASE_A;
	} else if (isLowercase(letter)) {
		return letter.charCodeAt(0) - CHARCODE_LOWERCASE_A;
	} else {
		console.error(
			'function shiftFromLetter() should not be called if argument is not a letter.');
	}
}

function substituteUpperOrLowercaseChar(charCode, shift, baseCharCode) {
	if (shift > 0) {
		const cutShift = shift % ALPHABET_LENGTH;
		// Reduce to base, add shift, module if wraps, lift to letter
		return (charCode - baseCharCode + cutShift) %
			ALPHABET_LENGTH +
			baseCharCode;
	} else if (shift < 0) {
		const cutShift = (Math.abs(shift)) % ALPHABET_LENGTH;
		// Reduce to base, add alphabet length, subtract shift, lift to letter
		return (charCode -
			baseCharCode +
			ALPHABET_LENGTH -
			cutShift) %
			ALPHABET_LENGTH +
			baseCharCode;
	} else {
		return charCode;
	}
}

export function substituteChar(char, shift) {
	const charCode = char.charCodeAt(0);
	let shiftedCharCode;
	if (isUppercase(char)) {
		shiftedCharCode =
			substituteUpperOrLowercaseChar(charCode,
				shift,
				CHARCODE_UPPERCASE_A);
	} else if (isLowercase(char)) {
		shiftedCharCode =
			substituteUpperOrLowercaseChar(charCode,
				shift,
				CHARCODE_LOWERCASE_A);
	} else {
		console.error(
			'function substituteChar() should not be called if character is not a letter.');
	}
	return String.fromCharCode(shiftedCharCode);
}

export function currentVigenereShift(key, i) {
	const currentCharacter = key[i % key.length];
	if (isUppercase(currentCharacter)) {
		return currentCharacter.charCodeAt(0) - CHARCODE_UPPERCASE_A;
	} else if (isLowercase(currentCharacter)) {
		return currentCharacter.charCodeAt(0) - CHARCODE_LOWERCASE_A;
	} else {
		console.error(
			'function currentVigenereShift() should not be called if key is not a string of letters.');
	}
}

export function generateAlphabet() {
	return Array.from(Array(26),
		(_, i) => String.fromCharCode(i + CHARCODE_UPPERCASE_A));
}

export function generateRepeatedKey(key) {
	if (!validVigenereKey(key) || !key) {
		return generateAlphabet();
	}
	let repeatedKey = [];
	for (let i = 0; i < ALPHABET_LENGTH; i += key.length) {
		repeatedKey.push(...key.split(''));
	}
	repeatedKey = repeatedKey.slice(0, 26).map(letter => letter.toUpperCase());
	return repeatedKey;
}

export function fittingKeyType(key, keyType) {
	if (LETTER_MATCHING_REGEX.test(key) && keyType !== KeyType.LETTER) {
		return KeyType.LETTER;
	} else if (NUMBER_MATCHING_REGEX.test(key) && keyType !== KeyType.SHIFT) {
		return KeyType.SHIFT;
	} else {
		return keyType;
	}
}

export function validCaesarKey(keyType, key) {
	if (keyType === KeyType.LETTER) {
		return LETTER_MATCHING_REGEX.test(key);
	} else if (keyType === KeyType.SHIFT) {
		return NUMBER_MATCHING_REGEX.test(key);
	}
}

export function validVigenereKey(key) {
	return key && AT_LEAST_ONE_LETTER_MATCHING_REGEX.test(key);
}

export function getKeyPlaceholder(keyType) {
	if (keyType === KeyType.LETTER) {
		return 'x';
	} else if (keyType === KeyType.SHIFT) {
		return '17';
	}
}