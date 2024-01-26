#5-1
car = "volvo"
print("Is car == 'volvo'? I predict True")
print(car == "volvo")

print("Is car == 'BMW'? I predict False")
print(car == "BMW")

#5-2
message = "HI"

if message == "HI":
    print(True)
else:
    print(False)

message_1 = "hElLo"

if message_1.lower() == "hello":
    print(True)
else:
    print(False)

age = 18
age_1 = 21

if age == 18 and age_1 == 21:
    print(True)
else:
    print(False)

if age == 18 or age_1 == 18:
    print(True)
else:
    print(False)


numbers = [1, 2, 3, 4, 5]

if 6 in numbers:
    print(True)
else:
    print(False)

if 6 not in numbers:
    print(True)
else:
    print(False)