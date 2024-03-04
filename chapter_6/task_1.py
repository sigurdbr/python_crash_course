#6-1
person =  {"first_name": "Sigurd", 
           "last_name": "Rønning", 
           "age": 25, 
           "city": "Stange",
           }

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

#6-2
favorite_numbers = {"sigurd": 6,
                    "aivi": 28,
                    "sander": 16,
                    "jørgen": 5,
                    "oliver": 5,
                    }

for key, value in favorite_numbers.items():
    print(f"{key.title()}s favorite number is {value}")

<<<<<<< HEAD
#6-3

glossary = {
    "dictionary": "A place to store key-value pairs",
    "list": "A place to store values",
    "value": "something that contains information",
    "if-else": "something that evalutes the value provided",
    "for-loop": "a function used to iterate a list for example",
}

for key, value in glossary.items():
    print(f"The meaning of {key.title()} is: '{value}'")
=======
glossary = {"value": "some kind of data",
            "variable": "can hold data",
            "list": "stores data in an indexed order",
            "tuple": "same as list, but can't be changed",
            "int": "the type of a number",
            }

for key, value in glossary.items():
    print(f"{key.title()} means '{value}'.")

>>>>>>> 560a67e52be6d5cc9422da46e2ad7984ac3f44d1
