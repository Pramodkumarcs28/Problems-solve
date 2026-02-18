arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
maxi=0
choice=0
jumps=0
for i in range(len(arr)-1):
    maxi=max(maxi,arr[i]+i)
    if i==choice:
        jumps+=1
        choice=maxi
if choice<len(arr)-1:
    print(-1)
print(jumps)





