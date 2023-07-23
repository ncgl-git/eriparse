import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestBaltimore(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/baltimore.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_median_income(self):
        result = parse(self.soup)

        self.assertEqual("$52,164", result["The median household income is"])

    def test_median_home_price(self):
        result = parse(self.soup)

        self.assertEqual("$167,300", result["The median home price is"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("17th highest", result["State Taxes"])

    def test_average_annual_salary(self):
        result = parse(self.soup)

        self.assertEqual("$67,579  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_hourly_salary(self):
        result = parse(self.soup)

        self.assertEqual("$32 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_employment_rate(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["Labor Force Count"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("33.8%", result["Upward Mobility Rate"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
