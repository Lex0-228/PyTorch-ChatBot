import random
import json
import torch
from model import NeuralNet
from NLP_functions import bag_of_words, tokenize
from bot_classes import Solver, log_print
import sys

with open('json_try#1.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()


class ChatBot:

    def __init__(self, name = "Розум'ян", expected_request = ['greetings'], sentence = '', last_answer = ''):
        self.name = name
        self.expected_request = expected_request
        self.sentence = sentence
        self.last_answer = last_answer


    def input_request(self) -> str:
        self.sentence = input("You: ")
        return self.sentence


    def generate_answer(self):
        sentence = self.sentence
        expected_request = self.expected_request
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])  # what is this
        X = torch.from_numpy(X)
        output = model(X)
        _, predicted = torch.max(output, dim=1)
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        answer_probability = prob.item()
        tag = tags[predicted.item()]
        if answer_probability > 0.75:
            for intent in intents['intents']:
                    if tag == intent["tag"]:
                        if tag in expected_request:
                            self.last_answer = tag
                            log_print(f"Розум'ян: {random.choice(intent['responses'])}".format(format_on='\033[91m', format_off='\033[00m'))
        else:
            log_print(f"Розум'ян: Не зовсім зрозумів твій запит...")


    def state_changer(self):
        state1 = ['question', 'bye']
        state2 = ['bye', 'physics', 'mathematics', 'geography', 'linguistics', 'work with text', 'miscellaneous', 'other projects']
        state3 = ['physics', 'mathematics', 'geography', 'linguistics', 'work with text', 'miscellaneous', 'other projects']
        state4 = [intent['tag'] for intent in intents['intents'] if intent['tag'].startswith(self.last_answer)]

        if self.last_answer == 'greetings':
            self.expected_request = state1

        elif self.last_answer == 'question':
            self.expected_request = state2

        elif self.last_answer == 'thanks':
            self.expected_request = state2

        elif self.last_answer in state3:
            self.expected_request = state4

        elif self.last_answer == 'bye':
            sys.exit("")

        elif self.last_answer in state4:
            f = Solver(self.last_answer)
            f.solve()
            self.expected_request = [tag for tag in tags]


    def function(self):
        log_print("Нумо спілкуватися! Бот може давати відповіді на поставлені питання з кількох тем, але він любить ввічливість. Щоб зав'язалася розмова, спочатку привітайтеся, потім запитайте, \nщо він знає або уміє. Для завершення програми попрощайтеся або напишіть 'Вихід'")
        while True:
            self.state_changer()
            self.input_request()
            self.generate_answer()



if __name__ == "__main__":
    Bot = ChatBot()
    Bot.function()