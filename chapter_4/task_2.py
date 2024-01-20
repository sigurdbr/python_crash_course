#4-3

for num in range(1,21):
    print(num)

#4-4
large_list = list(range(1,1000001))

#for num in large_list:
#    print(num)

#4-5
print(min(large_list))
print(max(large_list))
print(sum(large_list))

#4-6
odd_list = list(range(1,21,2))

for num in odd_list:
    print(num)

#4-7
threes = []
for num in range(3,31):
    value = num**2
    threes.append(value)

for num in threes:
    print(num)

#4-8
cubes = []
for num in range(1,11):
    value = num**3
    cubes.append(value)

for num in cubes:
    print(num)

#4-9

cubes_v2 = [value**3 for value in range(1,11)]

print(cubes_v2)