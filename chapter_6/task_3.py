#6-7

person_1 = {
    "first_name": "sigurd",
    "last_name": "rønning",
    "age": 25,
    "city": "stange",
}

person_2 = {
    "first_name": "aivi",
    "last_name": "falkum",
    "age": 23,
    "city": "stange",
}

person_3 = {
    "first_name": "jørgen",
    "last_name": "rønning",
    "age": 26,
    "city": "oslo",
}

people = [person_1, person_2, person_3]

print(people)


#6-8

pet_1 = {
    "name": "fiffi",
    "owner": "aivi",
}

pet_2 = {
    "name": "mira",
    "owner": "anne-kari",
}

pet_3 = {
    "name": "storm",
    "owner": "geir",
}

list_of_pets = [pet_1, pet_2, pet_3]

for pet in list_of_pets:
    print(pet)

#6-9
favorite_places = {
    "aivi": "syden",
    "sigurd": "roma",
    "jørgen": "oslo",
}

for name, place in favorite_places.items():
    print(f"{name.title()}s favorite place is {place.title()}.")

#6-10
favorite_numbers = {
    "sigurd": [1,3,5],
    "aivi": [2,4,6],
    "jørgen": [5,7,9],
}

for name, nums in favorite_numbers.items():
    print(f"\n{name.title()}s favorite number is: ")
    for num in nums:
        print(num)

#6-11
cities = {
    "oslo": {
        "country": "norway",
        "population": 634000,
        "size": "454km2",
    },
    "rome": {
        "country": "italy",
        "population": 2873000,
        "size": "1285km2",
    },
    "paris": {
        "country": "france",
        "population": 2161000,
        "size": "105.4km2"
    },
}

for city, fact in cities.items():
    print(f"{city.title()}: {fact}")

#6-12