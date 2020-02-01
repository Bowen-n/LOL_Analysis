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