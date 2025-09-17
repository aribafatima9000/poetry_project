

score = 0  

print("Welcome to the Quiz Game!\n")

# Question 1
print("Q1: What is the capital of Pakistan?")
print("a) Karachi\nb) Lahore\nc) Islamabad\nd) Peshawar")
ans = input("Your answer: ")

if ans.lower() == "c" or ans.lower() == "islamabad":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Islamabad.\n")

# Question 2
print("Q2: Which language is used for Data Science?")
print("a) Java\nb) Python\nc) C++\nd) HTML")
ans = input("Your answer: ")

if ans.lower() == "b" or ans.lower() == "python":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Python.\n")

# Question 3
print("Q3: Which planet is known as the Red Planet?")
print("a) Earth\nb) Venus\nc) Mars\nd) Jupiter")
ans = input("Your answer: ")

if ans.lower() == "c" or ans.lower() == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Final Score
print("Your Final Score is:", score, "/ 3")
