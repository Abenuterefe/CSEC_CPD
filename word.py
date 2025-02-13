s = input()
uppercase_count = 0
for c in s:
    if c.isupper():
        uppercase_count += 1

if uppercase_count > len(s) // 2:
    print(s.upper())
else:
    print(s.lower())
