class Garage():
    avail_ticket = [987200, 765433, 126543, 455380, 504439]
    avail_ticket_copy = [987200, 765433, 126543, 455380, 504439]
    avail_space = ["A", "B", "C", "D", "E"]
    status = {"paid" : False}
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
    print (f'After the first hour, the cost is reduced by an additional 10% for each hour.')
    while flag == True:
        time = int(input(f' \nHow many hours will your stay be? > '))
        if time not in Garage.hours:
            print (f'\nPlease enter a valid selection.')
        else:
            for instance in Garage.all:
                if time == instance.hours:
                    print (f'\nYour ticket number is {instance.number}. Please take the ticket.')
                    Garage.avail_ticket.pop(instance.index)
                    print (f'Your ticket is assigned to parking space {instance.space}. Please park in that location.')
                    Garage.avail_space.pop(instance.index)
                    flag = False
                    break
                else:
                    continue

def pay_for_parking():
    user_input = float(input("How much is your current payment? > "))
    user_input_pool = Garage.user_input_pool + user_input
    while user_input_pool < amount_due:
            print(f'\n Hmmm... {user_input_pool} dollars?')
            print(f'That is not enough.')
            print(f'You are missing {amount_due - user_input_pool} dollars.')
            user_input = float(input("How much is your current payment? > "))
            user_input_pool = user_input_pool + user_input
    if user_input_pool == amount_due:
        print("\nThank you, have a nice day! - you have 15 minutes to get out.")
    elif user_input_pool > amount_due:
        print (f'\nChange due is: {user_input_pool - amount_due}. Sorry, no change available.')
        print("\nThank you, have a nice day! ...(and thanks for the tip!) - you have 15 minutes to get out.")  
    Garage.status["paid"] = True

def replace_inventory():
    for instance in Garage.all:
        if user_ticket == instance.number:
            Garage.avail_space.insert(instance.index, instance.space)
            Garage.avail_ticket.insert(instance.index, user_ticket)

###################################### MAIN PROGRAM STARTS HERE #######################################            
print (f'\nWelcome to the garage.\nThere are {len(Garage.avail_space)} spots currently available and you may park up to 5 hours.')
take_ticket()
print (f'There are now {len(Garage.avail_space)} spots and {len(Garage.avail_ticket)} tickets available.') 
print("Time passes...\n              ...\n                 ...")

flag = True
while flag == True:
    user_ticket = int(input("\nTo pay, please enter your ticket number: "))
    if user_ticket not in Garage.avail_ticket_copy:
        print (f'Ticket recognition error. Please try again.')
    else:
        for instance in Garage.all:
            amount_due = (Garage.base_cost * instance.hours) * instance.rate
            print (f'The amount due is ${amount_due}.')
            flag = False
            break
while Garage.status["paid"] == False:
     pay_for_parking()

replace_inventory()
print (f'There are now {len(Garage.avail_space)} spots and {len(Garage.avail_ticket)} tickets available.')