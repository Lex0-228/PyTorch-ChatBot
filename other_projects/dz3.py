import random
def CoinCount():
 #3. Гра з монеткою. Монета має 2 грані - орел та решка. Ми підкидаємо монету вгору і отримуємо рандомний результат. Виведіть результат підкидання та порахуйте, скільки разів випаде орел та решка, якщо ми підкинемо монету 100 разів? 1000?
    options = ['орел', 'решка']
    total_number1 = []
    total_number2 = []
    ask = int(input('Скільки разів підкинути монету? :'))
    for i in range(ask):
        x = random.choice(options)
        print(x)
        if x == 'орел':
            total_number1.append(x)
        else:
            total_number2.append(x)
    print('Загальна кількість орлів: '+str(len(total_number1)))
    print('Загальна кількість решок: ' + str(len(total_number2)))