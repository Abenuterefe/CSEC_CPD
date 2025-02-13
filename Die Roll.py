Y, W = map(int, input().split())
max_points = max(Y, W)
prob = 6 - max_points + 1
gcd = 1
for i in range(1, prob + 1):
    if prob % i == 0 and 6 % i == 0:
        gcd = i
numerator = prob // gcd
denominator = 6 // gcd
print(f"{numerator}/{denominator}")
