from web_analytics.models import BaseAnalyzer

class WebsiteAnalyzer(BaseAnalyzer):
    """Analyze website traffic data."""

    def __init__(self, data):
        super().__init__(data)

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

    def pageviews_by_page(self):
        return self.data["page"].value_counts()

    def pageviews_by_country(self):
        return self.data["country"].value_counts()

    def pageviews_by_device(self):
        return self.data["device"].value_counts()

    def average_duration_by_page(self):
        return (
            self.data.groupby("page")["duration"]
            .mean()
            .sort_values(ascending=False)
        )

    def longest_visit(self):
        return self.data["duration"].max()

    def shortest_visit(self):
        return self.data["duration"].min()

    def summary(self):
        return {
            "pageviews": self.total_pageviews(),
            "sessions": self.unique_sessions(),
            "average_duration": self.average_duration(),
            "countries": self.number_of_countries(),
            "top_page": self.most_visited_page(),
            "longest_visit": self.longest_visit(),
            "shortest_visit": self.shortest_visit(),
        }

    def pageviews_by_date(self):
        daily_views = (
            self.data
            .groupby(self.data["timestamp"].dt.date)
            .size()
        )

        return daily_views

    def pageviews_by_hour(self):
        hourly_views = (
            self.data
            .groupby(self.data["timestamp"].dt.hour)
            .size()
        )

        return hourly_views
    
    def analyze(self):
        return self.summary()
    