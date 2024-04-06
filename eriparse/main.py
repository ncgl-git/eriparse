import json
import sys

from bs4 import BeautifulSoup

from eriparse.parse import parse

if __name__ == "__main__":
    input_ = sys.stdin.read()
    soup = BeautifulSoup(input_, "html.parser")
    result = parse(soup)
    output = json.dumps(result)
    sys.stdout.write(output)
