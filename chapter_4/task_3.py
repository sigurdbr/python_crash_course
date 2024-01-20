#4-10
from task_2 import cubes_v2

print(f"The first three items in the list are {cubes_v2[:3]}")
print(f"Here are three items from the middle of the list {cubes_v2[3:6]}")
print(f"Here are the last three items of the list {cubes_v2[-3:]}")

#4-11
from task_1 import pizzas
friend_pizzas = pizzas[:]

pizzas.append("Plain")
friend_pizzas.append("Diavola")

print("My favorite pizzas are")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are")
for pizza in friend_pizzas:
    print(pizza)