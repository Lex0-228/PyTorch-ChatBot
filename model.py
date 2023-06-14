# Цей файл задає структуру нейромережі

import torch.nn as nn

class NeuralNet(nn.Module):
    """Нейромережа з 3 шарів: вхідний ("мішки слів"), прихований, вихідний (відповідний теґ). Задана функція активації - Rectified Linear Unit"""
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        """For-propagation - алгоритм обробки вхідних даних через усі шари до отримання результату"""
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out