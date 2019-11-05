num=int(input())
nums=input().split()
min=int(nums[0])
max=int(nums[0])
for i in range(num):
    if int(nums[i])>=max:
        max=int(nums[i])
    if int(nums[i])<=min:
        min=int(nums[i])
print(min,max)