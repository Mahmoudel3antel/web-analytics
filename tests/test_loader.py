import os
import tempfile
import unittest

from web_analytics.loader import load_data


class TestLoader(unittest.TestCase):

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_data("not_existing.csv")

    def test_missing_columns(self):
        csv_content = "name,age\nMahmoud,22\n"

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".csv",
            delete=False,
        ) as temporary_file:
            temporary_file.write(csv_content)
            file_path = temporary_file.name

        try:
            with self.assertRaises(ValueError):
                load_data(file_path)

        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()