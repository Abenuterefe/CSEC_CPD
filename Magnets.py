n = int(input())
last_magnet = input()
groups = 1
for _ in range(n - 1):
    magnet = input()
    if magnet != last_magnet:
        groups += 1
    last_magnet = magnet
print(groups)
