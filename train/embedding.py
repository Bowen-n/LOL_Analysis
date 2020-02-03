from utils import get_champion_names
import torch
import torch.nn as nn

cham_list = get_champion_names()
cham_to_id = {champion: cham_list.index(champion) for champion in cham_list}
embeds = nn.Embedding(148, 5)
lookup = torch.tensor([cham_to_id['Ezreal']], dtype=torch.long)
ezreal_embed = embeds(lookup)
print(ezreal_embed)