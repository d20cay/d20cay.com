import {writable} from 'svelte/store';

// Use values from 1000-1100 only.
export const CheatsheetPages = {
    ASCII: 1000,
    LINUX: 1001,
    PROGRAMS: 1002,
    SCHOOL: 1003,
};

// Use values from 2000-2100 only.
export const MinecraftPages = {
    COMMANDS: 2000,
    HY_STATS: 2001,
    SERVER: 2002,
};

// Use values from 3000-3100 only.
export const ProjectPages = {
    CRYPTO: 3000,
    PI: 3001,
    PRIME_FACT: 3002,
    UMLAUT: 3003,
};

// Use values from 0-100 only.
export const OtherPages = {
    UNKNOWN: 0,
    HOME: 1,
    CONTACT: 2,
    CHANGELOG: 3,
    IMPRINT: 4,
    PRIVACY: 5,
};

export const Pages = {...CheatsheetPages, ...MinecraftPages, ...ProjectPages, ...OtherPages};

export const currentPage = writable(Pages.UNKNOWN);