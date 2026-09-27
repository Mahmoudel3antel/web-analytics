class WebsiteAnalyzer:
    """Analyze website traffic data."""

    def __init__(self, data):
        self.data = data

    def total_pageviews(self):
        return len(self.data)

    def unique_sessions(self):
        return self.data["session_id"].nunique()

    def average_duration(self):
        return self.data["duration"].mean()

    def number_of_countries(self):
        return self.data["country"].nunique()

    def most_visited_page(self):
        return self.data["page"].value_counts().idxmax()

    def summary(self):
        return {
            "pageviews": self.total_pageviews(),
            "sessions": self.unique_sessions(),
            "average_duration": self.average_duration(),
            "countries": self.number_of_countries(),
            "top_page": self.most_visited_page(),
        }