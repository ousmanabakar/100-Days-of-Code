# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
list_len = len(names)
random_name = random.randint(0,(list_len - 1))

print(f"{names[random_name]} is going to buy the meal today!")


