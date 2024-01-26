#5-8,
#5-9
usernames = ["ifreezki", 
             "thorlirn", 
             "xormia", 
             "sigurdmeister", 
             "space_fuel", 
             "admin"]

if usernames:
    for name in usernames:
        if name == "admin":
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")

#5-10
current_users = usernames[:]
new_users = [current_users[1],
            current_users[2],
            "pattason",
            "srnning",
            "sigurd_ronning"]

for user in new_users:
    if user.lower() in current_users:
        print("You need to enter a new username.")
    elif user.lower() not in current_users:
        print("Username is available!")
    
#5-11
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

