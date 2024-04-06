import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestCharlottesville(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/charlottesville.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("229", result["Violent Crime"])

    def test_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("1,218", result["Property Crime"])

    def test_total_crime(self):
        result = parse(self.soup)

        self.assertEqual("1,447", result["Total Crime"])

    def test_murder(self):
        result = parse(self.soup)

        self.assertEqual("0", result["Murder"])

    def test_robbery(self):
        result = parse(self.soup)

        self.assertEqual("34", result["Robbery"])

    def test_assault(self):
        result = parse(self.soup)

        self.assertEqual("162", result["Assault"])

    def test_burglary(self):
        result = parse(self.soup)

        self.assertEqual("125", result["Burglary"])

    def test_larceny(self):
        result = parse(self.soup)

        self.assertEqual("944", result["Larceny"])

    def test_vehicle_theft(self):
        result = parse(self.soup)

        self.assertEqual("149", result["Vehicle Theft"])

    def test_arson(self):
        result = parse(self.soup)

        self.assertEqual("2", result["Arson"])

    def test_total_population(self):
        result = parse(self.soup)

        self.assertEqual("47,257", result["Total Population:"])

    def test_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("3.06%", result["Crime Rate:"])

    def test_total_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("229", result["Total Violent Crime:"])

    def test_violent_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0.48%", result["Violent Crime Rate:"])

    def test_total_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("1,218", result["Total Property Crime:"])

    def test_property_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("2.58%", result["Property Crime Rate:"])

    def test_the_median_household_income_is(self):
        result = parse(self.soup)

        self.assertEqual("$59,598", result["The median household income is"])

    def test_the_median_home_price_is(self):
        result = parse(self.soup)

        self.assertEqual("$329,100", result["The median home price is"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("7th highest", result["State Taxes"])

    def test_average_salary_annual(self):
        result = parse(self.soup)

        self.assertEqual("$61,099  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_salary_hourly(self):
        result = parse(self.soup)

        self.assertEqual("$29 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_employment_rate_per_month(self):
        result = parse(self.soup)

        self.assertEqual("17", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("24,264", result["Labor Force Count"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("3%", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("34.5%", result["Upward Mobility Rate"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
