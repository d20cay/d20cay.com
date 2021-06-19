export function calculatePrimes(n) {
	if (n < 2) {
		return [];
	}
	let primes = [2];
	for (let i = 2; i <= n; i++) {
		if (isPrime(i, primes)) {
			primes.push(i);
		}
	}
	return primes;
}

function isPrime(n, primes) {
	for (const prime of primes) {
		if (n % prime === 0) {
			return false;
		}
	}
	return true;
}

export function calculateFactors(n, primes) {
	let factors = [];
	let foundFactor = true;
	while (foundFactor) {
		foundFactor = false;
		for (const prime of primes) {
			if (n % prime === 0) {
				foundFactor = true;
				// Factor was found. Add factor to list, update value n, start
				// from beginning.
				factors.push(prime);
				n = n / prime;
				if (primes.indexOf(prime) !== 0) {
					// Remove any smaller primes because those aren't use
					// anymore.
					primes = primes.slice(primes.indexOf(prime), primes.length);
				}
				break;
			}
		}
	}
	if (factors.length === 1) {
		factors.push(n);
	}
	return factors;
}