def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)
result=jc(5)
print(result)