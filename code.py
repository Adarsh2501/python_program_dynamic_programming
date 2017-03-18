n=input()
list=[]
n1=int(n)
for i in range(n1):
    k=input()
    list=list+[int(k)]
ans=[]
for k in range(n1):
    ans=ans+[1]
for m in range(n1-2,-1,-1):
    
    for p in range(m+1,n1,+1):
        if(list[p]%list[m]==0):
            if 1+ans[p]>ans[m]:
                ans[m]=1+ans[p]
print(max(ans))