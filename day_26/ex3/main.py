with open("./file1.txt") as first:
    file1_data = first.readlines()
        
with open("./file2.txt") as second:
    file2_data = second.readlines()

result = [int(num) for num in file1_data if num in file2_data]

print(result)