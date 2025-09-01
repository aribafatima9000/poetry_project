# Students dictionary
students = {
    "Ali": 78,
    "Sara": 92,
    "Ahmed": 85,
    "Fatima": 95,
    "Hassan": 88
}

# Highest marks find karna
highest_student = max(students, key=students.get)

print("Highest marks wale student:", highest_student)
print("Marks:", students[highest_student])



# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose logic
rows = len(matrix)
cols = len(matrix[0])

transpose = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

print("Original matrix:", matrix)
print("Transpose:", transpose)


# Check prime function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = [10, 11, 12, 13, 17, 20, 23, 29]
prime_list = [num for num in numbers if is_prime(num)]

print("Original list:", numbers)
print("Prime numbers:", prime_list)



sentence = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


numbers = [12, 45, 67, 23, 89, 34]

# Average
total = 0
for num in numbers:
    total += num
average = total / len(numbers)

# Max and Min
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Numbers:", numbers)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)



sentence = input("Enter a sentence: ")
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:", frequency)



import string

sentence = input("Enter a sentence: ").lower()
alphabet = set(string.ascii_lowercase)

if alphabet.issubset(set(sentence)):
    print("Yes, it is a pangram.")
else:
    print("No, it is not a pangram.")



sentence = input("Enter a sentence: ")
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:", frequency)


