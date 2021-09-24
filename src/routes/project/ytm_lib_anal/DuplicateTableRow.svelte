<script>
	export let duplicate;

	function getSongShareString(videoId) {
		return `https://music.youtube.com/watch?v=${videoId}&feature=share`;
	}

	function getPlaylistShareString(playlistId) {
		return `https://music.youtube.com/playlist?list=${playlistId}&feature=share`;
	}
</script>


<tr>
	<td>
		<a href={getSongShareString(duplicate.videoId)}>{duplicate.title}</a>
	</td>
	<td>
		<a href={getSongShareString(duplicate.duplicateVideoId)}>{duplicate.duplicateTitle}</a>
	</td>
	<td>{duplicate.artists.map(a => a.name)}</td>
	<td>{duplicate.duplicateArtists.map(a => a.name)}</td>
	<td>
		{#if duplicate.playlist === undefined}
			Library Songs
		{:else}
			<a href={getPlaylistShareString(duplicate.playlist.id)}>{duplicate.playlist.title}</a>
		{/if}
	</td>
	<td>
		{#if duplicate.duplicatePlaylist === undefined} Library
			Songs
		{:else}
			<a href={getPlaylistShareString(duplicate.duplicatePlaylist.id)}>{duplicate.duplicatePlaylist.title}</a>
		{/if}
	</td>
</tr>