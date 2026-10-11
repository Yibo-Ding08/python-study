list=["asdfa",'asfdf',"afsojgeg","fgge"]
print(list)
list.sort(key=lambda x: len(x),reverse=True)
print(list)