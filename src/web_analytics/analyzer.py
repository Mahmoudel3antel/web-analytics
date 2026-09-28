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
            "missing_values": self.total_missing_values(),
            "duplicate_rows": self.duplicate_rows(),
            "average_pages_per_session": self.average_pages_per_session(),
            "bounce_rate": self.bounce_rate(),
            "busiest_hour": self.busiest_hour(),
            "top_device": self.top_device(),
            "top_device_percentage": self.top_device_percentage(),
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

    def missing_values(self):
        return self.data.isna().sum()

    def total_missing_values(self):
        return self.data.isna().sum().sum()
    def duplicate_rows(self):
        return self.data.duplicated().sum()
    def pages_per_session(self):
        pages_per_session = (
            self.data.groupby("session_id")
            .size()
        )

        return pages_per_session


    def average_pages_per_session(self):
        pages_per_session = self.pages_per_session()

        return pages_per_session.mean()


    def single_page_sessions(self):
        pages_per_session = self.pages_per_session()

        return (pages_per_session == 1).sum()


    def bounce_rate(self):
        total_sessions = self.unique_sessions()

        if total_sessions == 0:
            return 0.0

        bounced_sessions = self.single_page_sessions()

        return (bounced_sessions / total_sessions) * 100
    def busiest_hour(self):
        hourly_views = self.pageviews_by_hour()

        return hourly_views.idxmax()
    def top_device(self):
        return self.data["device"].value_counts().idxmax()
    def top_device_percentage(self):
        device_counts = self.data["device"].value_counts()

        top_device_count = device_counts.max()
        total_pageviews = self.total_pageviews()

        return (top_device_count / total_pageviews) * 100
    def top_pages(self, limit=3):
        return self.data["page"].value_counts().head(limit)

    def top_countries(self, limit=3):
        return self.data["country"].value_counts().head(limit)


    def country_percentages(self):
        counts = self.data["country"].value_counts()
        total = self.total_pageviews()

        return (counts / total) * 100


    def device_percentages(self):
        counts = self.data["device"].value_counts()
        total = self.total_pageviews()

        return (counts / total) * 100
    def average_duration_by_device(self):
        return (
            self.data.groupby("device")["duration"]
            .mean()
            .sort_values(ascending=False)
        )
    def average_duration_by_country(self):
        return (
            self.data.groupby("country")["duration"]
            .mean()
            .sort_values(ascending=False)
        )


    