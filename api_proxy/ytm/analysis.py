import datetime
import logging
import re
from enum import Enum

logging.basicConfig(format='%(asctime)s %(levelname)s - %(message)s', level=logging.DEBUG)


def ytm_analyze(library, exclude_all_playlist, exclude_foreign_playlists, username):
    if exclude_foreign_playlists and username is None:
        logging.warning('Not excluding foreign playlists because username is not set.')

    start_time = datetime.datetime.now()
    # Filter out Likes playlist

    playlists = list(
        filter(lambda pl: playlist_passes_filter(pl, exclude_all_playlist, exclude_foreign_playlists, username),
               [pl for pl in library["playlists"]]))
    # List of all songs
    playlist_songs = [{"track": track, "playlist": {"id": pl["id"], "title": pl["title"]}} for pl in playlists
                      for track in pl["tracks"]]

    logging.info('Iteration count: {}'.format(
        len(library["songs"]) ** 2 + len(library["songs"]) * len(playlist_songs) + len(playlist_songs) ** 2))

    library_song_issues = []
    for i, t1 in enumerate(library["songs"]):
        # Adds duplicates within library itself.
        other_songs = [s for j, s in enumerate(library["songs"]) if i != j]
        inner_duplicates = list(filter(lambda duplicate: duplicate is not None,
                                       [build_duplicate_issue(t1, None, t2, None) for t2 in other_songs]))
        outer_duplicates = list(filter(lambda duplicate: duplicate is not None,
                                       [build_duplicate_issue(t1, None, t2["track"], t2["playlist"]) for t2 in
                                        playlist_songs]))
        library_song_issues += inner_duplicates
        library_song_issues += outer_duplicates

    playlist_song_issues = []
    for i, t1 in enumerate(playlist_songs):
        other_songs = [s for j, s in enumerate(playlist_songs) if i != j]
        playlist_song_issues += list(filter(lambda duplicate: duplicate is not None, [
            build_duplicate_issue(t1["track"], t1["playlist"], t2["track"], t2["playlist"]) for t2 in other_songs]))

    excluded_pl = map(lambda pl: {"id": pl["id"], "author": pl["author"], "title": pl["title"]}, list(filter(
        lambda pl_before: playlist_passes_filter(pl_before, exclude_all_playlist, exclude_foreign_playlists, username),
        library["playlists"])))
    analysis = {"excludedPlaylists": {}, "duplicates": {
        "library": categorize_issues(library_song_issues), "playlists": categorize_issues(playlist_song_issues)
    }}
    logging.info("Analysis completed in {}. Found {} issues.".format(datetime.datetime.now() - start_time,
                                                                     analysis["duplicates"]["library"][
                                                                         "totalDuplicateCount"] +
                                                                     analysis["duplicates"]["playlists"][
                                                                         "totalDuplicateCount"]))
    return analysis


def categorize_issues(issues):
    # Deduplicate duplicates, because duplicates within the same playlist get added twice for each copy of the song.
    for i, issue in enumerate(issues):
        other_issues = [issue2 for j, issue2 in enumerate(issues) if i != j]
        if issue in other_issues:
            issues.remove(issue)
    return {
        "totalDuplicateCount": len(issues),
        "idDuplicates": list(filter(lambda issue: issue["type"] == DuplicateIssueType.ID_DUPLICATE, issues)),
        "titleArtistDuplicates": list(
            filter(lambda issue: issue["type"] == DuplicateIssueType.TITLE_ARTIST_DUPLICATE, issues)),
        "titleDuplicates": list(filter(lambda issue: issue["type"] == DuplicateIssueType.TITLE_DUPLICATE, issues)),
        "simpleTitleDuplicates": list(
            filter(lambda issue: issue["type"] == DuplicateIssueType.SIMPLE_TITLE_DUPLICATE, issues))
    }


def build_duplicate_issue(t1, pl1, t2, pl2):
    duplicate_type = duplicate_type_check(t1, t2)
    return {
        "type": duplicate_type,
        "videoId": t1["videoId"],
        "title": t1["title"],
        "artists": t1["artists"],
        "playlist": None if pl1 is None else {"id": pl1["id"], "title": pl1["title"]},
        "duplicateVideoId": t2["videoId"],
        "duplicateTitle": t2["title"],
        "duplicateArtists": t2["artists"],
        "duplicatePlaylist": None if pl2 is None else {"id": pl2["id"], "title": pl2["title"]},
    } if duplicate_type is not None else None


def duplicate_type_check(t1, t2):
    if t1["videoId"] == t2["videoId"]:
        return DuplicateIssueType.ID_DUPLICATE
    elif t1["title"] == t2["title"] and t1["artists"] == t2["artists"]:
        return DuplicateIssueType.TITLE_ARTIST_DUPLICATE
    elif t1["title"] == t2["title"]:
        return DuplicateIssueType.TITLE_DUPLICATE
    elif simplify_title(t1["title"]) == simplify_title(t2["title"]):
        return DuplicateIssueType.SIMPLE_TITLE_DUPLICATE


def simplify_title(title):
    # Remove any () and containing text from titles.
    removed_brackets = re.sub(r"\(.*\)", "", title)
    return re.sub(r"\s+", " ", removed_brackets).strip()


def playlist_passes_filter(pl, exclude_all_playlist, exclude_foreign_playlists, username):
    likes = pl["title"] == "Your Likes"
    all = pl["title"] == "All"
    foreign = pl["author"] != username
    return not likes or (not all and exclude_all_playlist) or (not foreign and exclude_foreign_playlists)


class DuplicateIssueType(str, Enum):
    ID_DUPLICATE = "ID_DUPLICATE",
    TITLE_ARTIST_DUPLICATE = "TITLE_ARTIST_DUPLICATE",
    TITLE_DUPLICATE = "TITLE_DUPLICATE",
    SIMPLE_TITLE_DUPLICATE = "SIMPLE_TITLE_DUPLICATE",
