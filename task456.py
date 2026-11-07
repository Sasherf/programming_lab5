result = []
binary_list = input().split(",")

for num in binary_list:
    dec = int(num, 2)
    
    if dec % 5 == 0:
        result.append(num)

print(",".join(result))