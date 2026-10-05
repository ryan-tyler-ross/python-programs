"""Read a CSV with the standard library and summarize its temperatures."""

import csv
from pathlib import Path


def main():
    path = Path(__file__).with_name("weather_data.csv")
    with path.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
    temperatures = [int(row["temp"]) for row in rows]
    print(f"Average temperature: {sum(temperatures) / len(temperatures):.1f}°C")
    warmest = max(rows, key=lambda row: int(row["temp"]))
    print(f"Warmest day: {warmest['day']} ({warmest['temp']}°C)")


if __name__ == "__main__":
    main()
