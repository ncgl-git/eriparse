import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestPhiladelphia(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/philadelphia.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_the_median_household_income_is(self):
        result = parse(self.soup)

        self.assertEqual("$49,127", result["The median household income is"])

    def test_the_median_home_price_is(self):
        result = parse(self.soup)

        self.assertEqual("$171,600", result["The median home price is"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("25th highest", result["State Taxes"])

    def test_average_salary_annual(self):
        result = parse(self.soup)

        self.assertEqual("$67,586  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_salary_hourly(self):
        result = parse(self.soup)

        self.assertEqual("$32 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_employment_rate_per_month(self):
        result = parse(self.soup)

        self.assertEqual("976", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("687,722", result["Labor Force Count"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("5%", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("37.1%", result["Upward Mobility Rate"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
