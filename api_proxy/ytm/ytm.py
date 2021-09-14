from ytmusicapi import YTMusic
from pprint import pprint
import json


def get_library(cookie, x_goog_user):
    auth = YTMusic.setup(headers_raw=f"cookie: {cookie}\nx-goog-authuser: {x_goog_user}")
    api = YTMusic(auth)

    playlists = [api.get_playlist(lpl['playlistId'], limit=10**9) for lpl in api.get_library_playlists()]
    songs = api.get_library_songs()

    return {'songs': songs, 'playlists': playlists}
