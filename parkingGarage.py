# before testing code, make sure to type this in your command/terminal, [pip install colorama].
# as well reload vscode.
from colorama import Fore, Back, Style
import threading
event = threading.Event()


class Garage():
    avail_ticket = [987200, 765433, 126543, 455380, 504439]
    avail_ticket_copy = [987200, 765433, 126543, 455380, 504439]
    avail_space = ["A", "B", "C", "D", "E"]
    status = {"paid": False}
    base_cost = 10.0
    user_input_pool = 0.0
    hours = [1, 2, 3, 4, 5]
    all = []

    def __init__(self, number, hours, space, index, rate):
        self.number = number
        self.hours = hours
        self.space = space
        self.index = index
        self.rate = rate
        Garage.all.append(self)


ticket1 = Garage(987200, 1, "A", 0, 1)
ticket2 = Garage(765433, 2, "B", 1, .9)
ticket3 = Garage(126543, 3, "C", 2, .8)
ticket4 = Garage(455380, 4, "D", 3, .7)
ticket5 = Garage(504439, 5, "E", 4, .6)


def take_ticket():
    flag = True
    print(f'After the first hour,' + Fore.YELLOW +
          ' the cost is reduced by an additional 10% for each hour.' + Fore.WHITE)
    event.wait(1.50)
    while flag == True:
        time = int(input(Fore.WHITE + f' \nHow many hours will your stay be? > '))
        if time not in Garage.hours:
            print(Fore.RED + f'\nPlease enter a valid selection.')
            event.wait(.50)
        else:
            for instance in Garage.all:
                if time == instance.hours:
                    print(
                        Fore.YELLOW + f'\nYour ticket number is {instance.number}.' + Fore.WHITE + ' Please take the ticket.')
                    event.wait(.50)
                    Garage.avail_ticket.pop(instance.index)
                    print(
                        f'Your ticket is assigned to parking space {instance.space}. Please park in that location.')
                    event.wait(.50)
                    Garage.avail_space.pop(instance.index)
                    flag = False
                    break
                else:
                    continue


def pay_for_parking():
    user_input = float(input("\nHow much is your current payment? > "))
    user_input_pool = Garage.user_input_pool + user_input
    while user_input_pool < amount_due:
        print(Fore.RED + '\n######################')
        event.wait(.50)
        print('# INSUFFICIENT FUNDS #')
        event.wait(.50)
        print('######################\n')
        event.wait(.50)
        print(f'You are missing {amount_due - user_input_pool} dollars.\n')
        event.wait(1.50)
        user_input = float(
            input(Fore.WHITE + "How much is your current payment? > "))
        user_input_pool = user_input_pool + user_input
    if user_input_pool == amount_due:
        print(Fore.GREEN + "\nThank you, have a nice day!" +
              Fore.WHITE + "- you have 15 minutes to get out.")
        event.wait(.50)
    elif user_input_pool > amount_due:
        print(Fore.YELLOW +
              f'\nChange due is: {user_input_pool - amount_due}... ' + Fore.RED + 'Sorry, no change available.')
        event.wait(.50)
        print(Fore.GREEN + "\nThank you, have a nice day! ...(and thanks for the tip!) " +
              Fore.WHITE + "- you have 15 minutes to get out.")
        event.wait(.50)
    Garage.status["paid"] = True


def replace_inventory():
    for instance in Garage.all:
        if user_ticket == instance.number:
            Garage.avail_space.insert(instance.index, instance.space)
            Garage.avail_ticket.insert(instance.index, user_ticket)


###################################### MAIN PROGRAM STARTS HERE #######################################

# CLS #
def clearConsole(): return print('\n' * 150)


clearConsole()
# CLS #

# TITLE #
print(Fore.BLUE + '░█──░█ ░█▀▀▀ ░█─── ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ▀▀█▀▀ ░█─░█ ░█▀▀▀ 　 ░█▀▀█ ─█▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▀ ')
event.wait(.50)
print('░█░█░█ ░█▀▀▀ ░█─── ░█─── ░█──░█ ░█░█░█ ░█▀▀▀ 　 ─░█── ░█──░█ 　 ─░█── ░█▀▀█ ░█▀▀▀ 　 ░█─▄▄ ░█▄▄█ ░█▄▄▀ ░█▄▄█ ░█─▄▄ ░█▀▀▀ ')
event.wait(.50)
print('░█▄▀▄█ ░█▄▄▄ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄▄ 　 ─░█── ░█▄▄▄█ 　 ─░█── ░█─░█ ░█▄▄▄ 　 ░█▄▄█ ░█─░█ ░█─░█ ░█─░█ ░█▄▄█ ░█▄▄▄\n')
event.wait(1.50)
#TITLE #

#TITLE 2 #
print("                                                                       _________________________   ")
event.wait(.50)
print("                                  /\       _____          _____       |   |     |     |    | |  \  ")
event.wait(.50)
print("                   ,-----,       /  \ ____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ ")
event.wait(.50)
print("                ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \ ")
event.wait(.50)
print("               ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--' ")
event.wait(.50)
print('              `````````````````````````````````````````````````````````````````````````````````````')
event.wait(1.50)
#TITLE 2 #

# START #
print(Fore.YELLOW +
      f'\nThere are {len(Garage.avail_space)} spots currently available and you may park up to 5 hours.' + Fore.WHITE)
event.wait(.50)

# take_ticket() #
take_ticket()
# take_ticket() #

print(Fore.YELLOW +
      f'There are now {len(Garage.avail_space)} spots and {len(Garage.avail_ticket)} tickets available.' + Fore.WHITE)
event.wait(1.50)
print("Time passes... " + Fore.BLUE + "    _______  " + Fore.WHITE)
event.wait(.50)
print(Fore.WHITE + "...      " + Fore.BLUE + "         /  12   \ ")
event.wait(.50)
print(Fore.WHITE + "...      " + Fore.BLUE + "        |    |    |")
event.wait(.50)
print(Fore.WHITE + "...      " + Fore.BLUE + "        |9   |   3|")
event.wait(.50)
print(Fore.WHITE + "...      " + Fore.BLUE + "        |     \   |")
event.wait(.50)
print(Fore.WHITE + "...      " + Fore.BLUE + "        |         |")
event.wait(.50)
print(Fore.WHITE + "...      " + Fore.BLUE + "         \___6___/" + Fore.WHITE)
event.wait(1.50)
flag = True
while flag == True:
    user_ticket = int(
        input(Fore.WHITE + "\nTo pay, please enter your ticket number: "))
    if user_ticket not in Garage.avail_ticket_copy:
        print(Fore.RED + f'\nTicket recognition error. Please try again.')
        event.wait(.50)
    else:
        for instance in Garage.all:
            if user_ticket == instance.number:
                amount_due = (Garage.base_cost * instance.hours) * instance.rate
                print(f'The amount due is ${amount_due}.')
                event.wait(.50)
                flag = False
                break
while Garage.status["paid"] == False:
    pay_for_parking()

replace_inventory()
print(Fore.YELLOW +
      f'There are now {len(Garage.avail_space)} spots and {len(Garage.avail_ticket)} tickets available.' + Fore.WHITE)
# START #

# END #
event.wait(1.50)
print(Fore.BLUE + '\n   -           __')
event.wait(.50)
print(' --          ~( @\   \ ')
event.wait(.50)
print('---   _________]_[__/_>________')
event.wait(.50)
print('     /  ____ \ <>     |  ____  \ ')
event.wait(.50)
print('    =\_/ __ \_\_______|_/ __ \__D')
event.wait(.50)
print('________(__)_____________(__)____' + Fore.WHITE)
event.wait(1.50)
# END #