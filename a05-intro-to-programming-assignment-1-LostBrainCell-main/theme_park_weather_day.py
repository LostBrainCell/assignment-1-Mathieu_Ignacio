from random import randint


WeatherRating= randint(1, 3)  # Randomly select a weather condition (1: sunny, 2: rainy, 3: cloudy)    

Sunny = 1
Rainy = 2
Stormy = 3 
# Sunny = no change
# Rainy= snacks half price
# Stormy = Parking is free
snackpass = 8
parkingPrice = 10

randomDiscount = randint(1, 5)
print("Welcome to Dragon Coaster Park")
user_input = input("Would you like to buy a ticket? (yes/no): ").lower() 

if user_input == "yes":
    age = int(input("Enter the guest age?"))
    if age < 5:
        ticketPrice = 0
        print("Your ticket is free")
        parking = input("Do you need parking? (yes/no): ").lower() #Parking costs $10
        if parking == "yes":
            print("Parking added")
            if WeatherRating == 3: # Stormy
                parkingPrice = 0
        elif parking == "no":
            parkingPrice = 0
        snacks = input("Do you want a snack pass? (yes/no): ").lower() #Snacks cost $8
        if snacks == "yes": 
            print("Snacks pass added")
            if WeatherRating == 2: # Rainy
                snackpass = snackpass / 2
        elif snacks == "no":
            snackpass = 0
        print("Your total is: $", ticketPrice + parkingPrice + snackpass)
        breakpoint()
    elif 5 <= age <= 12: 
        ticketPrice = 12
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == "yes":
            ticketPrice -= 5
            print(f"Mystery discount: ${randomDiscount}")
            ticketPrice -= randomDiscount
            print(f"Your ticket cost ${ticketPrice}")
        elif coupon == "no":
            ticketPrice -= randomDiscount
            print(f"Your ticket cost ${ticketPrice}")
    elif 12 < age <= 64:
        ticketPrice = 25
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket cost ${ticketPrice}")
        elif coupon == "no":
            ticketPrice -= randomDiscount
            print(f"Your ticket cost ${ticketPrice}")
    elif age >= 65:
        ticketPrice = 15
        coupon = input("Do you have a coupon? (yes/no): ").lower()
        if coupon == "yes":
            ticketPrice -= 5
            ticketPrice -= randomDiscount
            print(f"Your ticket cost ${ticketPrice}")
        elif coupon == "no":
            ticketPrice -= randomDiscount
            print(f"Your ticket cost ${ticketPrice}")
elif user_input == "no":
    print("Thanks maybe next time!")
else:
    print("Invalid input, Please try again")

# parking = input("Do you need parking? (yes/no): ").lower() #Parking costs $10
# if parking == "yes":
#     parkingPrice = 10
#     print("Parking added")
#     if WeatherRating == 3: # Stormy
#         parkingPrice = 0
# elif parking == "no":
#     parkingPrice = 0
# snacks = input("Do you want a snack pass? (yes/no): ").lower() #Snacks cost $5
# if snacks == "yes": 
#     snackpass = 8
#     print("Snacks pass added")
#     if WeatherRating == 2: # Rainy
#         snackpass = 4
# elif snacks == "no":
#     snackpass = 0
# print("Your total is: $", ticketPrice + parkingPrice + snackpass)