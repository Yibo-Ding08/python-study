a=input()
counts={}
for i in a:
    if i==" ":
        continue
    counts[i]=counts.get(i,0)+1

items=sorted(counts.items(),key=lambda x:x[1],reverse=True)
for i,n in items:
    print(f"{i}出现了{n}次")
print(items)
print(type(items))