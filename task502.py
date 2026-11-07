s = input()
min_digit = min(s)

index = s.find(min_digit)
result = s[:index] + s[index+1:]

print(result)