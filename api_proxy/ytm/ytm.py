from ytmusicapi import YTMusic
from pprint import pprint


auth = YTMusic.setup(filepath="headers_auth.json", headers_raw="cookie: \nx-goog-authuser: ")
api = YTMusic(auth)

data = api.get_library_playlists()

pprint(data)