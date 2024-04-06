
# Eriparse
![is_still_valid_workflow](https://github.com/ncgl-git/eriparse/actions/workflows/is_still_valid.yaml/badge.svg)

*HTML parsing logic for `https://www.erieri.com/cost-of-living-calculator`. Was written to help my wife and I better understand the differences between potential cities for her fellowship.*


#### Notes
Be aware that website frontend can change _whenever_ - the badge indicates if the website HTML has changed since this code was written.


## Usage

Intended to be called like: 
```
wget -q https://www.erieri.com/cost-of-living/united-states/illinois/chicago -O - | pipenv run python eriparse/main.py >> chicago.json
```

Or, if you'd like to integrate it into your Python code 

`pip install eriparse`

and then

`from eriparse import parse`

## Tests
The test uses HTML taken from July, 2023.


_Github Actions stops running scheduled jobs if no commits have been pushed after certain period of time. For now, we work around this by modifying the below tally as a dummy commit._

|