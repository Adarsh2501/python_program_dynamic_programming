n=int(input())
list=[]
for i in range(n):
    k=int(input())
    list.append(k)
ans=[]
for k in range(n1):
    ans.append(1)
for m in range(n1-2,-1,-1):
    for p in range(m+1,n1,+1):
        if(list[p]%list[m]==0):
            if 1+ans[p]>ans[m]:
                ans[m]=1+ans[p]
print(max(ans))
