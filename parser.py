def PlayNowParser(data):

    homeTeam = {}
    awayTeam = {}
    overUnder = {}

    awayTeam['name'] = data[0]
    homeTeam['name'] = data[1]
    awayTeam['spread'] = data[2]
    homeTeam['spreadOdds'] = data[3]
    awayTeam['spread'] = data[4]
    homeTeam['spreadOdds'] = data[5]
    awayTeam['moneyline'] = data[7]
    homeTeam['moneyline'] = data[9]

    overUnder['over'] = data[11]
    overUnder['overOdds'] = data[12]
    overUnder['under'] = data[14]
    overUnder['underOdds'] = data[15]

    return homeTeam, awayTeam, overUnder


