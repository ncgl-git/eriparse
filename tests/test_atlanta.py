import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestAtlanta(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/atlanta.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("4,609", result["Violent Crime"])

    def test_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("19,154", result["Property Crime"])

    def test_total_crime(self):
        result = parse(self.soup)

        self.assertEqual("23,763", result["Total Crime"])

    def test_murder(self):
        result = parse(self.soup)

        self.assertEqual("159", result["Murder"])

    def test_robbery(self):
        result = parse(self.soup)

        self.assertEqual("835", result["Robbery"])

    def test_assault(self):
        result = parse(self.soup)

        self.assertEqual("3,465", result["Assault"])

    def test_burglary(self):
        result = parse(self.soup)

        self.assertEqual("1,689", result["Burglary"])

    def test_larceny(self):
        result = parse(self.soup)

        self.assertEqual("14,272", result["Larceny"])

    def test_vehicle_theft(self):
        result = parse(self.soup)

        self.assertEqual("3,193", result["Vehicle Theft"])

    def test_arson(self):
        result = parse(self.soup)

        self.assertEqual("13", result["Arson"])

    def test_total_population(self):
        result = parse(self.soup)

        self.assertEqual("521,274", result["Total Population:"])

    def test_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("4.56%", result["Crime Rate:"])

    def test_total_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("4,609", result["Total Violent Crime:"])

    def test_violent_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0.88%", result["Violent Crime Rate:"])

    def test_total_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("19,154", result["Total Property Crime:"])

    def test_property_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("3.67%", result["Property Crime Rate:"])

    def test_the_median_household_income_is(self):
        result = parse(self.soup)

        self.assertEqual("$64,179", result["The median household income is"])

    def test_the_median_home_price_is(self):
        result = parse(self.soup)

        self.assertEqual("$314,400", result["The median home price is"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("14th highest", result["State Taxes"])

    def test_average_salary_annual(self):
        result = parse(self.soup)

        self.assertEqual("$62,388  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_salary_hourly(self):
        result = parse(self.soup)

        self.assertEqual("$30 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_employment_rate_per_month(self):
        result = parse(self.soup)

        self.assertEqual("902", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("516,376", result["Labor Force Count"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("5%", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("33.1%", result["Upward Mobility Rate"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
