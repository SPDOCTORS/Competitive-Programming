t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    first_a = -1
    last_b = -1

    for i in range(n):
        if s[i] == "A":
            first_a = i
            break

    for i in range(n - 1, -1, -1):
        if s[i] == "B":
            last_b = i
            break

    if first_a != -1 and last_b != -1 and first_a < last_b:
        print(last_b - first_a)
    else:
        print(0)