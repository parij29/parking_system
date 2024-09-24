import os
from colorama import Fore, Back, Style

# parking floor with 10 slots in each of them
# parkings = { 1: [0,0,0,0,0,0,0,0,0,0] , 2: [0,0,0,0,0,0,0,0,0,0] }
parkings = { 1: [0]*10 , 2: [0]*10 }

#select parking slot
def Select_Parking_Slot():
    slots_available = False
    print("Select Parking Floor\n")
    
    while not slots_available:
        parking_floor = int(input())

        if parking_floor == 0:
            #doesn't return any value
            return [0,0]
        if parking_floor in parkings:   # check whether the entered parking floor value is present in Parkings dictionary
            if 0 in parkings[parking_floor]:  # Check if any of the values in the Parkings list is 0 (this indicates available parking)
                print("slots available")
                slots_available = True
            else:
                print(f"parking is full on floor # {parking_floor}\nPlease select some other floor or select 0 to go back to the main menu")
    print("Select Parking Slot\n")
    parking_Slot = int(input())

    return [parking_floor, parking_Slot]

#shows all the available slots in green and all the occupied ones in red
def Show_Availability():
    for f in range(1,3):
        print("+------+-----+-----+-----+-----+-----+")
        slot_count = len(parkings[f])   #slot_count = len(selected parking floor's slots list)
        print("|      |", end="");
        for p1 in range(1, slot_count, 2):  #to print even slot numbers 
            printable_number = p1+1     #p1 is zero index, so we need add 1 to display the slot number
            if(parkings[f][p1] == 0):
                print(Fore.GREEN+f"  {printable_number}", end="")   #printable_number = slot number(to be printed in green)
            else:
                print(Fore.RED+f"  {printable_number}", end="")
            print(Style.RESET_ALL, end="")  #to reset the color to normal
            print(" "*(3-len(str(printable_number))) + "|", end="") #to pad every slot with right number of wide spaces
        print("\n|      |     |     |     |     |     |")
        print("|      +-----+-----+-----+-----+-----+")
        print("|                                    |")
        print("|      +-----+-----+-----+-----+-----+")

        print("|      |", end="");
        for p1 in range(0, slot_count-1, 2):    #to print odd slot numbers

            printable_number = p1+1
            if(parkings[f][p1] == 0):
                print(Fore.GREEN+f"  {printable_number}", end="")
            else:
                print(Fore.RED+f"  {printable_number}", end="")
            print(Style.RESET_ALL, end="")
            print(" "*(3-len(str(printable_number))) + "|", end="")
        print("\n|      |     |     |     |     |     |")
        print("|      +-----+-----+-----+-----+-----+")
        print(f"|      | Floor-{f}");

        print("\n"*2)

                
#parks the car in the chosen slot               
def Park_Car(floor, slot):
    if floor in parkings:
        if (slot >= 1 and slot < 11 and parkings[floor][slot-1] == 0):  #slot number entered is not zero index (ex: if entered slot number is 1, it's position is 0 )
            parkings[floor][slot-1] = 1
            print(f"Your car is parked at Floor # {floor} - Parking Slot # {slot}")
        else:
            print("Selected parking slot is either invalid or already in use")
    else:
        print(f"Invalid Floor number {floor}")
    print("Press enter to continue...")
    input()

#removes the car from its slot
def Remove_Car(floor, slot):
    if floor in parkings:
        if (slot >= 1 and slot < 11 and parkings[floor][slot-1] == 1):
            parkings[floor][slot-1] = 0
            print(f"Your car is removed from floor # {floor} - Parking Slot # {slot}")
        else:
            print("Selected parking slot is either invalid or already empty")
    else:
        print(f"Invalid Floor number {floor}")
    print("Press enter to continue...")
    input()
        
#the program execution starts here
option = 0
parking_slot = 0
parking_floor = 0
while (option != 4):
    os.system("cls")
    print ("1. Park your car\n")
    print ("2. Remove your car\n")
    print ("3. Check availability\n")
    print ("4. Exit\n")

    option = int(input('Enter your choice: '))
    if(option == 1):
        Show_Availability()
        parking_floor, parking_Slot = Select_Parking_Slot()
        if(parking_floor > 0):
            Park_Car(parking_floor, parking_Slot)
    if(option == 2):
        parking_floor, parking_Slot = Select_Parking_Slot()
        Remove_Car(parking_floor, parking_Slot)
    if(option == 3):
        Show_Availability()
        print("Press enter to continue...")
        input()

