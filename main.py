# Use the logical connective and rather than a double inequality.

'''
player_hand = 17
dealer_hand = 19

if (player_hand > dealer_hand) and (player_hand <= 21):
    print("The player wins!")

# Last time, we explored user input.

name = input("What's your name? ")
print(f"Hello, {name}.")

print()

# The input function interprets the user's input
# as a string!

age_string = input("How old are you? ")
age = int(age_string)
if age > 60:
    print("You're old!")

print()

age = int(input("How old are you? "))
if age > 40:
    print("You're old!")

print()
# Chain if-elif-else is efficient.
user_response = input("Do you want to play again? Y/N ")
# Try if-else.
if user_response.upper() == 'Y':
    print("Let's play again.")
# Otherwise if...
elif user_response.upper() == 'N':
    print("Quitting.")
else:
    print("Error.")

# Contrast with sequential if statements.
user_response = input("Do you want to play again? Y/N ")
# Try if-else.
if user_response.upper() == 'Y':
    print("Let's play again.")
if user_response.upper() == 'N':
    print("Quitting.")
if (user_response.upper() != 'Y') and (user_response != 'N'):
    print("Error.")

for i in range(5):
    print(i + 1)

print()

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print()

prompt = "\nTell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Let's try to streamline the design of this while loop.
prompt = "\nTell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    print(message)
    message = input(prompt)

# Use a flag in a while loop.
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Let's try to streamline.
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
active = True
message = ""
while active:
    print(message)
    message = input(prompt)
    if message == 'quit':
        active = False
# We eliminated the need for a false block.
# We used if rather than if-else.

'''

# Use break to exit a while loop.
prompt = "\nWhat cities have you visited?"
prompt += "\nEnter 'quit' when you're done. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I've been to {city}!")
