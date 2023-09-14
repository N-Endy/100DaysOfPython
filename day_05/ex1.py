student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heigth = 0
count = 0
for height in student_heights:
    total_heigth += height
    count += 1
avg_height = total_heigth / count
print(avg_height)