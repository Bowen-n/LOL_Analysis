import requests
from bs4 import BeautifulSoup

url = 'https://www.op.gg/summoner/userName=%ED%9B%88%EB%A0%A8%EB%B3%91%EC%9D%B4%EC%83%81%ED%98%B8'
herohtml = requests.get(url).text
soup = BeautifulSoup(herohtml, 'lxml')

games = soup.find_all('div', class_='GameItemWrap')
games_list = []

for one_game in games:

    using_hero = one_game.find('div', class_='ChampionName').text.strip()
    result = one_game.find('div', class_='GameResult').text.strip()
    game_type = one_game.find('div', class_='GameType').text.strip()
    # Victory Defeat Remake
    if result == 'Remake' and game_type != 'Ranked Solo':
        continue
    
    team_hero = [[], []]

    teams = one_game.find_all('div', class_='Team')

    for i in range(2):
        team = teams[i]
        heroes = team.find_all('div', class_='ChampionImage')
        for hero in heroes:
            hero_name = hero.text.strip().split('\n')[0]
            team_hero[i].append(hero_name)

    team_index = 0 if using_hero in team_hero[0] else 1

    if result == 'Victory':
        team_hero[0], team_hero[1] = team_hero[team_index], team_hero[(team_index+1)%2]
    else: # lose
        team_hero[0], team_hero[1] = team_hero[(team_index+1)%2], team_hero[team_index]

    games_list.append(team_hero)

print(games_list)
print(len(games_list))

