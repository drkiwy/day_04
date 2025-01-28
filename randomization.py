# import random


# random_integer = random.randint(1, 10)
# print(random_integer)


# print(my_module.pi)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

#  state1 = "Delaware"
#  state2 = "Pennsylvania"

# states_of_america = ["Delaware" , "Pennsylvania" , "New Jersey" , "Georgia" , "Connecticut" , "Massachusetts" , "Maryland" , "South Carolina" , "New Hampshire" , "Virginia" , "New York" , "North Carolina" , "Rhode Island" , "Vermont" , "Kentucky" , "Tennessee" , "Ohio" , "Louisiana" , "Indiana" , "Mississippi" , "Illinois" , "Alabama" , "Maine" , "Missouri" , "Arkansas" , "Michigan" , "Florida" , "Texas" , "Iowa" , "Wisconsin" , "California" , "Minnesota" , "Oregon" , "Kansas" , "West Virginia" , "Nevada" , "Nebraska" , "Colorado" , "North Dakota" , "South Dakota" , "Montana" , "Washington" , "Idaho" , "Wyoming" , "Utah" , "Oklahoma" , "New Mexico" , "Arizona" , "Alaska" , "Hawaii"]
# print(states_of_america[0])

# states_of_america[1] = "Pencilvania"
# print(states_of_america)

# states_of_america.append("Angoland")
# print(states_of_america)

#  states_of_america.extend(["Angoland", "Jack Bauer Land"])
#  print(states_of_america)
# num_of_states = len(states_of_america)
#  If you print it out, you will see that you will get an error because the index is out of range
# print(states_of_america[num_of_states])

#Solution to the error above is to subtract 1 from the length of the list
# print(states_of_america[num_of_states - 1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)