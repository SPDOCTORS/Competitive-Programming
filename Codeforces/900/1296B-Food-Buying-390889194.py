t=int(input())
for _ in range(t):
    s=int(input())
    money=s
    total=0
    while money>=10:
        cashback=money//10
        remaining=money%10
        spent=money-remaining
        money=cashback+remaining
        total+=spent
    total+=money
    print(total)