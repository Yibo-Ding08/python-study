def fb(n):
    if n==0:
        return 0
    if n==1:
        return  1
    return fb(n-1)+fb(n-2)
for i in range(0,20):
    print(fb(i))



    