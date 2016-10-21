import json
import requests
from helper import get_row_num


SCORES = "http://api.foxsports.com/sportsdata/v1/football/nfl/events.json?"\
        + "season=2016&seasontype=reg&week={}&"\
        + "apikey=jE7yBJVRNAwdDesMgTzTXUUSx1It41Fq"

def get_all_scores():
    all_scores= []
    for week in range(1,18):
       all_scores.append(get_scores(week))
    return all_scores

def get_scores(week):
    json_str = get_json(week)
    if not json_str:
        return False
    return get_row_scores(json_str, week)


def get_json(week):
    try:
        re = requests.get(SCORES.format(week), timeout=15)
        if not re.ok:
            return False
        return json.loads(re.content)
    except requests.exceptions.RequestException as err:
        return False

def get_row_scores(score_dict, week):
    row_scores = [""] * 32
    for game in score_dict['page']:
        try:
            home = game['homeTeam']['abbreviation']
            away = game['awayTeam']['abbreviation']
            home_score = game['score']['homeScore']
            away_score = game['score']['awayScore']
            row_scores[get_row_num(home)] = home_score - away_score
            row_scores[get_row_num(away)] = away_score - home_score
        except KeyError as err:
            row_scores[get_row_num(home)] = ""
            row_scores[get_row_num(away)] = ""
    return row_scores


if __name__ == "__main__":
    print(get_all_scores())

