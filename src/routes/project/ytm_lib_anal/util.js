export function getSongShareString(videoId) {
    return `https://music.youtube.com/watch?v=${videoId}&feature=share`;
}

export function getPlaylistShareString(playlistId) {
    return `https://music.youtube.com/playlist?list=${playlistId}&feature=share`;
}