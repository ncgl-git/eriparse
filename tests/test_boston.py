import pathlib
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse


class TestBoston(unittest.TestCase):
    path_data = pathlib.PurePath("./tests/data/boston.html")

    def setUp(self) -> None:
        with open(self.path_data, "rb") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def test_arson(self):
        result = parse(self.soup)

        self.assertEqual("26", result["Arson"])

    def test_assault(self):
        result = parse(self.soup)

        self.assertEqual("2,855", result["Assault"])

    def test_average_salary_annual(self):
        result = parse(self.soup)

        self.assertEqual("$73,314  (USD) Yearly", result["Average Salary (Annual)"])

    def test_average_salary_hourly(self):
        result = parse(self.soup)

        self.assertEqual("$35 (USD) Hourly", result["Average Salary (Hourly)"])

    def test_burglary(self):
        result = parse(self.soup)

        self.assertEqual("1,342", result["Burglary"])

    def test_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("2.2%", result["Crime Rate:"])

    def test_employment_rate_per_month(self):
        result = parse(self.soup)

        self.assertEqual("-163", result["Employment Rate per Month"])

    def test_labor_force_count(self):
        result = parse(self.soup)

        self.assertEqual("412,498", result["Labor Force Count"])

    def test_larceny(self):
        result = parse(self.soup)

        self.assertEqual("9,118", result["Larceny"])

    def test_murder(self):
        result = parse(self.soup)

        self.assertEqual("36", result["Murder"])

    def test_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("11,614", result["Property Crime"])

    def test_property_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("1.65%", result["Property Crime Rate:"])

    def test_robbery(self):
        result = parse(self.soup)

        self.assertEqual("771", result["Robbery"])

    def test_state_taxes(self):
        result = parse(self.soup)

        self.assertEqual("9th highest", result["State Taxes"])

    def test_the_median_home(self):
        result = parse(self.soup)

        self.assertEqual("$581,200", result["The median home price is"])

    def test_the_median_income(self):
        result = parse(self.soup)

        self.assertEqual("$76,298", result["The median household income is"])

    def test_total_crime(self):
        result = parse(self.soup)

        self.assertEqual("15,499", result["Total Crime"])

    def test_total_population(self):
        result = parse(self.soup)

        self.assertEqual("704,758", result["Total Population:"])

    def test_total_property_crime(self):
        result = parse(self.soup)

        self.assertEqual("11,614", result["Total Property Crime:"])

    def test_total_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("3,885", result["Total Violent Crime:"])

    def test_unemployment_rate(self):
        result = parse(self.soup)

        self.assertEqual("4%", result["Unemployment Rate"])

    def test_upward_mobility_rate(self):
        result = parse(self.soup)

        self.assertEqual("39.8%", result["Upward Mobility Rate"])

    def test_vehicle_theft(self):
        result = parse(self.soup)

        self.assertEqual("1,154", result["Vehicle Theft"])

    def test_violent_crime(self):
        result = parse(self.soup)

        self.assertEqual("3,885", result["Violent Crime"])

    def test_violent_crime_rate(self):
        result = parse(self.soup)

        self.assertEqual("0.55%", result["Violent Crime Rate:"])

    def test_walkability(self):
        result = parse(self.soup)

        self.assertEqual("NA", result["walkability"])
