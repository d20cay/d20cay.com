export const IssueType = {
    DUPLICATE: 0,
};

export const DuplicateIssueType = {
    ID_DUPLICATE: 0,
    TITLE_ARTIST_DUPLICATE: 1,
    TITLE_DUPLICATE: 2,
    SIMPLE_TITLE_DUPLICATE: 3,
}

export function duplicateAnalysis(library) {
    let librarySongIssues = [];
    library.songs.forEach((t1, i) => {
        // Adds duplicates within library itself.
        library.songs.filter((_, j) => i !== j).forEach(t2 => {
            librarySongIssues.push(duplicateTypeCheck(t1, undefined, t2, undefined));
        });
        // Adds duplicates between library and other playlists.
        library.playlists.forEach(pl => {
            pl.tracks.forEach(t2 => {
                librarySongIssues.push(duplicateTypeCheck(t1, undefined, t2, pl));
            })
        });
    });

    let playlistSongIssues = [];
    library.playlists.forEach(pl1 => pl1.tracks.forEach((t1, i) => {
        // Adds duplicates within library playlists.
        pl1.tracks.filter((_, j) => i !== j).forEach(t2 => {
            playlistSongIssues.push(duplicateTypeCheck(t1, pl1, t2, pl1))
        });
        // Adds duplicates between different library playlists.
        library.playlists.filter(pl2 => pl2.id !== pl1.id)
            .forEach(pl2 => pl2.tracks.forEach(t2 => {
                playlistSongIssues.push(duplicateTypeCheck(t1, pl1, t2, pl2));
            }));
    }));


    return {
        library: categorizeIssues(librarySongIssues), playlists: categorizeIssues(playlistSongIssues)
    };
}

function categorizeIssues(issues) {
    // Deduplicate all issues, because duplicates within playlists are stored twice otherwise.
    issues = issues.filter((issue, i, self) =>
        i === self.findIndex((issue1) => JSON.stringify(issue) === JSON.stringify(issue1))
    );
    console.log(issues);
    return {
        'totalDuplicates': issues.filter(i => i !== undefined).length,
        'idDuplicates': issues.filter(i => i !== undefined && i.type === DuplicateIssueType.ID_DUPLICATE),
        'titleArtistDuplicates': issues.filter(i => i !==
            undefined &&
            i.type ===
            DuplicateIssueType.TITLE_ARTIST_DUPLICATE),
        'titleDuplicates': issues.filter(i => i !== undefined && i.type === DuplicateIssueType.TITLE_DUPLICATE),
        'simpleTitleDuplicates': issues.filter(i => i !==
            undefined &&
            i.type ===
            DuplicateIssueType.SIMPLE_TITLE_DUPLICATE),
    };
}

function duplicateTypeCheck(t1, pl1, t2, pl2) {
    if (t1.videoId === t2.videoId) {
        return buildDuplicateIssue(t1, pl1, t2, pl2, DuplicateIssueType.ID_DUPLICATE);
    } else if (t1.title === t2.title && JSON.stringify(t1.artists) === JSON.stringify(t2.artists)) {
        return buildDuplicateIssue(t1, pl1, t2, pl2, DuplicateIssueType.TITLE_ARTIST_DUPLICATE);
    } else if (t1.title === t2.title) {
        return buildDuplicateIssue(t1, pl1, t2, pl2, DuplicateIssueType.TITLE_DUPLICATE);
    } else if (simplifyTitle(t1.title) === simplifyTitle(t2.title)) {
        return buildDuplicateIssue(t1, pl1, t2, pl2, DuplicateIssueType.SIMPLE_TITLE_DUPLICATE);
    } else {
        return undefined;
    }
}

function buildDuplicateIssue(t1, pl1, t2, pl2, duplicateType) {
    return {
        type: duplicateType,
        videoId: t1.videoId,
        title: t1.title,
        artists: t1.artists,
        playlist: pl1 === undefined ? undefined : {id: pl1.id, title: pl1.title},
        duplicateVideoId: t2.videoId,
        duplicateTitle: t2.title,
        duplicateArtists: t2.artists,
        duplicatePlaylist: pl2 === undefined ? undefined : {id: pl2.id, title: pl2.title}
    };
}

function simplifyTitle(title) {
    if ((title.match(/\(/g) || []).length === (title.match(/\)/g) || []).length) {
        while ((title.match(/\(/g) || []).length > 0 && (title.match(/\)/g) || []).length > 0) {
            const openingIndex = title.indexOf('(');
            const closingIndex = title.indexOf(')');
            if (openingIndex !== 0 && title[openingIndex - 1] === ' ') {
                title = title.substr(0, openingIndex - 1) + title.substr(closingIndex + 1, title.length - 1)
            } else if (closingIndex !== title.length - 1 && title[closingIndex + 1] === ' ') {
                title = title.substr(0, openingIndex) + title.substr(closingIndex + 2, title.length - 1)
            } else {
                return title;
            }
        }
    }
    return title;
}