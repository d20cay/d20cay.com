import {writable} from 'svelte/store';

export const Page = {
    UNKNOWN: 0,
    HOME: 1,
    CONTACT: 2,
    CS_PROGRAMS: 3,
    CS_LINUX: 4,
    CS_SCHOOL: 5,
    MC_COMMAND: 6,
    MC_SERVER: 7,
    UMLAUT: 8,
    HY_STATS: 9,
    CHANGELOG: 10,
    CRYPTO: 11,
    ASCII: 12,
    IMPRINT: 13,
    PRIVACY: 14
};

export const currentPage = writable(Page.UNKNOWN);