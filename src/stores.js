import {writable} from 'svelte/store';

// Use values from 1000-1100 only.
export const CheatsheetPages = {
    ASCII: 1000,
    LINUX: 1001,
    PROGRAMS: 1002,
    SCHOOL: 1003,
};
export const CheatsheetUriMap = new Map([
    [CheatsheetPages.ASCII, "/cheatsheet/ascii"],
    [CheatsheetPages.LINUX, "/cheatsheet/linux"],
    [CheatsheetPages.PROGRAMS, "/cheatsheet/programs"],
    [CheatsheetPages.SCHOOL, "/cheatsheet/school"],
]);
export const CheatsheetLabelMap = new Map([
    [CheatsheetPages.ASCII, "Ascii Table"],
    [CheatsheetPages.LINUX, "Linux (Ubuntu)"],
    [CheatsheetPages.PROGRAMS, "Programs"],
    [CheatsheetPages.SCHOOL, "School"],
]);

// Use values from 2000-2100 only.
export const MinecraftPages = {
    COMMANDS: 2000,
    HY_STATS: 2001,
    SERVER: 2002,
};
export const MinecraftUriMap = new Map([
    [MinecraftPages.COMMANDS, "/mc/command"],
    [MinecraftPages.HY_STATS, "/mc/hy_stats"],
    [MinecraftPages.SERVER, "/mc/server"],
]);
export const MinecraftLabelMap = new Map([
    [MinecraftPages.COMMANDS, "Server Commands"],
    [MinecraftPages.HY_STATS, "Hypixel Bedwars Stats"],
    [MinecraftPages.SERVER, "Server Overview"],
]);

// Use values from 3000-3100 only.
export const ProjectPages = {
    CRYPTO: 3000,
    PI: 3001,
    PRIME_FACT: 3002,
    UMLAUT: 3003,
};
export const ProjectUriMap = new Map([
    [ProjectPages.CRYPTO, "/project/crypto"],
    [ProjectPages.PI, "/project/pi"],
    [ProjectPages.PRIME_FACT, "/project/prime_factorization"],
    [ProjectPages.UMLAUT, "/project/umlaut"],
]);
export const ProjectLabelMap = new Map([
    [ProjectPages.CRYPTO, "Cryptography"],
    [ProjectPages.PI, "Pi"],
    [ProjectPages.PRIME_FACT, "Prime Factorization"],
    [ProjectPages.UMLAUT, "Umlaut"],
]);

// Use values from 0-100 only.
export const OtherPages = {
    UNKNOWN: 0,
    HOME: 1,
    CONTACT: 2,
    CHANGELOG: 3,
    IMPRINT: 4,
    PRIVACY: 5,
};
export const OtherUriMap = new Map([
    [OtherPages.HOME, "/"],
    [OtherPages.CONTACT, "/contact"],
    [OtherPages.CHANGELOG, "/changelog"],
    [OtherPages.IMPRINT, "/imprint"],
    [OtherPages.PRIVACY, "/privacy"],
]);
export const OtherLabelMap = new Map([
    [OtherPages.CHANGELOG, "Changelog"],
    [OtherPages.IMPRINT, "Imprint"],
    [OtherPages.PRIVACY, "Privacy"],
]);

export const Pages = {...CheatsheetPages, ...MinecraftPages, ...ProjectPages, ...OtherPages};
export const UriMap = new Map([...CheatsheetUriMap, ...MinecraftUriMap, ...ProjectUriMap, ...OtherUriMap]);
export const LabelMap = new Map([...CheatsheetLabelMap, ...MinecraftLabelMap, ...ProjectLabelMap, ...OtherLabelMap]);

export const currentPage = writable(Pages.UNKNOWN);