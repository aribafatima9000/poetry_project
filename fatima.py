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
end = 50

print("Perfect Squares between", start, "and", end, ":")
for num in range(start, end+1):
    if int(num**0.5) ** 2 == num:
        print(num, end=" ")






nums = [1, 2, 3, 2, 4, 1, 5, 3]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Original:", nums)
print("Without Duplicates:", unique)
