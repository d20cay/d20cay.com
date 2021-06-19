export function generatePoints(count) {
	let p = [];
	for (let i = 0; i < count; i++) {
		p.push(generatePoint());
	}
	return p;
}

export function generatePoint() {
	return {x: (Math.random() - 0.5) * 2, y: (Math.random() - 0.5) * 2};
}