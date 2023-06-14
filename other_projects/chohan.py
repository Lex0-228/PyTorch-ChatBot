import random
import time

def ChoHan():
    while 1 > 0:
        number = int(input('丁半 game！\nSet the number of players (up to 6): '))
        if number <= 1:
            print('From 2 to 6, come on!')
            continue
        else:
            if number > 6:
                print('From 2 to 6, come on!')
                continue
            else:
                break

    list_players = []
    for i in range(1, number + 1):
        list_players.append('player' + str(i))
    # ask = input('Do you want to play against the computer? (yes/no):')
    player1_total = 1000
    # if ask == 'yes':
    while 0 < 1:
        correct_answers = ['cho', 'han']
        choice = ''
        while choice not in correct_answers:
            choice = input('\nLet the game begin!\n\nDo you want to bet on CHO or HAN? : ')
        print('Your current number of points is ' + str(player1_total))
        while 1 > 0:
            bet = int(input('How many points do you want to bet? :'))
            if bet > player1_total:
                print('You don\'t have that many points!')
                continue
            else:
                if bet < 0:
                    print('Are you trynna mess with me?')
                    continue
                else:
                    break
        if choice in correct_answers:
            choice_list = []
            bets_list = []
            bets_list.append(bet)
            choice_list.append(choice)
            print('\n--------------------\n' + 'Your bet is ' + str(bet) + ' on ' + str(choice))
            for i in list_players[1:]:
                bets_list.append(random.randint(100, 1000))
                choice_list.append(random.choice(correct_answers))
                print(i + ' bets ' + str(bets_list[-1]) + ' on ' + str(choice_list[-1]))
            print('--------------------')
            data = dict(zip(choice_list, bets_list))
            losing_bet = 0
            winning_bet = 0
            time.sleep(1)
            n = 3
            while n > 0:
                print(n)
                time.sleep(1)
                n -= 1
            print('🎲\n--------------------')
            dice = ['  — — — —\n|         |\n|    🛑    |\n|         |\n  — — — —',
                    '  — — — —\n|    🛑   |\n|         |\n|    🛑   |\n  — — — —',
                    ' — — — —\n|🛑      |\n|   🛑   |\n|      🛑|\n — — — —',
                    '  — — — —\n|🛑     🛑|\n|        |\n|🛑     🛑|\n  — — — —',
                    '  — — — —\n|🛑     🛑|\n|   🛑    |\n|🛑     🛑|\n  — — — —',
                    ' — — — —\n|🛑    🛑|\n|🛑    🛑|\n|🛑    🛑|\n — — — —']
            result1, result2 = random.choice(dice), random.choice(dice)
            whole_number = result1.count('🛑') + result2.count('🛑')
            print(result1)
            print(result2)
            total = 'cho' if (whole_number) % 2 == 0 else 'han'
            print(str(whole_number) + ' - ' + total + '!')
            for key in data:
                losing_bet += data[key] if key != total else 0
                winning_bet += data[key] if key == total else 0
            try:
                player1_result = round(
                    (100 * bet / (winning_bet / 100 * 95)) * (losing_bet / 100)) if choice == total else -1 * bet
            except:
                player1_result = 0
                print('No one won! Dealer grabs your bets >:)')
            player1_total += player1_result
            print('--------------------')
            print('Your result is ', player1_result)
            if player1_total <= 0:
                print('Game over! You\'ve run out of points :( ')
            else:
                print('Your current total number of points: ' + str(player1_total))
                continue_ = input('Do you want to continue? (yes/no):')
                print('--------------------')
                if continue_ == 'yes':
                    continue
                else:
                    break


