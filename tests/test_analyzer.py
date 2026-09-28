import unittest

import pandas as pd

from web_analytics.analyzer import WebsiteAnalyzer


class TestWebsiteAnalyzer(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "timestamp": pd.to_datetime(
                    [
                        "2026-09-01 10:00:00",
                        "2026-09-01 10:05:00",
                        "2026-09-01 10:10:00",
                    ]
                ),
                "session_id": ["S001", "S001", "S002"],
                "page": ["/home", "/products", "/home"],
                "country": ["Germany", "Germany", "Egypt"],
                "device": ["mobile", "mobile", "desktop"],
                "duration": [10, 20, 30],
            }
        )

        self.analyzer = WebsiteAnalyzer(self.data)

    def test_total_pageviews(self):
        self.assertEqual(self.analyzer.total_pageviews(), 3)

    def test_unique_sessions(self):
        self.assertEqual(self.analyzer.unique_sessions(), 2)

    def test_average_duration(self):
        self.assertEqual(self.analyzer.average_duration(), 20)

    def test_number_of_countries(self):
        self.assertEqual(self.analyzer.number_of_countries(), 2)

    def test_most_visited_page(self):
        self.assertEqual(
            self.analyzer.most_visited_page(),
            "/home",
        )

    def test_duplicate_rows(self):
        self.assertEqual(
            self.analyzer.duplicate_rows(),
            0,
        )

    def test_total_missing_values(self):
        self.assertEqual(
            self.analyzer.total_missing_values(),
            0,
        )

    def test_pages_per_session(self):
        pages = self.analyzer.pages_per_session()

        self.assertEqual(pages["S001"], 2)
        self.assertEqual(pages["S002"], 1)

    def test_average_pages_per_session(self):
        self.assertEqual(
            self.analyzer.average_pages_per_session(),
            1.5,
        )

    def test_single_page_sessions(self):
        self.assertEqual(
            self.analyzer.single_page_sessions(),
            1,
        )

    def test_bounce_rate(self):
        self.assertEqual(
            self.analyzer.bounce_rate(),
            50,
        )

    def test_top_device(self):
        self.assertEqual(
            self.analyzer.top_device(),
            "mobile",
        )


if __name__ == "__main__":
    unittest.main()