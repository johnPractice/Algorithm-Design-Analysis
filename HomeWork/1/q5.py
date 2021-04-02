def get_input():
    n=int(int(input()))
    result=input()
    result=result.split(' ')
    result=list(int(t) for t in result)
    return result
    
def minus_arr(arr):
    result=[0]*(len(arr))
    for i in range(0,len(arr)):
        if i>0:
            result[i-1]=arr[i]-arr[i-1]
    return result

def check_hight_low(arr):
    count_p=1
    count_m=1
    i=len(arr)-2
    while i >=0 :
        if arr[i]>0 : 
            count_p=1+count_m
        elif arr[i]<0:
            count_m=count_p+1
        i=i-1
    return max(count_m,count_p)

def main():
    arr=get_input()
    arr_minus=(minus_arr(arr))
    print(check_hight_low(arr_minus))
if __name__=="__main__":
    main()