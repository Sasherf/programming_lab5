list1 = [int(x) for x in input("First list: ").split(",")]
list2 = [int(x) for x in input("Second list: ").split(",")]

intersection = sorted(list(set(list1) & set(list2)))

for elements in intersection:
    print(elements, end=" ")