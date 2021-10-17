from random import randrange
from gamedata import data
a = data()
print("This is my first program\n #######lottery game#######")
p = True
while p:
    entry = input("put 'y' to continue or type 'n' to out:\n")
    if entry=='y':
        print("welcome from the game")
        id = int(input("Enter your Id: "))
        if id in range(111,131):
            money = a.list[id]
            print('This is your money',money)
            while money > 100:
                usemoney = int(input('Enter the amount of money to play lottery.\nmust be more than 200:\n'))
                if usemoney >= 200 and money>= usemoney:
                    num = int(input('Enter the 2 digits number to play lottery: '))
                    if num == randrange(10,11):
                        usemoney = usemoney*10
                        money = money + usemoney
                        print('You win this game.\nYour money is ',money)
                    else:
                        money = money - usemoney 
                        print('You lose the game and your money is ',money)
                elif usemoney> money:
                    print('your money is exceed than original money')
                    entry = input("put 'y' to continue or type 'n' to out:\n")
                    if entry=='y':
                        while money > 100:
                            usemoney = int(input('Enter the amount of money to play lottery.\nmust be more than 200:\n'))
                            if usemoney >= 200 and money>=usemoney:
                                num = int(input('Enter the 2 digits number to play lottery: '))
                                if num == randrange(10,100):
                                    usemoney = usemoney*10
                                    money = money + usemoney
                                    print('You win this game.\nYour money is ',money)
                                else:
                                    money = money - usemoney 
                                    print('You lose the game and your money is ',money)
                            elif usemoney> money:
                                print('your money is exceed than original money')
                                entry = input("put 'y' to continue or type 'n' to out:\n")
                                if entry=='y':
                                    while money > 100:
                                        usemoney = int(input('Enter the amount of money to play lottery.\nmust be more than 200:\n'))
                                        if usemoney >= 200 and money>= usemoney:
                                            num = int(input('Enter the 2 digits number to play lottery: '))
                                            if num == randrange(10,100):
                                                usemoney = usemoney*10
                                                money = money + usemoney
                                                print('You win this game.\nYour money is ',money)
                                            else:
                                                money = money - usemoney 
                                                print('You lose the game and your money is ',money)
                elif usemoney <200:
                    print("you need to put more money")
                    entry = input("put 'y' to continue or type 'n' to out:\n")
                    if entry=='y':
                        while money > 100:
                            usemoney = int(input('Enter the amount of money to play lottery.\nmust be more than 200:\n'))
                            if usemoney >= 200 and money>= usemoney:
                                num = int(input('Enter the 2 digits number to play lottery: '))
                                if num == randrange(10,100):
                                    usemoney = usemoney*10
                                    money = money + usemoney
                                    print('You win this game.\nYour money is ',money)
                                else:
                                    money = money - usemoney 
                                    print('You lose the game and your money is ',money)
                            elif usemoney> money:
                                print('your money is exceed than original money')
                                entry = input("put 'y' to continue or type 'n' to out:\n")
                                if entry=='y':
                                    while money > 100:
                                        usemoney = int(input('Enter the amount of money to play lottery.\nmust be more than 200:\n'))
                                        if usemoney >= 200 and money>= usemoney:
                                            num = int(input('Enter the 2 digits number to play lottery: '))
                                            if num == randrange(10,100):
                                                usemoney = usemoney*10
                                                money = money + usemoney
                                                print('You win this game.\nYour money is ',money)
                                            else:
                                                money = money - usemoney 
                                                print('You lose the game and your money is ',money)
                    elif entry == 'n':
                        print("you can leave.")
                        p = False
                        exit()
            if money < 100:
                print('You don\'t have enough money to play.\nRecharge!')
                p = False
                exit()
        else:
            print('Wrong Id')
            p = False
            exit()
                
    elif entry == 'n':
        print("you can leave.")
        p = False
        exit()
else:
    p = False
