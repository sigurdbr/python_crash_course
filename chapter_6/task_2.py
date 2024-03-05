#6-4
#Already done this in task_1.py

#6-5
rivers = {
    "norway": "glomma",
    "egypt": "nile",
    "china": "yangtze"
}

for country, river in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.values():
    print(river)

for country in rivers:
    print(country)

#6-6
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

to_take_poll = ["sigurd", "kristoffer", "simen", "jen", "edward"]

for name in to_take_poll:
    if name in favorite_languages:
        print(f"Thank you for taking the poll, {name.title()}!")
    elif name not in favorite_languages:
        print(f"Please take the poll, {name.title()}!")