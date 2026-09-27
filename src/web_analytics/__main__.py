from web_analytics.loader import load_data


def main():
    file_path = "data/website_events.csv"

    data = load_data(file_path)

    print("Website Analytics Analyzer")
    print()
    print(data)


if __name__ == "__main__":
    main()