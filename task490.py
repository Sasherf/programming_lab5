a = list(int(x) for x in input().split())
k = int(input())

length = len(a)
k = k % length

a[:] = a[-k:] + a[:-k]

for elements in a:
    print(elements, end=" ")