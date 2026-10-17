list=[12, 7, 5, 12, 9, 7, 7, 3]
num_max=max(list)
print(num_max)
num_min=min(list)
print(num_min)
print(list)
list.sort()
nums=[]
for i in list:
    if i  not in nums:
        nums.append(i)
nums.sort()
print(nums)