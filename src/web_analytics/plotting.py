import os

import matplotlib.pyplot as plt


class PlotGenerator:
    """Create and save visualizations for website analytics data."""

    def __init__(self, data, output_directory="output"):
        self.data = data
        self.output_directory = output_directory

        os.makedirs(self.output_directory, exist_ok=True)

    def pageviews_by_page(self):
        page_counts = self.data["page"].value_counts()

        plt.figure()
        page_counts.plot(kind="bar")

        plt.title("Pageviews by Page")
        plt.xlabel("Page")
        plt.ylabel("Pageviews")
        plt.tight_layout()

        file_path = os.path.join(
            self.output_directory,
            "pageviews_by_page.png",
        )

        plt.savefig(file_path)
        plt.close()

        return file_path

    def pageviews_by_country(self):
        country_counts = self.data["country"].value_counts()

        plt.figure()
        country_counts.plot(kind="bar")

        plt.title("Pageviews by Country")
        plt.xlabel("Country")
        plt.ylabel("Pageviews")
        plt.tight_layout()

        file_path = os.path.join(
            self.output_directory,
            "pageviews_by_country.png",
        )

        plt.savefig(file_path)
        plt.close()

        return file_path

    def device_distribution(self):
        device_counts = self.data["device"].value_counts()

        plt.figure()
        device_counts.plot(kind="bar")

        plt.title("Device Distribution")
        plt.xlabel("Device")
        plt.ylabel("Pageviews")
        plt.tight_layout()

        file_path = os.path.join(
            self.output_directory,
            "device_distribution.png",
        )

        plt.savefig(file_path)
        plt.close()

        return file_path

    def duration_histogram(self):
        durations = self.data["duration"].dropna()

        plt.figure()
        plt.hist(durations, bins=10)

        plt.title("Visit Duration Distribution")
        plt.xlabel("Duration in Seconds")
        plt.ylabel("Frequency")
        plt.tight_layout()

        file_path = os.path.join(
            self.output_directory,
            "duration_histogram.png",
        )

        plt.savefig(file_path)
        plt.close()

        return file_path

    def pageviews_by_date(self):
        daily_views = (
            self.data.groupby(self.data["timestamp"].dt.date)
            .size()
        )

        plt.figure()

        daily_views.plot(
            kind="line",
            marker="o",
        )

        plt.title("Pageviews by Date")
        plt.xlabel("Date")
        plt.ylabel("Pageviews")
        plt.tight_layout()

        file_path = os.path.join(
            self.output_directory,
            "pageviews_by_date.png",
        )

        plt.savefig(file_path)
        plt.close()

        return file_path