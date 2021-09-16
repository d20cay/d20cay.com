from ytmusicapi import YTMusic
from pprint import pprint
import json


def get_library(cookie, x_goog_authuser):
    auth = YTMusic.setup(headers_raw=f"cookie: {cookie}\nx-goog-authuser: {x_goog_authuser}")
    api = YTMusic(auth)

    playlists = [api.get_playlist(lpl['playlistId'], limit=10**9) for lpl in api.get_library_playlists()]
    songs = api.get_library_songs(limit=10**9)

    return {'songs': songs, 'playlists': playlists}
