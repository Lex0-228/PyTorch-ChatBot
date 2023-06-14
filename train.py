import numpy as np
import json
import torch
import torch.nn as nn
from NLP_functions import bag_of_words, tokenize, stem
from model import NeuralNet
import stopwords_ua_set

with open('json_try#1.json', 'r', encoding='utf-8') as j:
    intents = json.load(j)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

all_words = [stem(w) for w in all_words if w not in stopwords_ua_set.stopwords]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

X_train = torch.from_numpy(np.array(X_train))
y_train = torch.from_numpy(np.array(y_train))

num_epochs = 10000
batch_size = 24 # what is this
learning_rate = 0.1
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)


model = NeuralNet(input_size, hidden_size, output_size)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    words = X_train
    labels = y_train.to(dtype=torch.long) # what is this
    outputs = model(words)
    loss = criterion(outputs, labels)

    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')

data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')
