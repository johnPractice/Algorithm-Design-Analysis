def get_input():
    n=int(int(input()))
    result=input()
    result=result.split(' ')
    result=list(int(t) for t in result)
    return result
    
def minus_arr(arr):
    result=[0]*(len(arr)-1)
    for i in range(0,len(arr)-1):
        result[i]=arr[i+1]-arr[i]
    return result
def check_hight_low(arr):
    result=[0]*(len(arr)+1)
    sign=True
    for i in range(0,len(arr)):
        count=0
        if arr[i]<0:
            sign=False
        elif arr[i]>0:
            sign=True
        else:
            continue
        for j in range(i+1,len(arr)):
            if sign==True and arr[j]<0:
                count=count=count+1
            elif sign==False and arr[j]>0:
                count=count+1
        result[i]=max(1,count)

    return max(result)+1
def main():
    arr=get_input()
    arr_minus=(minus_arr(arr))
    print(check_hight_low(arr_minus))
if __name__=="__main__":
    main()