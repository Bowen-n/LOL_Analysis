import argparse
import json

import lxml
import requests
from lxml import etree

from constants import *


class OpggSpider():

    def __init__(self, path, server='www'):
        ''' server: 'all' for all servers '''
        self.server = server
        if self.server == 'all':
            self.url = REGIONS
        else:
            self.url = ['http://{}.op.gg/ranking/ladder/'.format(server)]
        self.count = 0
        self.file_path = path


    def _parse_profile(self, selector, server):
        for summoner in selector:
            link = summoner.xpath(XPATH_GAME['profile_link'])
            link = "http:" + link[0]
            self._parse_games(link, server, first_flag=False)


    def _parse_champions(self, selector):
        team = []
        for champion in selector:
            name = champion.xpath(XPATH_GAME['champion_name'])[0]
            team.append(name)
        return team


    def _parse_games(self, url, server, first_flag=False):
        response = etree.HTML(requests.get(url=url).text)
        matches = response.xpath(XPATH_GAME['matches'])
            
        for match in matches:
            # crawl in summoners url
            summoners_t1 = match.xpath(XPATH_GAME['summoners_team_1'])
            summoners_t2 = match.xpath(XPATH_GAME['summoners_team_2'])
            if first_flag:
                self._parse_profile(summoners_t1, server)
                self._parse_profile(summoners_t2, server)
                
            # only crawl Ranked Solo
            # pass Remake
            match_type = match.xpath(XPATH_GAME['match_type'])[0].strip()
            match_result = match.xpath(XPATH_GAME['match_result'])[0].strip()
            if match_type != 'Ranked Solo' or match_result == 'Remake':
                continue
        
            # get hero names
            champion_t1 = match.xpath(XPATH_GAME['champions_team_1'])
            champion_t2 = match.xpath(XPATH_GAME['champions_team_2'])
            team_1 = self._parse_champions(champion_t1)
            team_2 = self._parse_champions(champion_t2)
                
            player = response.xpath(XPATH_GAME['player'])[0]
            players_t1 = [summoner.xpath('.//a//text()')[0] for summoner in summoners_t1]

            # store info
            item = {}
            item['team_1'] = team_1
            item['team_2'] = team_2

            if player in players_t1:
                item['result'] = 'Victory' if match_result == 'Victory' else 'Defeat'
            else:
                item['result'] = 'Victory' if match_result == 'Defeat' else 'Defeat'

            mmr = response.xpath(XPATH_GAME['mmr'])
            item['mmr'] = mmr[0] if len(mmr) > 0 else 'None'
            item['timestamp'] = match.xpath(XPATH_GAME['timestamp'])[0]
            item['server'] = server

            # json_str = json.dumps(item)
            # readed = json.load(open('dataset/opgg.json', 'r'))

            if self.count == 0:
                item_as_list = [item]
                with open(self.file_path, 'w') as f:
                    json.dump(item_as_list, f, indent=1)
                    self.count += 1
                    print(self.count)
            else:
                with open(self.file_path, 'r') as f:
                    data_list = json.load(f)
                data_list.append(item)
                with open(self.file_path, 'w') as f:
                    json.dump(data_list, f, indent=1)
                    self.count += 1
                    print(self.count)



    def parse(self):

        for url in self.url:
            if self.server == 'all':
                server = SERVERS[self.url.index(url)]
            else:
                server = self.server

            response = etree.HTML(requests.get(url=url).text)
            summoners = response.xpath(XPATH_SUMMONER['summoners'])
            for summoner in summoners:
                summoner_url = 'http:{}'.format(summoner)
                self._parse_games(summoner_url, server=server, first_flag=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='the path of file to store data')
    args = parser.parse_args()

    opgg_spider = OpggSpider(server='www', path=args.path)
    opgg_spider.parse()


if __name__ == '__main__':
    main()   
