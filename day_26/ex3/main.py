with open("./file1.txt") as first:
    file1_data = first.readlines()
    file1 = [int(num.strip()) for num in file1_data]
        
with open("./file2.txt") as second:
    file2_data = second.readlines()
    file2 = [int(num.strip()) for num in file2_data]

result = [num for num in file1 if num in file2]

print(result)