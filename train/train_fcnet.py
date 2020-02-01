import numpy as np
import torch
from torch import nn, optim
from torch.utils import data

from data_loader import LolDataset
from model import FcNet

# gpu
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# data
source = 'data/dataset/processed.json'
lol_dataloader = data.DataLoader(LolDataset(source), batch_size=4, shuffle=True)
# net
net = FcNet(10, 2).to(device)

# loss and optim
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=1e-4)


for epoch in range(2):

    running_loss = 0.0
    for i, data in enumerate(lol_dataloader):
        # data, label
        inputs = data['draft'].to(device)
        labels = data['result'].to(device)

        optimizer.zero_grad()

        outputs = net(inputs.float())
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 200 == 199:
            print('Epoch {}, Step {}, Loss {}'.format(epoch+1, i+1, running_loss/200))
            running_loss = 0.0

print('Finished')
# TODO: 1. split data into train and eval
#       2. add eval part



