import sys
def get_input():
    n=int(int(input()))
    result=input()
    result=result.split(' ')
    result=list(int(t) for t in result)
    return result
def find_min(arr,mins):
    mins[0]=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<mins[i-1]:
            mins[i]=arr[i]
        else:mins[i]=mins[i-1]
def find_best(arr,mins,best):
    for i in range(1,len(arr)):
        if i==1:
            best[i-1]=arr[i]-mins[i]
        else:
            best[i-1]=max(best[i-2],arr[i]-mins[i])
    

def split_memo():
    arr=get_input()
    if len(arr)==1:return 0
    l=[]
    for k in range(1,len(arr)):
        l.append(main(arr[:k])+main(arr[k:]))
    print(l)
    return max(l)




    

def main(arr):
    mins=[sys.maxsize]*len(arr)
    find_min(arr,mins)
    best=[0]*(len(arr)-1 if len(arr) >1 else 1)
    find_best(arr,mins,best)
    # print(mins)
    # print(best)
    return max(best)
    



if __name__=="__main__":
    print(split_memo())