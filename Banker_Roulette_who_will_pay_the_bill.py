# Split string method
name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")


#Write your code below this line 👇
# print(names)

import random

# random_name = random.randint(0, len(names))
# print(f"{names[random_name]} is going to buy the meal today!")

# num_items = len(names)
# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")