import argparse
import json
import os
import sys

from bs4 import BeautifulSoup

from parse import parse


def get_input(parser: argparse.ArgumentParser):
    data = sys.stdin.read()
    return BeautifulSoup(data, "html.parser")
  


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="eri_parser", description="Parsing HTML data from erieri.com")
    
    soup = get_input(parser)

    result = parse(soup)

    sys.stdout.write(json.dumps(result))
