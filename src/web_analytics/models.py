from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):
    """Base class for all website analytics analyzers."""

    def __init__(self, data):
        if data.empty:
            raise ValueError("Cannot analyze an empty dataset.")

        self.data = data

    @abstractmethod
    def analyze(self):
        """Return the main analysis results."""
        pass