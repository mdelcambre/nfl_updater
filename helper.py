


def get_row_num(name):
    try:
        try:
            name = REDUCED[name]
        except KeyError:
            pass
        row_num = ROW_NUM[name]
        return row_num
    except KeyError as err:
        print("Can't find team name {}".format(name))
        return False


REDUCED = {
        "Arizona": "ARI", "ARZ": "ARI",
        "Atlanta": "ATL",
        "Baltimore": "BAL",
        "Buffalo": "BUF",
        "Carolina": "CAR",
        "Chicago": "CHI",
        "Cincinnati": "CIN",
        "Cleveland": "CLE",
        "Dallas": "DAL",
        "Denver": "DEN",
        "Detroit": "DET",
        "Green Bay": "GB",
        "Houston": "HOU",
        "Indianapolis": "IND",
        "Jacksonville": "JAX",
        "Kansas City": "KC",
        "Los Angeles": "LA",
        "Miami": "MIA",
        "Minnesota": "MIN",
        "New England": "NE",
        "New Orleans": "NO",
        "NY Giants": "NYG",
        "NY Jets": "NYJ",
        "Oakland": "OAK",
        "Philadelphia": "PHI",
        "Pittsburgh": "PIT",
        "San Diego": "SD",
        "Seattle": "SEA",
        "San Francisco": "SF",
        "Tampa Bay": "TB",
        "Tennessee": "TEN",
        "Washington": "WSH"
}

ROW_NUM = {
        "ARI": 0,
        "ATL": 1,
        "BAL": 2,
        "BUF": 3,
        "CAR": 4,
        "CHI": 5,
        "CIN": 6,
        "CLE": 7,
        "DAL": 8,
        "DEN": 9,
        "DET": 10,
        "GB": 11,
        "HOU": 12,
        "IND": 13,
        "JAX": 14,
        "KC": 15,
        "LA": 16,
        "MIA": 17,
        "MIN": 18,
        "NE": 19,
        "NO": 20,
        "NYG": 21,
        "NYJ": 22,
        "OAK": 23,
        "PHI": 24,
        "PIT": 25,
        "SD": 26,
        "SEA": 27,
        "SF": 28,
        "TB": 29,
        "TEN": 30,
        "WSH": 31,
}
