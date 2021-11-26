export const Type = {
	ADDED: 0,
	CHANGED: 1,
	FIXED: 2
}

const LabelType = {
	DEFAULT: `default`,
	SUCCESS: `success`,
	WARNING: `warning`,
	DANGER: `danger`
}

export const TypeMap = new Map([
	[Type.ADDED, LabelType.SUCCESS],
	[Type.CHANGED, LabelType.DEFAULT],
	[Type.FIXED, LabelType.DANGER]
]);

export const TypeTextMap = new Map([
	[Type.ADDED, `ADDED`],
	[Type.CHANGED, `CHANGED`],
	[Type.FIXED, `FIXED`]
]);

export const changelog = [
	{
		date: '2021-11-26',
		version: '2021.47.1',
		changes: [
			{
				text: 'YTM library analysis project. This was huge. I worked on this for basically half a year.',
				type: Type.ADDED
			},
			{
				text: 'Adds secret santa page. Still under construction!',
				type: Type.ADDED
			}
		]
	},
	{
		date: '2021-06-19',
		version: '2021.24.2',
		changes: [
			{
				text: 'changelog of version 2021.24.1 to indicate correct version. Was 2021.23.1.',
				type: Type.FIXED
			},
			{
				text: 'OutOfMemory exception on Pi approximation project when too many point values are stored.',
				type: Type.FIXED
			},
			{
				text: 'Pi project for some smaller code cleanup.',
				type: Type.CHANGED
			},
			{
				text: 'Prime factorization project.',
				type: Type.ADDED
			},
		]
	},
	{
		date: '2021-06-16',
		version: '2021.24.1',
		changes: [
			{
				text: 'Pi approximation project.',
				type: Type.ADDED
			},
		]
	},
	{
		date: '2021-03-24',
		version: '2021.12.1',
		changes: [
			{
				text: 'Physics cheatsheet to add thermal capacity formulas.',
				type: Type.CHANGED
			},
			{
				text: 'Physics cheatsheet to add electricity measurement device inaccuracies formulas.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-03-20',
		version: '2021.11.1',
		changes: [
			{
				text: 'Physics cheatsheet to add performance formula for electricity.',
				type: Type.CHANGED
			},
			{
				text: 'Math cheatsheet to add log and pow rules.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-03-13',
		version: '2021.10.1',
		changes: [
			{
				text: 'Physics cheatsheet to add parallel and serial resistor logic.',
				type: Type.CHANGED
			},
			{
				text: 'Physics cheatsheet to add gas law formulas.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-03-06',
		version: '2021.9.1',
		changes: [
			{
				text: 'Physics cheatsheet to fix oscillation and waves formulas.',
				type: Type.CHANGED
			},
			{
				text: 'Physics cheatsheet to add hydrostatics formulas.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-02-28',
		version: '2021.8.1',
		changes: [
			{
				text: 'Physics cheatsheet to fix some formulas and add more context to oscillation theory.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-02-15',
		version: '2021.7.1',
		changes: [
			{
				text: 'Homepage to include twitch link.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-02-14',
		version: '2021.6.1',
		changes: [
			{
				text: 'Hypixel stats page to include all different modes and a download stats feature to help you plot your progress.',
				type: Type.CHANGED
			},
			{
				text: 'Hypixel stats backend completely to be much more readable and stable.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-02-02',
		version: '2021.5.1',
		changes: [
			{
				text: 'Physics cheatsheet to add some clarifications for theory that isn\'t understandable after not having looked at it for a while.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-01-28',
		version: '2021.4.1',
		changes: [
			{
				text: 'Physics cheatsheet to add some more harmonic oscillation formulas and sketch.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2021-01-14',
		version: '2021.2.1',
		changes: [
			{
				text: 'Physics cheatsheet to add harmonic oscillation formulas and sketch.',
				type: Type.CHANGED
			},
		]
	},
	{
		date: '2020-12-26',
		version: '2020.52.1',
		changes: [
			{
				text: 'Hypixel Bedwars Stats page inability to handle a player not existing in some cases.',
				type: Type.FIXED
			},
		]
	},
	{
		date: '2020-12-19',
		version: '2020.51.2',
		changes: [
			{
				text: 'Imprint page for better legal compliance.',
				type: Type.ADDED
			},
			{
				text: 'Privacy policy page for better legal compliance.',
				type: Type.ADDED
			},
			{
				text: 'Cookie modal that has to be accepted to use the website.',
				type: Type.ADDED
			},
		]
	},
	{
		date: `2020-12-15`,
		version: `2020.51.1`,
		changes: [
			{
				text: `Physics cheatsheet unit for performance.`,
				type: Type.FIXED
			},
			{
				text: `Changelog revision 2020.50.2 to use the correct date.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-12-13`,
		version: `2020.50.2`,
		changes: [
			{
				text: `Github link to footer and home page.`,
				type: Type.ADDED
			},
			{
				text: `Physics cheatsheet to clarify some formulas.`,
				type: Type.CHANGED
			},
			{
				text: `Changelog revision numbers from 2020.50.2 to 2020.50.1.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-12-11`,
		version: `2020.50.1`,
		changes: [
			{
				text: `Changelog revision from date 2020-11-29 to correct version.`,
				type: Type.FIXED
			},
			{
				text: `Physics cheatsheet to add energy conservation formulas.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-11-29`,
		version: `2020.49.1`,
		changes: [
			{
				text: `Math cheatsheet to add some more geometry definitions.`,
				type: Type.CHANGED
			},
			{
				text: `Physics cheatsheet to add angular velocity definitions.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-11-29`,
		version: `2020.48.2`,
		changes: [
			{
				text: `Physics cheatsheet to add some more horizontal throw function definitions.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-11-23`,
		version: `2020.48.1`,
		changes: [
			{
				text: `Physics cheatsheet to add some throw function definitions.`,
				type: Type.CHANGED
			},
			{
				text: `Math cheatsheet to add some geometry similarity definitions.`,
				type: Type.CHANGED
			},
			{
				text: `YouTube video preview on homepage.`,
				type: Type.ADDED
			},
			{
				text: `Link to plancke.io from hy_stats page.`,
				type: Type.ADDED
			},
		]
	},
	{
		date: `2020-11-22`,
		version: `2020.47.2`,
		changes: [
			{
				text: `Physics cheatsheet to add some throw function definitions.`,
				type: Type.CHANGED
			},
			{
				text: `Math cheatsheet to add some geometry definitions.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-11-16`,
		version: `2020.47.1`,
		changes: [
			{
				text: `Physics cheatsheet to add some definitions and add more consistency throughout.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-11-09`,
		version: `2020.46.1`,
		changes: [
			{
				text: `Math cheatsheet to add some geometry definitions.`,
				type: Type.CHANGED
			},
			{
				text: `Physics cheatsheet to add some friction definitions.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-11-02`,
		version: `2020.45.1`,
		changes: [
			{
				text: `Math cheatsheet to add some geometry definitions.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-10-26`,
		version: `2020.44.1`,
		changes: [
			{
				text: `Physics cheatsheet sketch.`,
				type: Type.FIXED
			},
			{
				text: `Physics cheatsheets adding some missing details.`,
				type: Type.CHANGED
			},
			{
				text: `Math cheatsheets to make them one document instead of three.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-10-06`,
		version: `2020.41.1`,
		changes: [
			{
				text: `Vigenere encryption not respecting that non-letter characters shouldn\`t affect the <q>cursor</q> on the keyword.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-10-03`,
		version: `2020.40.3`,
		changes: [
			{
				text: `Hypixel Bedwars stats mod download.`,
				type: Type.ADDED
			},
		]
	},
	{
		date: `2020-10-03`,
		version: `2020.40.2`,
		changes: [
			{
				text: `JSON issue on hy_stats page.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-09-30`,
		version: `2020.40.1`,
		changes: [
			{
				text: `Updated physics cheatsheet with some more subjects and author info.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-09-27`,
		version: `2020.39.2`,
		changes: [
			{
				text: `Updated vector geometry cheatsheet with linear dependency definition.`,
				type: Type.CHANGED
			},
			{
				text: `Physics cheatsheet.`,
				type: Type.ADDED
			},
		]
	},
	{
		date: `2020-09-21`,
		version: `2020.39.1`,
		changes: [
			{
				text: `Chevrons to dropdowns in navbar to differentiate dropdowns.`,
				type: Type.ADDED
			},
		]
	},
	{
		date: `2020-09-20`,
		version: `2020.38.4`,
		changes: [
			{
				text: `Notification shade on hypixel stats page to be less alarming when non-critical error occurs.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-09-20`,
		version: `2020.38.3`,
		changes: [
			{
				text: `Error handling on Hypixel Stats page.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-09-19`,
		version: `2020.38.2`,
		changes: [
			{
				text: `Footer design.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-09-17`,
		version: `2020.38.1`,
		changes: [
			{
				text: `Title on contact page.`,
				type: Type.ADDED
			},
			{
				text: `API crashes due to nonexistent players.`,
				type: Type.FIXED
			},
			{
				text: `Player name not showing correctly in Hypixel stats page.`,
				type: Type.FIXED
			},
			{
				text: `Invisible semantics in navbar.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-09-13`,
		version: `2020.37.5`,
		changes: [
			{
				text: `More keyboard shortcuts cheatsheets`,
				type: Type.ADDED
			},
			{
				text: `Rebranded csp page to programs.`,
				type: Type.CHANGED
			},
			{
				text: `Global function to update URL invisibly.`,
				type: Type.ADDED
			},
			{
				text: `Copy direct link in Hypixel Stats page to silently update url.`,
				type: Type.CHANGED
			},
			{
				text: `URL update on encryption method and direct link functionality.`,
				type: Type.ADDED
			},
		]
	},
	{
		date: `2020-09-12`,
		version: `2020.37.4`,
		changes: [
			{
				text: `Removed manual ad placements.`,
				type: Type.CHANGED
			},
			{
				text: `API crashes due to incomplete Hypixel stats.`,
				type: Type.FIXED
			},
		]
	},
	{
		date: `2020-09-09`,
		version: `2020.37.3`,
		changes: [
			{
				text: `Vigènere Cipher to Cryptography project.`,
				type: Type.ADDED
			},
			{
				text: `Error page to include more personal error message.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-09-08`,
		version: `2020.37.2`,
		changes: [
			{text: `Logo transparency and resolution.`, type: Type.FIXED},
			{
				text: `Changed to using pregenerated data for ASCII table instead of generating data on the fly in the hope that it would improve loading time.`,
				type: Type.CHANGED
			},
		]
	},
	{
		date: `2020-09-07`,
		version: `2020.37.1`,
		changes: [
			{
				text: `Proxy API crash due to user not having played bedwars eight two ultimate.`,
				type: Type.FIXED
			},
			{
				text: `Proxy API crash due to user not having bedwars stats.`,
				type: Type.FIXED
			},
			{
				text: `Copy button for direct link to current user\`s bedwars stats.`,
				type: Type.ADDED
			},
			{
				text: `Make all letters uppercase option to Caesar cipher.`,
				type: Type.ADDED
			},
			{
				text: `Made caesar cipher code more readable.`,
				type: Type.CHANGED
			},
			{
				text: `Removed placeholder text in Caesar cipher output textarea.`,
				type: Type.CHANGED
			},
			{
				text: `General cleanup.`,
				type: Type.CHANGED
			}
		]
	},
	{
		date: `2020-09-06`,
		version: `2020.36.4`,
		changes: [
			{text: `Decryption capability for Caesar cipher.`, type: Type.ADDED}
		]
	},
	{
		date: `2020-09-06`,
		version: `2020.36.3`,
		changes: [
			{text: `Internal proxy API.`, type: Type.ADDED},
			{text: `Hypixel API key exposure.`, type: Type.FIXED},
			{
				text: `Simplified logic of Hypixel stats page in Javascript and moved calculation logic to API.`,
				type: Type.CHANGED
			}
		]
	},
	{
		date: `2020-09-04`,
		version: `2020.36.2`,
		changes: [
			{text: `Cryptography project.`, type: Type.ADDED},
			{text: `Caesar cipher.`, type: Type.ADDED},
			{text: `Ascii table.`, type: Type.ADDED}
		]
	},
	{
		date: `2020-08-31`,
		version: `2020.36.1`,
		changes: [
			{
				text: `Overflow of wide tables in cheatsheets and minecraft pages.`,
				type: Type.FIXED
			}
		]
	},
	{
		date: `2020-08-31`,
		version: `2020.35.2+`,
		changes: [
			{text: `Hypixel Player stats.`, type: Type.ADDED},
			{
				text: `Botched merge of hypixel player stats branch that removed all changes in the last three weeks.`,
				type: Type.FIXED
			}
		]
	},
	{
		date: `2020-08-28`,
		version: `2020.35.1`,
		changes: [
			{
				text: `Added additional author to vector geo cheatsheets.`,
				type: Type.CHANGED
			},
			{text: `French Accent characters to umlaut.`, type: Type.ADDED}
		]
	},
	{
		date: `2020-08-23`,
		version: `2020.34.6`,
		changes: [
			{text: `Added author info to cheatsheets.`, type: Type.CHANGED}
		]
	},
	{
		date: `2020-08-22`,
		version: `2020.34.5-3`,
		changes: [
			{text: `Footer`, type: Type.ADDED},
			{text: `BPMN cheatsheet`, type: Type.ADDED},
			{text: `Changelog`, type: Type.ADDED},
			{text: `Better responsiveness`, type: Type.FIXED},
			{
				text: `Enum values not adjusted to new definition causing crash in umlaut project.`,
				type: Type.FIXED
			}
		]
	},
	{
		date: `2020-08-20`,
		version: `2020.34.2`,
		changes: [
			{text: `Greek alphabet to umlaut project`, type: Type.ADDED},
			{text: `Updated vector geometry cheatsheet`, type: Type.CHANGED}
		]
	},
	{
		date: `2020-08-17`,
		version: `2020.34.1`,
		changes: [
			{
				text: `Opening umlaut project w/o referrer copies undefined`,
				type: Type.FIXED
			}
		]
	}
]