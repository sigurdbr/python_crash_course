#7-1
car_to_choose = input("Which car would you like? ")
print(f"Let me see if I can find you a {car_to_choose}!")

#7-2
num_of_guests = input("How many people are in your dinner group? ")
num_of_guests = int(num_of_guests)

if num_of_guests < 8:
    print("Your table is ready!")
elif num_of_guests >= 8:
    print("You'll have to wait for a table.")

#7-3
asked_num = input("What is your favorite number? ")
asked_num = int(asked_num)

if asked_num%10 == 0:
    print("It's a multiple of 10!")