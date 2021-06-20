export function emptyFields(board) {
	let indices = [];
	for (const [y, row] of board) {
		for (const [x, _] of row) {
			indices.push([x, y]);
		}
	}
	return indices;
}

export function validNumbers(board, x, y) {
	const rowIndices = [];
	for (let i = 0; i < 9; i++) {
		rowIndices.append(i, y);
	}
	const rowNumbers = rowIndices.map(i => board[i[0]][i[1]]);

	const columnIndices = [];
	for (let i = 0; i < 9; i++) {
		rowIndices.append(x, i);
	}
	const columnNumbers = columnIndices.map(i => board[i[0]][i[1]]);

	const topLeftGroupFieldIndex = {x: Math.ceil(x / 3), y: Math.ceil(y / 3)};
	const groupIndices = [];
	for (let i = 0; i < 9; i++) {
		groupIndices.append(topLeftGroupFieldIndex.x + i % 3,
			topLeftGroupFieldIndex.y + Math.floor(i / 3));
	}
	const groupNumbers = groupIndices.map(i => board[i[0]][i[1]]);

	const existingNumbers = [
		...new Set(rowNumbers.concat(columnNumbers, groupNumbers))
	];
	return allNumbers.filter(n => !existingNumbers.includes(n))
}

const allNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

export const defaultBoard = [
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
	[
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined,
		undefined
	],
];