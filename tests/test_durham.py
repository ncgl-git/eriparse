import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestDurham(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/durham.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("2,160", result["Violent Crime"])

    def test_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("9,674", result["Property Crime"])

    def test_total_crime(self):
        result = parse(self.soup)

        self.assertEqual("11,834", result["Total Crime"])

    def test_murder(self):
        result = parse(self.soup)

        self.assertEqual("47", result["Murder"])

    def test_robbery(self):
        result = parse(self.soup)

        self.assertEqual("546", result["Robbery"])

    def test_assault(self):
        result = parse(self.soup)

        self.assertEqual("1,442", result["Assault"])

    def test_burglary(self):
        result = parse(self.soup)

        self.assertEqual("1,494", result["Burglary"])

    def test_larceny(self):
        result = parse(self.soup)

        self.assertEqual("7,417", result["Larceny"])

    def test_vehicle_theft(self):
        result = parse(self.soup)

        self.assertEqual("763", result["Vehicle Theft"])

    def test_arson(self):
        result = parse(self.soup)

        self.assertEqual("36", result["Arson"])

    def test_total_population(self):
        result = parse(self.soup)

        self.assertEqual("291,962", result["Total Population:"])

    def test_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("4.05%", result["Crime Rate:"])

    def test_total_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("2,160", result["Total Violent Crime:"])

    def test_violent_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0.74%", result["Violent Crime Rate:"])

    def test_total_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("9,674", result["Total Property Crime:"])

    def test_property_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("3.31%", result["Property Crime Rate:"])

    def test_the_median_household_income_is(self):
        result = parse(self.soup)

        self.assertEqual("$61,962", result["The median household income is"])

    def test_the_median_home_price_is(self):
        result = parse(self.soup)

        self.assertEqual("$243,000", result["The median home price is"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("18th highest", result["State Taxes"])

    def test_average_salary_annual(self):
        result = parse(self.soup)

        self.assertEqual("$64,100  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_salary_hourly(self):
        result = parse(self.soup)

        self.assertEqual("$31 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_employment_rate_per_month(self):
        result = parse(self.soup)

        self.assertEqual("341", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("155,722", result["Labor Force Count"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("5%", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("33.6%", result["Upward Mobility Rate"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
