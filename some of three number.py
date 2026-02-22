nums=[-100,-70,-60,110,120,130,160] 
nums.sort()
s=set()
target=0
output=[]
for i in range(len(nums)):
    j=i+1
    k=len(nums)-1
    while(j<k):
        sum=nums[i]+nums[j]+nums[k]
        if(sum==target):
            s.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1
        elif(target>sum):
            k-=1
        else:
            j+=1
    
output=list(s)
print(output)

      
        