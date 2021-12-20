from ytmusicapi import YTMusic


def get_library(cookie, x_goog_authuser):
    auth = YTMusic.setup(headers_raw=f"cookie: {cookie}\nx-goog-authuser: {x_goog_authuser}")
    api = YTMusic(auth)

    playlists = [api.get_playlist(lpl['playlistId'], limit=10 ** 9) for lpl in api.get_library_playlists()]
    songs = api.get_library_songs(limit=10 ** 9)

    return strip_library(songs, playlists)


def strip_library(songs, playlists):
    playlists = list(map(
        lambda playlist: {"id": playlist["id"], "title": playlist["title"],
                          "author": playlist["author"] if "author" in playlist else "",
                          "tracks": strip_songs(playlist["tracks"])},
        playlists))
    return {"songs": strip_songs(songs), "playlists": playlists}


def strip_songs(songs):
    return list(
        map(lambda song: {"videoId": song["videoId"], "title": song["title"], "artists": song["artists"]}, songs))
