list = []
elements = [int(x) for x in input().split()]

for element in elements:
    list.append(element)

max = max(list)
index = list.index(max)

print(max, index)