import json

from champion_names import get_champion_names


def data_process(path):
    ''' convert champion name to onehot number '''
    champions = get_champion_names()
    game_count = 0

    with open('dataset\data\opgg.json') as json_f:

        game_list = json.load(json_f)
        for game in game_list:
            item = {}
            item['result'] = 1 if game['result'] == 'Victory' else 0
            item['team_1'] = []; item['team_2'] = []
            for champion_t1 in game['team_1']:
                c_index = champions.index(champion_t1)
                item['team_1'].append(c_index)
            for champion_t2 in game['team_2']:
                c_index = champions.index(champion_t2)
                item['team_2'].append(c_index)
            
            if game_count == 0:
                item_as_list = [item]
                with open(path, 'w') as f:
                    json.dump(item_as_list, f, indent=1)
                    game_count += 1

            else:
                with open(path, 'r') as f:
                    data_list = json.load(f)
                data_list.append(item)
                with open(path, 'w') as f:
                    json.dump(data_list, f, indent=1)
                    game_count += 1
            
            if game_count % 200 == 0:
                print(game_count)


if __name__ == '__main__':
    target_path = 'dataset\data\processed.json'
    data_process(target_path)
    print('Succeed')