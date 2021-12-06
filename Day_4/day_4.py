# Banker meal russian roulette

import random

names = input("type in some names\n")
names_split = names.split(", ")
len_names_split = len(names_split)

number = random.randint(0, len_names_split-1)
payor = names_split[number]

print(number)
print(names_split)
print(payor)

print(f"{payor} will be paying tonight")