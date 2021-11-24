import unittest

from ytm.analysis import simplify_title, ytm_analyze, DuplicateIssueType


class TestAnalysis(unittest.TestCase):
    maxDiff = None

    def test_simplify_title(self):
        self.assertEqual(simplify_title("Halle(lujah)"), "Halle", "Should remove (lujah) and leave Halle")
        self.assertEqual(simplify_title("Halle(lujah(ha))"), "Halle", "Should remove (lujah(ha)) and leave Halle")
        self.assertEqual(simplify_title("Halle(lujah(ha)"), "Halle", "Should remove (lujah(ha) and leave Halle")

    def test_ytm_analyze_id_duplicate_library_library(self):
        library = {
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
        issues = {"library": {"totalDuplicateCount": 1, "idDuplicates": [{
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
        self.assertEqual(ytm_analyze(library), issues)

    def test_ytm_analyze_title_artist_duplicate_library_library(self):
        library = {
            "songs": [{
                "videoId": "a",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]}, {
                "videoId": "b",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]
            }],
            "playlists": []
        }
        issues = {"library": {"totalDuplicateCount": 2, "titleArtistDuplicates": [{
            "type": DuplicateIssueType.TITLE_ARTIST_DUPLICATE,
            "videoId": "a",
            "title": "Heat Waves",
            "artists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "playlist": None,
            "duplicateVideoId": "b",
            "duplicateTitle": "Heat Waves",
            "duplicateArtists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "duplicatePlaylist": None,
        }, {
            "type": DuplicateIssueType.TITLE_ARTIST_DUPLICATE,
            "videoId": "b",
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
        }], "simpleTitleDuplicates": [], "idDuplicates": [], "titleDuplicates": []},
                  "playlists": {"totalDuplicateCount": 0, "idDuplicates": [],
                                "simpleTitleDuplicates": [],
                                "titleArtistDuplicates": [],
                                "titleDuplicates": []}}
        self.assertEqual(ytm_analyze(library), issues)

    def test_ytm_analyze_title_duplicate_library_library(self):
        library = {
            "songs": [{
                "videoId": "a",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]}, {
                "videoId": "b",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"}
                ]
            }],
            "playlists": []
        }
        issues = {"library": {"totalDuplicateCount": 2, "titleDuplicates": [{
            "type": DuplicateIssueType.TITLE_DUPLICATE,
            "videoId": "a",
            "title": "Heat Waves",
            "artists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "playlist": None,
            "duplicateVideoId": "b",
            "duplicateTitle": "Heat Waves",
            "duplicateArtists": [{"name": "Glass animals", "id": "b"}],
            "duplicatePlaylist": None,
        }, {
            "type": DuplicateIssueType.TITLE_DUPLICATE,
            "videoId": "b",
            "title": "Heat Waves",
            "artists": [{"name": "Glass animals", "id": "b"}],
            "playlist": None,
            "duplicateVideoId": "a",
            "duplicateTitle": "Heat Waves",
            "duplicateArtists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "duplicatePlaylist": None,
        }], "simpleTitleDuplicates": [], "idDuplicates": [], "titleArtistDuplicates": []},
                  "playlists": {"totalDuplicateCount": 0, "idDuplicates": [],
                                "simpleTitleDuplicates": [],
                                "titleArtistDuplicates": [],
                                "titleDuplicates": []}}
        self.assertEqual(ytm_analyze(library), issues)

    def test_ytm_analyze_simple_title_duplicate_library_library(self):
        library = {
            "songs": [{
                "videoId": "a",
                "title": "Heat Waves (Acoustic)",
                "artists": [
                    {"name": "Glass animals", "id": "b"},
                    {"name": "iann dior", "id": "c"}
                ]}, {
                "videoId": "b",
                "title": "Heat Waves",
                "artists": [
                    {"name": "Glass animals", "id": "b"}
                ]
            }],
            "playlists": []
        }
        issues = {"library": {"totalDuplicateCount": 2, "simpleTitleDuplicates": [{
            "type": DuplicateIssueType.SIMPLE_TITLE_DUPLICATE,
            "videoId": "a",
            "title": "Heat Waves (Acoustic)",
            "artists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "playlist": None,
            "duplicateVideoId": "b",
            "duplicateTitle": "Heat Waves",
            "duplicateArtists": [{"name": "Glass animals", "id": "b"}],
            "duplicatePlaylist": None,
        }, {
            "type": DuplicateIssueType.SIMPLE_TITLE_DUPLICATE,
            "videoId": "b",
            "title": "Heat Waves",
            "artists": [{"name": "Glass animals", "id": "b"}],
            "playlist": None,
            "duplicateVideoId": "a",
            "duplicateTitle": "Heat Waves (Acoustic)",
            "duplicateArtists": [
                {"name": "Glass animals", "id": "b"},
                {"name": "iann dior", "id": "c"}
            ],
            "duplicatePlaylist": None,
        }], "titleDuplicates": [], "idDuplicates": [], "titleArtistDuplicates": []},
                  "playlists": {"totalDuplicateCount": 0, "idDuplicates": [],
                                "simpleTitleDuplicates": [],
                                "titleArtistDuplicates": [],
                                "titleDuplicates": []}}
        self.assertEqual(ytm_analyze(library), issues)

    def test_ytm_analyze_id_duplicate_library_playlists(self):
        library = {
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
        issues = {"library": {"totalDuplicateCount": 1, "idDuplicates": [{
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
        self.assertEqual(ytm_analyze(library),
                         issues)


if __name__ == "__main__":
    unittest.main()
