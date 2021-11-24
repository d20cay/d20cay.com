import unittest

from ytm.analysis import simplify_title, ytm_analyze, DuplicateIssueType


class TestAnalysis(unittest.TestCase):
    maxDiff = None

    def test_simplify_title(self):
        self.assertEqual(simplify_title("Halle(lujah)"), "Halle", "Should remove (lujah) and leave Halle")
        self.assertEqual(simplify_title("Halle(lujah(ha))"), "Halle", "Should remove (lujah(ha)) and leave Halle")
        self.assertEqual(simplify_title("Halle(lujah(ha)"), "Halle", "Should remove (lujah(ha) and leave Halle")

    def test_ytm_analyze_id_duplicate_library_library(self):
        DUPLICATE_ID_LIBRARY_LIBRARY_SONG_LIBRARY = {
            "songs": [{
                "videoId": "a",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]}, {
                "videoId": "a",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]
            }],
            "playlists": []
        }
        DUPLICATE_ID_LIBRARY_LIBRARY_SONG_ISSUES = {"library": {"totalDuplicateCount": 1, "idDuplicates": [{
            "type": DuplicateIssueType.ID_DUPLICATE,
            "videoId": "a",
            "title": "Heat Waves",
            "artists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "playlist": None,
            "duplicateVideoId": "a",
            "duplicateTitle": "Heat Waves",
            "duplicateArtists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "duplicatePlaylist": None,
        }], "simpleTitleDuplicates": [], "titleArtistDuplicates": [], "titleDuplicates": []},
                                                    "playlists": {"totalDuplicateCount": 0, "idDuplicates": [],
                                                                  "simpleTitleDuplicates": [],
                                                                  "titleArtistDuplicates": [],
                                                                  "titleDuplicates": []}}
        self.assertEqual(ytm_analyze(DUPLICATE_ID_LIBRARY_LIBRARY_SONG_LIBRARY),
                         DUPLICATE_ID_LIBRARY_LIBRARY_SONG_ISSUES)

    def test_ytm_analyze_id_duplicate_library_playlists(self):
        DUPLICATE_ID_LIBRARY_PLAYLISTS_SONG_LIBRARY = {
            "songs": [{
                "videoId": "a",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]
            }],
            "playlists": [{
                "id": "d",
                "title": "Best",
                "tracks": [{
                    "videoId": "a",
                    "title": "Heat Waves",
                    "artists": [
                        {"name": "Glass animals", "id": "b"},
                        {"name": "iann dior", "id": "c"}
                    ]
                }]
            }]
        }
        DUPLICATE_ID_LIBRARY_PLAYLISTS_SONG_ISSUES = {"library": {"totalDuplicateCount": 1, "idDuplicates": [{
            "type": DuplicateIssueType.ID_DUPLICATE,
            "videoId": "a",
            "title": "Heat Waves",
            "artists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "playlist": None,
            "duplicateVideoId": "a",
            "duplicateTitle": "Heat Waves",
            "duplicateArtists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "duplicatePlaylist": {"id": "d", "title": "Best"},
        }], "simpleTitleDuplicates": [], "titleArtistDuplicates": [], "titleDuplicates": []},
                                                      "playlists": {"totalDuplicateCount": 0, "idDuplicates": [],
                                                                    "simpleTitleDuplicates": [],
                                                                    "titleArtistDuplicates": [],
                                                                    "titleDuplicates": []}}
        self.assertEqual(ytm_analyze(DUPLICATE_ID_LIBRARY_PLAYLISTS_SONG_LIBRARY),
                         DUPLICATE_ID_LIBRARY_PLAYLISTS_SONG_ISSUES)


if __name__ == "__main__":
    unittest.main()
