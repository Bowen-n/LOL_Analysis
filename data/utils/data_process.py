import json

from champion_names import get_champion_names


def data_process(source, target):
    ''' convert champion name to onehot number '''
    champions = get_champion_names()

    out_list = []

    with open(source) as json_f:

        game_count = 0
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
            
            out_list.append(item)
            game_count += 1

            if game_count % 200 == 0:
                print(game_count)
        
    with open(target, 'w') as f:
        json.dump(out_list, f, indent=1)


if __name__ == '__main__':
    source_path = 'data/dataset/opgg.json'
    target_path = 'data/dataset/processed.json'
    data_process(source_path, target_path)
    print('Succeed')