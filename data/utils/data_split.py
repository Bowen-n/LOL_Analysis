import json
import os

def train_val_split(source, target):
    ''' split data into train and val '''
    with open(source) as json_f:
        game_list = json.load(json_f)
        val = game_list[0:9000]
        train = game_list[9000:]
    
    with open(os.path.join(target, 'train.json'), 'w') as f:
        json.dump(train, f, indent=1)
    with open(os.path.join(target, 'val.json'), 'w') as f:
        json.dump(val, f, indent=1)
    


if __name__ == '__main__':
    source = 'data/dataset/processed.json'
    target = 'data/dataset'
    train_val_split(source, target)