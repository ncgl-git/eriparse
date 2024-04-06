import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestChicago(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/chicago.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("26,583", result["Violent Crime"])

    def test_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("0", result["Property Crime"])

    def test_total_crime(self):
        result = parse(self.soup)

        self.assertEqual("26,583", result["Total Crime"])

    def test_murder(self):
        result = parse(self.soup)

        self.assertEqual("771", result["Murder"])

    def test_robbery(self):
        result = parse(self.soup)

        self.assertEqual("7,869", result["Robbery"])

    def test_assault(self):
        result = parse(self.soup)

        self.assertEqual("16,597", result["Assault"])

    def test_burglary(self):
        result = parse(self.soup)

        self.assertEqual("8,643", result["Burglary"])

    def test_larceny(self):
        result = parse(self.soup)

        self.assertEqual("0", result["Larceny"])

    def test_vehicle_theft(self):
        result = parse(self.soup)

        self.assertEqual("10,053", result["Vehicle Theft"])

    def test_arson(self):
        result = parse(self.soup)

        self.assertEqual("636", result["Arson"])

    def test_total_population(self):
        result = parse(self.soup)

        self.assertEqual("2,693,598", result["Total Population:"])

    def test_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0.99%", result["Crime Rate:"])

    def test_total_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("26,583", result["Total Violent Crime:"])

    def test_violent_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0.99%", result["Violent Crime Rate:"])

    def test_total_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("0", result["Total Property Crime:"])

    def test_property_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0%", result["Property Crime Rate:"])

    def test_the_median_household_income_is(self):
        result = parse(self.soup)

        self.assertEqual("$62,097", result["The median household income is"])

    def test_the_median_home_price_is(self):
        result = parse(self.soup)

        self.assertEqual("$267,600", result["The median home price is"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("8th highest", result["State Taxes"])

    def test_average_salary_annual(self):
        result = parse(self.soup)

        self.assertEqual("$68,023  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_salary_hourly(self):
        result = parse(self.soup)

        self.assertEqual("$33 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_employment_rate_per_month(self):
        result = parse(self.soup)

        self.assertEqual("3,290", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("2,646,920", result["Labor Force Count"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("6%", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("38%", result["Upward Mobility Rate"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
