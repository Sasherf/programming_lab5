a = list(int(x) for x in input().split())
a.sort()
middle_index = len(a) // 2
print(a[middle_index])