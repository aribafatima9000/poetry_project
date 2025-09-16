score = 0   
a = input("Which is the capital city of Pakistan? ")
if a.lower() == "islamabad":
    print("Correct ")
    score += 1
else:
    print("Wrong , the correct answer is Islamabad")


b = input("Is cancer a biggest problem? (Yes/No): ")
if b.lower() == "yes":
    print("Correct ")
    score += 1
else:
    print("Wrong , the correct answer is Yes")


print("\nYour total score is:", score)
