# 1. Hello User Program
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Even/Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. Simple Interest Calculator
p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (in years): "))
si = (p * r * t) / 100
print("Simple Interest:", si)

# 4. Temperature Converter
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("In Fahrenheit:", f)

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5/9
print("In Celsius:", c)

# 5. Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
print("Your age is:", age)

# 6. Table Generator
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 7. Factorial Finder
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# 8. Word Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words:", len(words))

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are NOT eligible to vote.")
