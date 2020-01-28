XPATH_GAME = {

    'matches': "//div[@class='GameItemWrap']",
    'summoners_team_1': './/div[@class="Team"][1]//div[@class="SummonerName"]',
    'summoners_team_2': './/div[@class="Team"][2]//div[@class="SummonerName"]',
    'profile_link': './/a//@href',
    'match_type': './/div[@class="GameType"]//text()',
    'match_result': './/div[@class="GameResult"]//text()',

    'champions_team_1': './/div[@class="Team"][1]//div[@class="ChampionImage"]',
    'champions_team_2': './/div[@class="Team"][2]//div[@class="ChampionImage"]',
    'champion_name': './/div//text()',

    'player': './/div[@class="Information"]/span/text()',
    'timestamp': './/div[@class="TimeStamp"]/span/text()',
    'mmr': './/div[@class="TierRank"]//text()',
}

XPATH_SUMMONER = {
    'summoners': '//a//@href[contains(., "userName")]'
}

SERVERS = ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune', 'las', 'ru']
REGIONS = ['http://' + server + '.op.gg/ranking/ladder/' for server in SERVERS]