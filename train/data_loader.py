import json
import torch
from torch.utils import data
import numpy as np


class LolDataset(data.Dataset):
    ''' Lol dataset crawled from op.gg'''
    
    def __init__(self, json_file, normal=True):
        with open(json_file, 'r') as f:
            self.lol_data = json.load(f)
        self.normal = normal
    
    def __len__(self):
        return len(self.lol_data)
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        data = self.lol_data[idx]
        features = (data['team_1'] + data['team_2'])
        

        return {
            'draft': torch.from_numpy(np.asarray(features)/148) if self.normal else torch.from_numpy(np.asarray(features)),
            'result': torch.tensor(data['result'])}


def data_loader(source):
    with open(source, 'r') as f:
        data = json.load(f)
        print(data)


if __name__ == '__main__':
    source = 'data/dataset/processed.json'
    lol_data = LolDataset(source)
    dataloader = data.DataLoader(lol_data, batch_size=4, shuffle=True)
    for i_batch, sample_batched in enumerate(dataloader):
        print(i_batch, sample_batched['draft'], sample_batched['result'])
        break
