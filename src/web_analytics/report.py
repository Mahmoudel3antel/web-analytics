import os


class ReportGenerator:
    """Generate text reports from website analytics results."""

    def __init__(self, output_directory="output"):
        self.output_directory = output_directory

        os.makedirs(self.output_directory, exist_ok=True)

    def generate(self, website_analyzer, statistics_analyzer):
        website_results = website_analyzer.analyze()
        statistics_results = statistics_analyzer.analyze()

        report_lines = [
            "WEBSITE ANALYTICS REPORT",
            "=" * 40,
            "",
            "GENERAL METRICS",
            "-" * 40,
            f"Total pageviews: {website_results['pageviews']}",
            f"Unique sessions: {website_results['sessions']}",
            (
                "Average duration: "
                f"{website_results['average_duration']:.2f} seconds"
            ),
            f"Countries: {website_results['countries']}",
            f"Most visited page: {website_results['top_page']}",
            (
                "Missing values: "
                f"{website_results['missing_values']}"
            ),
            (
                "Duplicate rows: "
                f"{website_results['duplicate_rows']}"
            ),
            (
                "Longest visit: "
                f"{website_results['longest_visit']:.2f} seconds"
            ),
            (
                "Shortest visit: "
                f"{website_results['shortest_visit']:.2f} seconds"
            ),
            "",
            "DURATION STATISTICS",
            "-" * 40,
            f"Mean: {statistics_results['mean']:.2f}",
            f"Median: {statistics_results['median']:.2f}",
            (
                "Standard deviation: "
                f"{statistics_results['standard_deviation']:.2f}"
            ),
            f"Minimum: {statistics_results['minimum']:.2f}",
            f"Maximum: {statistics_results['maximum']:.2f}",
            (
                "25th percentile: "
                f"{statistics_results['percentile_25']:.2f}"
            ),
            (
                "75th percentile: "
                f"{statistics_results['percentile_75']:.2f}"
            ),
            (
                "Duration outliers: "
                f"{statistics_results['outliers']}"
            ),
        ]

        report_text = "\n".join(report_lines)

        file_path = os.path.join(
            self.output_directory,
            "analytics_report.txt",
        )

        with open(file_path, "w", encoding="utf-8") as report_file:
            report_file.write(report_text)

        return file_path