num = int(input("Enter a number: "))
rev = 0
temp = num

# Reverse logic
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed Number:", rev)

# Palindrome check
if num == rev:
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")



# Sentence me longest aur shortest word find karna

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = max(words, key=len)
shortest = min(words, key=len)

print("Longest word:", longest)
print("Shortest word:", shortest)
     



a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

merged = a.copy()
for x in b:
    if x not in merged:
        merged.append(x)

print("Merged List (No Duplicates):", merged)






matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = 0
for i in range(len(matrix)):
    s += matrix[i][i]

print("Diagonal Sum:", s)




# Duplicates remove karne ka program

numbers = [12, 23, 34, 12, 45, 23, 56, 34, 67]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)




nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
duplicates = []

for n in nums:
    if nums.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print("Duplicate Elements:", duplicates)




numbers = [10, 3, 5, 12, 17, 20, 23, 29, 30]
prime_list = []

for num in numbers:
    if num > 1:   # Prime sirf 1 se bade hote hain
        is_prime = True
        for i in range(2, num):   # 2 se num-1 tak check karna
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)

print("Original List:", numbers)
print("Prime Numbers List:", prime_list)





matrix = [
    [1, 22, 56],
    [67, 78, 90],
    [12, 34, 56]
]

for row in matrix:          # Har row ke liye
    for element in row:     # Row ke har element ke liye
        print(element, end=" ")
    print()   # New line after each row




matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transpose = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose:")
for r in transpose:
    print(r)





text = "programming"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)





num = 153
power = len(str(num))
total = sum(int(digit)**power for digit in str(num))
if total == num:
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")




numbers = [12, 45, 23, 67, 34, 89]
first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)




numbers = [12, 45, 23, 67, 34, 89]
first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)


