from web_analytics.analyzer import WebsiteAnalyzer
from web_analytics.statistics import StatisticsAnalyzer
from web_analytics.loader import load_data
from web_analytics.plotting import PlotGenerator


def main():
    file_path = "data/website_events.csv"

    try:
        data = load_data(file_path)
        analyzer = WebsiteAnalyzer(data)
        statistics = StatisticsAnalyzer(data)
        plots = PlotGenerator(data)
        

        print("Website Analytics Analyzer")
        print("=" * 35)

        print(f"Total pageviews: {analyzer.total_pageviews()}")
        print(f"Unique sessions: {analyzer.unique_sessions()}")
        print(
            f"Average duration: "
            f"{analyzer.average_duration():.2f} seconds"
        )
        print(f"Countries: {analyzer.number_of_countries()}")
        print(f"Most visited page: {analyzer.most_visited_page()}")
        print(f"Longest visit: {analyzer.longest_visit()} seconds")
        print(f"Shortest visit: {analyzer.shortest_visit()} seconds")

        print()
        print("Pageviews by page")
        print("-" * 20)
        print(analyzer.pageviews_by_page())

        print()
        print("Pageviews by country")
        print("-" * 20)
        print(analyzer.pageviews_by_country())

        print()
        print("Pageviews by device")
        print("-" * 20)
        
        print(analyzer.pageviews_by_device())

        print()
        print("Duration Statistics")
        print("-" * 20)

        print(f"Mean: {statistics.mean_duration():.2f}")
        print(f"Median: {statistics.median_duration():.2f}")
        print(
            f"Standard deviation: "
            f"{statistics.standard_deviation():.2f}"
        )
        print(f"Minimum: {statistics.minimum_duration():.2f}")
        print(f"Maximum: {statistics.maximum_duration():.2f}")
        print(f"25th percentile: {statistics.percentile_25():.2f}")
        print(f"75th percentile: {statistics.percentile_75():.2f}")

        print()
        print("Generating plots")
        print("-" * 20)

        generated_plots = [
            plots.pageviews_by_page(),
            plots.pageviews_by_country(),
            plots.device_distribution(),
            plots.duration_histogram(),
        ]      

        for plot_path in generated_plots:
            print(f"Saved: {plot_path}")




        
    except FileNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Invalid dataset: {error}")


if __name__ == "__main__":
    main()