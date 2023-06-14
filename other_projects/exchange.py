
def CurrencyExchange():
    options_list = [1, 2, 3]
    currency_in = None
    currency_out = None
    while currency_in not in options_list:
        currency_in = int(input('Виберіть вхідну валюту: 1 - українська гривня (UAN), 2 - долар США (USD), 3 -  японська єна (JPY)\n'))
        if currency_in in options_list:
            break
        else:
            print('Будь ласка, виберіть номер із запропонованих')
            continue
    while currency_out not in options_list:
        currency_out = int(input('Виберіть вихідну валюту: 1 - українська гривня (UAN), 2 - долар США (USD), 3 -  японська єна (JPY)\n'))
        if currency_out in options_list:
            break
        else:
            print('Будь ласка, виберіть номер із запропонованих')
            continue
    if currency_in == currency_out:
        print('Помилка')
        raise SystemExit(0)

    money = float(input('Введіть суму:'))
    if currency_in == 1:
        if currency_out == 2:
            print('За курсом станом на 14.06.2023:  ' +  str(money*0.027) + 'USD' )
        else:
            print('За курсом станом на 14.06.2023:  ' + str(money * 0.26) + 'JPY')
    elif currency_in == 2:
        if currency_out == 1:
            print('За курсом станом на 14.06.2023:  ' + str(money*36.94) + 'UAN')
        else:
            print('За курсом станом на 14.06.2023:  ' + str(money * 142.60) + 'JPY')
    else:
        if currency_out == 1:
            print('За курсом станом на 14.06.2023:  ' + str(money*3.86) + 'UAN')
        else:
            print('За курсом станом на 14.06.2023:  ' + str(money * 0.0070) + 'USD')
