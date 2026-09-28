# Web Analytics Analyzer

A Python package for analyzing website traffic data from CSV files.

The project loads website event data, validates the dataset, calculates traffic and session metrics, performs numerical analysis using NumPy, and generates visualizations and a text report.

## Features

The analyzer provides:

- Total pageviews
- Unique sessions
- Average visit duration
- Number of countries
- Most visited page
- Longest and shortest visit
- Missing-value detection
- Duplicate-row detection
- Average pages per session
- Bounce rate
- Busiest hour
- Most common device
- Device traffic percentages
- Country traffic percentages
- Top pages
- Top countries
- Average duration by page
- Average duration by country
- Average duration by device
- Mean and median visit duration
- Standard deviation
- Quartiles
- IQR-based outlier detection
- Matplotlib visualizations
- Automatic text report generation

## Technologies

This project uses:

- Python
- NumPy
- Pandas
- Matplotlib
- `uv`
- Git and GitHub

The project also uses Python concepts including:

- Functions
- Classes
- Inheritance
- Abstract base classes
- Lists
- Dictionaries
- Sets
- Control flow
- Exception handling
- File handling

## Project Structure

```text
web-analytics/
│
├── README.md
├── pyproject.toml
├── uv.lock
├── generate_data.py
│
├── data/
│   ├── website_events.csv
│   └── website_events_large.csv
│
├── src/
│   └── web_analytics/
│       ├── __init__.py
│       ├── __main__.py
│       ├── loader.py
│       ├── models.py
│       ├── analyzer.py
│       ├── statistics.py
│       ├── plotting.py
│       └── report.py
│
└── tests/
    ├── test_loader.py
    ├── test_analyzer.py
    └── test_statistics.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Mahmoudel3antel/web-analytics.git
```

Enter the project directory:

```bash
cd web-analytics
```

Install the package:

```bash
uv pip install -e .
```

## Running the Analyzer

Run the program with a CSV dataset:

```bash
uv run -m web_analytics data/website_events.csv
```

A larger example dataset can also be analyzed:

```bash
uv run -m web_analytics data/website_events_large.csv
```

A custom output directory can optionally be provided:

```bash
uv run -m web_analytics data/website_events_large.csv results
```

## Input Data Format

The CSV file must contain the following columns:

```text
timestamp
session_id
page
country
device
duration
```

Example:

```csv
timestamp,session_id,page,country,device,duration
2026-09-01 10:00:00,S001,/home,Germany,mobile,35
2026-09-01 10:01:30,S001,/products,Germany,mobile,42
2026-09-01 10:05:00,S002,/home,Egypt,desktop,15
```

The program validates the required columns before starting the analysis.

## Generated Output

The analyzer generates a text report:

```text
output/analytics_report.txt
```

It also creates visualizations:

```text
output/pageviews_by_page.png
output/pageviews_by_country.png
output/device_distribution.png
output/duration_histogram.png
output/pageviews_by_date.png
```

## Example Report

```text
WEBSITE ANALYTICS REPORT
========================================

GENERAL METRICS
----------------------------------------
Total pageviews: 14
Unique sessions: 10
Average duration: 34.21 seconds
Countries: 4
Most visited page: /home
Missing values: 0
Duplicate rows: 0

SESSION METRICS
----------------------------------------
Average pages per session: 1.40
Bounce rate: 60.00%
Busiest hour: 10:00
Top device: mobile

DURATION STATISTICS
----------------------------------------
Mean: 34.21
Median: 26.50
Standard deviation: 28.59
Minimum: 7.00
Maximum: 120.00
25th percentile: 15.75
75th percentile: 40.25
Duration outliers: 1
```

## Dataset Generation

The project includes a script for creating a larger artificial website analytics dataset.

Run:

```bash
uv run python generate_data.py
```

This creates:

```text
data/website_events_large.csv
```

The generated dataset contains multiple sessions, pages, countries, devices, timestamps, and visit durations.

A fixed random seed is used so the generated dataset is reproducible.

## Testing

The project uses Python's built-in `unittest` framework.

Run all tests with:

```bash
uv run python -m unittest discover tests
```

The tests cover:

- Website analytics calculations
- Session metrics
- NumPy statistics
- Outlier detection
- Dataset validation
- Missing required columns
- Invalid file paths

## Architecture

The analysis classes use inheritance.

```text
BaseAnalyzer
    |
    +-- WebsiteAnalyzer
    |
    +-- StatisticsAnalyzer
```

`BaseAnalyzer` defines common analyzer behavior, while the child classes implement specific forms of analysis.

Other components have separate responsibilities:

- `loader.py` — loading and validating datasets
- `analyzer.py` — website and session analytics
- `statistics.py` — numerical analysis
- `plotting.py` — visualization generation
- `report.py` — text report generation
- `__main__.py` — command-line execution

## Author

Mahmoud Mansour