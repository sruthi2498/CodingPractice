n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
    
if n==1:
    print(arr[0])
print("------")
opt=[0 for _ in range(n)]
opt[0]=arr[0]
for i in range(1,n):
    v=arr[i]
    for j in range(0,i):
        b = arr[j]+opt[j]
        #print(b)
        if b>v:
            v=b
    opt[i]=v
print(opt)