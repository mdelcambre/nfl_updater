import requests
import re

from helper import get_row_num

SPREAD_URL = "http://www.footballlocks.com/nfl_point_spreads.shtml"

SPREAD_REGEX = re.compile(
        r'<TD>(?:At )?(?P<fav>[a-zA-Z ]+?)</TD>.*?'
        r'<TD>(?P<spr>.+?)</TD>.*?'
        r'<TD>(?:At )?(?P<und>[a-zA-Z ]+?)<')


def get_spread():
    content = request_odds()
    if not content:
        return False
    nfl_odds = parse_response(content)
    if not nfl_odds:
        return False
    return nfl_odds


def request_odds():
    try:
        re = requests.get(SPREAD_URL, timeout=20)
        if not re.ok:
            print("Bad response from bet spread: {}".format(re.status_code))
            return False
        return re.content
    except requests.exceptions.RequestException as err:
        print("Request had error: {}".format(err))
        return False


def parse_response(content):
    content = content.replace('\n','').replace('\r','')
    content = re.sub('<!--.*?-->', "", content)
    week_match = re.search(r'NFL Point Spreads For Week (\d{1,2})', content)
    if not week_match:
        return False
    middle = content.split("NFL Point Spreads For Week")[1]
    spreads = SPREAD_REGEX.findall(middle)
    row_spreads = {
            "week": int(week_match.group(1)),
            "values": [None] * 32
        }
    for spread in spreads:
        fav_row = get_row_num(spread[0])
        und_row = get_row_num(spread[2])
        point = parse_point(spread[1])
        row_spreads['values'][fav_row] = point
        row_spreads['values'][und_row] = abs(point)
    return row_spreads


def parse_point(point_str):
    try:
        point = float(point_str)
        return point
    except ValueError:
        return 0


if __name__ == "__main__":
    print(get_spread())

