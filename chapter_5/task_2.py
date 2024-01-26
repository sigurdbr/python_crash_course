#5-3
alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points!")

if alien_color == "red":
    print("The alien is red!")

#5-4
if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#5-5
if alien_color == "green":
    print("You juste earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")



#5-6
age = 25

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

#5-7
favorite_fruits = ["Apple", "Orange", "Mango", "Grapes"]

if "Apple" in favorite_fruits:
    print(f"I like {favorite_fruits[0]}s!")

if "Orange" in favorite_fruits:
    print(f"I really like {favorite_fruits[1]}s!")

if "Mango" in favorite_fruits:
    print(f"I really like {favorite_fruits[2]}s!")

if "Banana" in favorite_fruits:
    print("I really like bananas!")