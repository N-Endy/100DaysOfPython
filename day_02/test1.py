num = input("Input a 2 digit number: ")
while len(num) > 2:
    num = input("Input a 2 digit number: ")
result = int(num[0]) + int(num[1])
print(result)