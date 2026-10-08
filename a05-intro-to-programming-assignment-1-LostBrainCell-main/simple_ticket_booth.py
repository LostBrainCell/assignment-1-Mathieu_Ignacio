

from random import randint, random


randomDiscount = randint(1, 5)

user_input = input("Do you want to buy a ticket? (yes/no): ").lower() 

if user_input == "yes":
    age = int(input("What is your age?"))
    if age < 5:
        print("Your ticket is free")
    elif 5 <= age <= 12: 
        ticketPrice = 12
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket price is ${ticketPrice}")
        elif coupon == "no":
            ticketPrice -= randomDiscount
            print(f"Your ticket price is ${ticketPrice}")
    elif 12 < age <= 64:
        ticketPrice = 25
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket price is ${ticketPrice}")
        elif coupon == "no":
            ticketPrice -= randomDiscount
            print(f"Your ticket price is ${ticketPrice}")
    elif age >= 65:
        ticketPrice = 15
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket price is ${ticketPrice}")
        elif coupon == "no":
            ticketPrice -= randomDiscount
            print(f"Your ticket price is ${ticketPrice}")
elif user_input == "no":
    print("Thanks maybe next time!")
else:
    print("Invalid input, Please try again")
