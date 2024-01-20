from task_2 import names_to_invite

#3-8
locations = ["USA", "Thailand", "Vietnam", "India", "Japan"]

print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)

print("\n")

locations.reverse()
print(locations)

locations.reverse()
print(locations)

print("\n")

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)


#3-9
print(f"Number of invited people to the dinner was {len(names_to_invite)}.\n")

#3-10
car_names = ["BMW", "Volvo", "Volkswagen", "Audi", "Toyota"]

print(car_names)

print(car_names[0])
print(car_names[-1])

car_names[0] = "Skoda"
print(car_names)

car_names.append("Ford")
car_names.insert(2, "Nissan")

print(car_names)

del car_names[0]
car_names.remove("Audi")

print(car_names)

popped_item = car_names.pop(2)
print(popped_item)

print(car_names)

print(sorted(car_names))
print(sorted(car_names, reverse=True))

car_names.sort()
print(car_names)
car_names.sort(reverse=True)
print(car_names)

print(len(car_names))