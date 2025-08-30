num = 28
s = 0

for i in range(1, num):
    if num % i == 0:
        s += i

if s == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")




num = 28

print("Factors of", num, ":")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")


text = "abc"

for i in range(len(text)):
    for j in range(i+1, len(text)+1):
        print(text[i:j])
sentence = "Python makes programming easy and powerful"
words = sentence.split()
largest = ""

for w in words:
    if len(w) > len(largest):
        largest = w

print("Largest word:", largest)




sentence = "Python makes programming easy and powerful"
words = sentence.split()
count = 0

for _ in words:
    count += 1

print("Total words:", count)




nums = [1,2,2,3,4,3,5,1,2]
freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)
  






nums = [5, 7, 2, 8, 1, 3]
first = second = float('-inf')
smallest = second_smallest = float('inf')

for n in nums:
    # largest logic
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

    # smallest logic
    if n < smallest:
        second_smallest = smallest
        smallest = n
    elif n < second_smallest and n != smallest:
        second_smallest = n

print("Second Largest:", second)
print("Second Smallest:", second_smallest)







nums = [1, 2, 3, 2, 4, 1, 5, 3]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Original:", nums)
print("Without Duplicates:", unique)








start = 1
end = 500

print("Armstrong Numbers between", start, "and", end, ":")
for num in range(start, end+1):
    power = len(str(num))
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** power
        temp //= 10
    if s == num:
        print(num, end=" ")







start = 1
end = 50

print("Perfect Squares between", start, "and", end, ":")
for num in range(start, end+1):
    if int(num**0.5) ** 2 == num:
        print(num, end=" ")
  





  # List of numbers
numbers = [10, 20, 30, 40, 50]

# Initialize variables
total = 0
count = 0

# Loop through each number
for num in numbers:
    total += num
    count += 1

# Calculate average
average = total / count

# Output
print("Numbers:", numbers)
print("Sum =", total)
print("Average =", average)








