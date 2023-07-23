import re
from typing import Any, Dict, Generator

from bs4 import BeautifulSoup, ResultSet

__all__ = [
    "parse_crime_data",
    "parse_crime_chart",
    "parse_area_data",
    "parse_employment_data",
    "parse",
]


def _pull_class(s: BeautifulSoup, class_name: str) -> Generator[ResultSet[Any], None, None]:
    for class_ in s.findAll("div", {"class": class_name}):
        yield class_


def _pull_divs(class_: ResultSet[Any]) -> Generator[ResultSet[Any], None, None]:
    for div in class_.findAll("div"):
        yield div


def _pull_spans(class_: ResultSet[Any]) -> Generator[ResultSet[Any], None, None]:
    for span in class_.findAll("span"):
        yield span


def _pull_headers(class_: ResultSet[Any]) -> Generator[ResultSet[Any], None, None]:
    header_pattern = re.compile("^h[1-6]$")
    for header in class_.findAll(header_pattern):
        yield header


def parse_crime_data(s: BeautifulSoup) -> Dict[str, str]:
    results = {}
    for data in _pull_class(s, "crime-header"):
        for span in _pull_spans(data):
            if span.attrs.get("class") == ["crime-header-label"]:
                header = span.getText()
            elif span.attrs.get("class") == ["crime-header-value"]:
                results[header] = span.getText()
    return results


def parse_crime_chart(s: BeautifulSoup) -> Dict[str, str]:
    results = {}
    for data in _pull_class(s, "crime-chart"):
        for div in _pull_divs(data):
            if div.attrs.get("class") == ["crime-header-label"]:
                header = div.getText()
            elif "local" in div.attrs.get("class", []):
                results[header] = div.getText()
    return results


def parse_area_data(s: BeautifulSoup) -> Dict[str, str]:
    results = {}
    for data in _pull_class(s, "area-information-section"):
        for div in _pull_divs(data):
            if div.attrs.get("class") == ["description"]:
                header = div.getText()
            elif "data-label" in div.attrs.get("class", []):
                results[header] = div.getText()

        for header in _pull_headers(data):
            if "comparison-data-label" in header.attrs.get("class", []):
                results["State Taxes"] = header.getText()

        for span in _pull_spans(data):
            if span.attrs.get("class") == ["annual-container"]:
                results["Average Salary (Annual)"] = span.getText()

            elif span.attrs.get("class") == ["hourly-container"]:
                results["Average Salary (Hourly)"] = span.getText()

    return results


def parse_walk_data(s: BeautifulSoup) -> Dict[str, str]:
    for data in _pull_class(s, "walk-score-section"):
        if walk := data.find(id="lblWalkScore"):
            return {"walkability": walk.getText().strip()}
    return {}


def parse_employment_data(s: BeautifulSoup) -> Dict[str, str]:
    results = {}
    for data in _pull_class(s, "employment-levels-section"):
        headers = list(_pull_headers(data))

        # skipping the first entry, hence 1 and 2 instead of 0 and 1
        for header, value in zip(headers[1::2], headers[2::2], strict=True):
            results[header.getText()] = value.getText()

    return results


def parse(s: BeautifulSoup):
    return {
        **parse_crime_chart(s),
        **parse_crime_data(s),
        **parse_area_data(s),
        **parse_employment_data(s),
        **parse_walk_data(s),
    }
