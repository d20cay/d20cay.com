import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from simplejson.errors import JSONDecodeError
from starlette.requests import Request
from starlette.responses import Response

from constant import NO_STATS_ERROR, NO_PLAYER_ERROR
from hypixel_stats.hypixel_stats import bedwars_overview
from ytm.analysis import ytm_analyze
from ytm.ytm import get_library

app = FastAPI()

origins = [
    "http://d20cay.com",
    "https://d20cay.com",
    "http://dev.d20cay.com",
    "https://dev.d20cay.com",
    "http://localhost:3000",
]


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)


app.middleware('http')(catch_exceptions_middleware)

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=['*'],
                   allow_headers=['*'])

mojang_api = 'https://api.mojang.com/users/profiles/minecraft/{}'
hypixel_api_key = '896208eb-4e24-41e6-a485-ba62b4875fb6'
hypixel_api = 'https://api.hypixel.net/player?key={}&uuid={}'


@app.get("/hypixel/stats/{player}")
def read_hypixel_bedwars_stats(player: str):
    try:
        uuid_response = requests.get(mojang_api.format(player))
        player_uuid = uuid_response.json()['id']
    except (JSONDecodeError, KeyError):
        return NO_PLAYER_ERROR

    try:
        hypixel_response = requests.get(
            hypixel_api.format(hypixel_api_key, player_uuid))
        hypixel_json = hypixel_response.json()
        if hypixel_json is None or hypixel_json['player'] is None:
            return NO_STATS_ERROR
        condensed_stats = bedwars_overview(hypixel_json)
    except JSONDecodeError:
        return NO_STATS_ERROR

    return condensed_stats


class YtmLibRequest(BaseModel):
    cookie: str
    x_goog_user: str
    excludeAllPlaylist = False
    excludeForeignPlaylists = False
    username: str


@app.post("/ytm/lib/")
async def read_ytm_library(body: YtmLibRequest):
    library = get_library(body.cookie, body.x_goog_user)
    return {'library': library,
            'analysis': ytm_analyze(library, body.excludeAllPlaylist, body.excludeForeignPlaylists, body.username)}
