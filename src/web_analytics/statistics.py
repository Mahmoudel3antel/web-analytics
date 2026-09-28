import numpy as np
from web_analytics.models import BaseAnalyzer

class StatisticsAnalyzer(BaseAnalyzer):
    """Perform numerical analysis on website duration data."""

    def __init__(self, data):
        super().__init__(data)

    def duration_array(self):
        durations = self.data["duration"].dropna()

        return np.array(durations)

    def mean_duration(self):
        durations = self.duration_array()

        return np.mean(durations)

    def median_duration(self):
        durations = self.duration_array()

        return np.median(durations)

    def standard_deviation(self):
        durations = self.duration_array()

        return np.std(durations)

    def minimum_duration(self):
        durations = self.duration_array()

        return np.min(durations)

    def maximum_duration(self):
        durations = self.duration_array()

        return np.max(durations)

    def percentile_25(self):
        durations = self.duration_array()

        return np.percentile(durations, 25)

    def percentile_75(self):
        durations = self.duration_array()

        return np.percentile(durations, 75)

    def analyze(self):
        return {
            "mean": self.mean_duration(),
            "median": self.median_duration(),
            "standard_deviation": self.standard_deviation(),
            "minimum": self.minimum_duration(),
            "maximum": self.maximum_duration(),
            "percentile_25": self.percentile_25(),
            "percentile_75": self.percentile_75(),
            "outliers": self.number_of_outliers(),
        }

    def duration_outliers(self):
        durations = self.duration_array()

        q1 = np.percentile(durations, 25)
        q3 = np.percentile(durations, 75)

        iqr = q3 - q1

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        outliers = durations[
            (durations < lower_bound)
            | (durations > upper_bound)
        ]

        return outliers

    def number_of_outliers(self):
        return len(self.duration_outliers())