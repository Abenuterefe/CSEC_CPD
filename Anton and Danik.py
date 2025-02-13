def find_winner(n, s):
    count_A = s.count('A')
    count_D = s.count('D')

    if count_A > count_D:
        print("Anton")
    elif count_A < count_D:
        print("Danik")
    else:
        print("Friendship")
n = int(input())
s = input().strip()
find_winner(n, s)
