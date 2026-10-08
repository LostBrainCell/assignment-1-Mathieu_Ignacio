from random import randint


WeatherRating= randint(1, 3)  # Randomly select a weather condition (1: sunny, 2: rainy, 3: cloudy)    

Sunny = 1
Rainy = 2
Stormy = 3 
# Sunny = no change
# Rainy= snacks half price
# Stormy = Parking is free



randomDiscount = randint(1, 5)
user_input = input("Do you want to buy a ticket? (yes/no): ").lower() 

if user_input == "yes":
    age = int(input("What is your age?"))
    coupon = input("Do you have a coupon? (yes/no): ").lower()
    if age < 5:
        print("Your ticket is free")
    elif 5 <= age <= 12: 
        ticketPrice = 12
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket costs ${ticketPrice}")
    elif 12 < age <= 64:
        ticketPrice = 25
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket costs ${ticketPrice}")
    elif age >= 65:
        ticketPrice = 15
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket costs ${ticketPrice}")
    parking = input("Do you need parking? (yes/no): ").lower() #Parking costs $10
    if parking == "yes":
        parkingPrice = 10
        print("Parking added")
        if WeatherRating == 3: # Stormy
            parkingPrice = 0
    elif parking == "no":
        parkingPrice = 0
    snacks = input("Do you want a snack pass? (yes/no): ").lower() #Snacks cost $5
    if snacks == "yes": 
        snackpass = 8
        print("Snacks pass added")
        if WeatherRating == 2: # Rainy
            snackpass = 4
    elif snacks == "no":
        snackpass = 0
    print("Your total is: $", ticketPrice + parkingPrice + snackpass)
elif user_input == "no":
    print("Thanks maybe next time!")
else:
    print("Invalid input, Please try again")





    print("Your ticket price is: $", ticketPrice)
    print("Your parking price is: $", parkingPrice) 
    print("Your snack pass price is: $", snackpass)