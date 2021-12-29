# Lists - Ordered
import random

fruits = ["apple", "banana", "dates"]

print(fruits)
print(len(fruits))

item = fruits.pop()
print(item)
print(fruits)

fruits.append(item)
print(fruits)

fruits.append("cherry")

fruits.sort()
print(fruits)

# Banker Roulette
print("\nLet's play Banker's Roulette")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

selected_name = names[random.randint(0, len(names) - 1)]
print(f"{selected_name} will pay for our meal today!")

# Rock Paper Scissors
print("\nLet's play Rock-Paper-Scissors")
rock = '🪨'
paper = '📄'
scissors = '✄'

options = ['rock', 'paper', 'scissors']
user_choice = int(input(f"What do you want to choose? 0 for {rock}, 1 for {paper} and 2 for {scissors}\n"))

computer_choice = random.randint(0, 2)

if user_choice == 0:
    if computer_choice == 0:
        print(f"Both choose {rock}. Try Again!")
    elif computer_choice == 1:
        print(f"You choose {rock}, Computer choose {paper}. You lose!")
    else:
        print(f"You choose {rock}, Computer choose {scissors}. You win!")
elif user_choice == 1:
    if computer_choice == 0:
        print(f"You choose {paper}, Computer choose {rock}. You win!")
    elif computer_choice == 1:
        print(f"Both choose {paper}. Try Again!")
    else:
        print(f"You choose {paper}, Computer choose {scissors}. You lose!")
else:
    if computer_choice == 0:
        print(f"You choose {scissors}, Computer choose {rock}. You lose!")
    elif computer_choice == 1:
        print(f"You choose {scissors}, Computer choose {paper}. You win!")
    else:
        print(f"Both choose {scissors}. Try Again!")

