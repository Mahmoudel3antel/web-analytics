from web_analytics.loader import load_data
from web_analytics.analyzer import WebsiteAnalyzer


def main():
    file_path = "data/website_events.csv"

    data = load_data(file_path)

    analyzer = WebsiteAnalyzer(data)

    print("Website Analytics Analyzer")
    print("--------------------------")
    print(f"Total pageviews: {analyzer.total_pageviews()}")
    print(f"Unique sessions: {analyzer.unique_sessions()}")
    print(f"Average duration: {analyzer.average_duration():.2f} seconds")
    print(f"Countries: {analyzer.number_of_countries()}")
    print(f"Most visited page: {analyzer.most_visited_page()}")


if __name__ == "__main__":
    main()