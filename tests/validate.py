import sys
import unittest

from bs4 import BeautifulSoup

from eriparse.parse import parse

expected = {
    "Violent Crime": "26,583",
    "Property Crime": "0",
    "Total Crime": "26,583",
    "Murder": "771",
    "Robbery": "7,869",
    "Assault": "16,597",
    "Burglary": "8,643",
    "Larceny": "0",
    "Vehicle Theft": "10,053",
    "Arson": "636",
    "Total Population:": "2,693,598",
    "Crime Rate:": "0.99%",
    "Total Violent Crime:": "26,583",
    "Violent Crime Rate:": "0.99%",
    "Total Property Crime:": "0",
    "Property Crime Rate:": "0%",
    "The median household income is": "$62,097",
    "The median home price is": "$267,600",
    "State Taxes": "8th highest",
    "Average Salary (Annual)": "$68,738  (USD) Yearly",
    "Average Salary (Hourly)": "$33 (USD) Hourly",
    "Employment Rate per Month": "3,290",
    "Labor Force Count": "2,646,920",
    "Unemployment Rate": "6%",
    "Upward Mobility Rate": "38%",
    "walkability": "NA",
}


if __name__ == "__main__":
    input_ = sys.stdin.read()
    soup = BeautifulSoup(input_, "html.parser")

    unittest.TestCase().assertDictEqual(expected, parse(soup))
