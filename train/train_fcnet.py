import time

import numpy as np
import torch
from torch import nn, optim
from torch.utils import data

from data_loader import LolDataset
from model import FcNet
import copy


def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs-1))
        print('-' * 10)

        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()
            else:
                model.eval()
            
            running_loss = 0.0
            running_corrects = 0

            for i, data in enumerate(lol_dataloader[phase]):
                inputs = data['draft'].to(device)
                labels = data['result'].to(device)

                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs.float())
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()
                
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels)
            
            if phase == 'train' and scheduler:
                scheduler.step()
            
            epoch_loss = running_loss / lol_datasize[phase]
            epoch_acc = running_corrects.double() / lol_datasize[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    model.load_state_dict(best_model_wts)
    return model


if __name__ == '__main__':
    # gpu
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # data
    lol_dataloader = {
        x: data.DataLoader(LolDataset('data/dataset/{}.json'.format(x), normal=True), 
                        batch_size=4, shuffle=True)
        for x in ['train', 'val']}
    lol_datasize = {'train': 51121, 'val': 9000}

    # net
    net = FcNet(10, 2).to(device)

    # loss and optim
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=1e-4)

    model_best = train_model(net, criterion, optimizer, scheduler=None, num_epochs=25)
    
