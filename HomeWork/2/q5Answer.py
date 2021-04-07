n,k = map(int,input().split())
l=[]
for i in range(n):
    t1,t2=map(int,input().split())
    l.append((t1,t2))
#print(n,k)
# print(l)
def sort_start(t1):
    return t1[1]
def return_dis(t1):
    return t1[1]-t1[0]
def sort_sd(t1):
    return (t1[1],t1[0]-t1[1])

#print(sorted(l,key=sort_sd))
l=sorted(l,key=sort_sd)
i=0
print(l)
answered=True
while(l!=[]):
    t=l.pop()
    #print("list is {0} and i is {1}".format(l,i)) 
    if(i>k):
        answered=False
        break
    if return_dis(t)==0:
        i+=1
        if(i>k):
            answered=False
            break
    else:
        i=0
        continue
    
    
if(answered):
    print("YES")
else:
    print("NO")
    