# Text-Based Adventure Game

print("Welcome to the Adventure Game!")
print("You are standing in a dark forest. Two paths are in front of you.")
choice1 = input("Do you go LEFT or RIGHT? ").lower()

if choice1 == "left":
    print("You find a river. Do you want to SWIM or BUILD a boat?")
    choice2 = input("Your choice: ").lower()
    if choice2 == "swim":
        print("Oh no! The river current was too strong. You drowned. ❌")
    else:
        print("Great! You built a boat and crossed the river safely. 🎉")

elif choice1 == "right":
    print("You see a cave. Do you want to ENTER or RUN away?")
    choice2 = input("Your choice: ").lower()
    if choice2 == "enter":
        print("Inside the cave you found a treasure chest! 🏆")
    else:
        print("You ran away safely, but missed the treasure. 😅")

else:
    print("Invalid choice. Game Over.")
