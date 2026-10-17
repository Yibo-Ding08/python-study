def is_prime(n):
    num=0
    for i in range(1,n+1):
        if n/i in range(1,n+1):
            num+=1
    if num==2:
        print(f"{n}是质数")
    else:
        print(f"{n}不是质数")
for i in range(1,101):
    is_prime(i)

