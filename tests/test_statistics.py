import unittest

import pandas as pd

from web_analytics.statistics import StatisticsAnalyzer


class TestStatisticsAnalyzer(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame(
            {
                "duration": [10, 20, 30, 40, 50]
            }
        )

        self.statistics = StatisticsAnalyzer(self.data)

    def test_mean_duration(self):
        self.assertEqual(
            self.statistics.mean_duration(),
            30,
        )

    def test_median_duration(self):
        self.assertEqual(
            self.statistics.median_duration(),
            30,
        )

    def test_minimum_duration(self):
        self.assertEqual(
            self.statistics.minimum_duration(),
            10,
        )

    def test_maximum_duration(self):
        self.assertEqual(
            self.statistics.maximum_duration(),
            50,
        )

    def test_number_of_outliers(self):
        self.assertEqual(
            self.statistics.number_of_outliers(),
            0,
        )


if __name__ == "__main__":
    unittest.main()