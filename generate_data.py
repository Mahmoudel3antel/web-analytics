import numpy as np
import pandas as pd


def generate_dataset(number_of_sessions=500):
    rng = np.random.default_rng(42)

    pages = [
        "/home",
        "/products",
        "/about",
        "/contact",
        "/pricing",
        "/blog",
    ]

    countries = [
        "Germany",
        "Egypt",
        "France",
        "Spain",
        "Italy",
        "Netherlands",
    ]

    devices = [
        "desktop",
        "mobile",
        "tablet",
    ]

    rows = []

    session_counter = 1

    for _ in range(number_of_sessions):
        session_id = f"S{session_counter:04d}"

        pages_in_session = int(
            rng.integers(1, 6)
        )

        country = rng.choice(countries)
        device = rng.choice(devices)

        start_time = pd.Timestamp("2026-09-01") + pd.Timedelta(
            minutes=int(rng.integers(0, 30 * 24 * 60))
        )

        for page_number in range(pages_in_session):
            timestamp = start_time + pd.Timedelta(
                minutes=page_number * int(rng.integers(1, 6))
            )

            page = rng.choice(pages)

            duration = int(
                rng.normal(
                    loc=45,
                    scale=20,
                )
            )

            duration = max(duration, 3)

            rows.append(
                {
                    "timestamp": timestamp,
                    "session_id": session_id,
                    "page": page,
                    "country": country,
                    "device": device,
                    "duration": duration,
                }
            )

        session_counter += 1

    data = pd.DataFrame(rows)

    return data


def main():
    data = generate_dataset()

    output_path = "data/website_events_large.csv"

    data.to_csv(
        output_path,
        index=False,
    )

    print(f"Generated {len(data)} rows.")
    print(f"Saved dataset to: {output_path}")


if __name__ == "__main__":
    main()