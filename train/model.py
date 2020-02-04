import torch
from torch import nn, optim
import torch.nn.functional as F
import numpy as np

class FcNet(nn.Module):
    def __init__(self, input_size, num_classes):
        super(FcNet, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 32)
        self.fc3 = nn.Linear(32, num_classes)
        self.softmax = nn.Softmax()

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = self.softmax(x)
        return x


class FcNet_Emb(nn.Module):
    def __init__(self, embed_size, num_classes):
        super(FcNet_Emb, self).__init__()
        self.embedding = nn.Embedding(148, embed_size)
        self.fc1 = nn.Linear(10*embed_size, 128)
        self.fc2 = nn.Linear(128, 32)
        self.fc3 = nn.Linear(32, num_classes)
        self.softmax = nn. Softmax()
    
    def forward(self, x):
        x = self.embedding(x)
        x = x.view(x.size(0), x.size(1)*x.size(2))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.softmax(self.fc3(x))
        return x

