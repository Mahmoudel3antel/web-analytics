import numpy as np


class StatisticsAnalyzer:
    """Perform numerical analysis on website duration data."""

    def __init__(self, data):
        self.data = data

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