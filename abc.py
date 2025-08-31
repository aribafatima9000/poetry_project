# Student Marks Analyzer

# Step 1: Take input for students
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []
    
    subjects = int(input(f"How many subjects for {name}? "))
    
    for j in range(subjects):
        score = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(score)
    
    students[name] = marks

# Step 2: Show report
print("\n===== Student Report =====")
for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    
    print(f"\nStudent: {name}")
    print(f" Marks: {marks}")
    print(f" Total: {total}")
    print(f" Average: {avg:.2f}")
    print(f" Highest: {highest}")
    print(f" Lowest: {lowest}")

# Step 3: Find topper
topper = max(students, key=lambda x: sum(students[x]))
print("\n🏆 Topper:", topper, "with total marks:", sum(students[topper]))
