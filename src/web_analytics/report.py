import os


class ReportGenerator:
    """Generate text reports from website analytics results."""

    def __init__(self, output_directory="output"):
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def generate(self, website_analyzer, statistics_analyzer):
        website_results = website_analyzer.analyze()
        statistics_results = statistics_analyzer.analyze()

        top_pages = website_analyzer.top_pages()
        top_countries = website_analyzer.top_countries()
        country_percentages = website_analyzer.country_percentages()
        device_percentages = website_analyzer.device_percentages()

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
            "SESSION METRICS",
            "-" * 40,
            (
                "Average pages per session: "
                f"{website_results['average_pages_per_session']:.2f}"
            ),
            (
                "Bounce rate: "
                f"{website_results['bounce_rate']:.2f}%"
            ),
            (
                "Busiest hour: "
                f"{website_results['busiest_hour']}:00"
            ),
            (
                "Top device: "
                f"{website_results['top_device']}"
            ),
            (
                "Top device share: "
                f"{website_results['top_device_percentage']:.2f}%"
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
            "",
            "TOP PAGES",
            "-" * 40,
        ]

        for page, count in top_pages.items():
            report_lines.append(
                f"{page}: {count} pageviews"
            )

        report_lines.extend(
            [
                "",
                "TOP COUNTRIES",
                "-" * 40,
            ]
        )

        for country, count in top_countries.items():
            percentage = country_percentages[country]

            report_lines.append(
                f"{country}: {count} pageviews ({percentage:.2f}%)"
            )

        report_lines.extend(
            [
                "",
                "DEVICE DISTRIBUTION",
                "-" * 40,
            ]
        )

        for device, percentage in device_percentages.items():
            report_lines.append(
                f"{device}: {percentage:.2f}%"
            )

        report_text = "\n".join(report_lines)

        file_path = os.path.join(
            self.output_directory,
            "analytics_report.txt",
        )

        with open(file_path, "w", encoding="utf-8") as report_file:
            report_file.write(report_text)

        return file_path