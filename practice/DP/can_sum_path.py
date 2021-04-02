def get_input():
    n=int(int(input()))
    result=input()
    result=result.split(' ')
    result=list(int(t) for t in result)
    return {"canSum":n,"arr":result}
def can_sum_func(c,a,memo):
    if c==0:
        return []
    if c<0 :
        return None
    for i in a:
        reminder=c-i
        key=str(reminder)
        memo[key]=memo[key] if key in memo else can_sum_func(reminder,a,memo)
        if  memo[key] != None:
            memo[key].append(i)
            return  memo[key]
    return None
        
def main():
    # memo dictionary save true or false for DP 
    memo={}
    user_input=get_input()
    can_sum=user_input['canSum'] 
    arr=user_input['arr']
    print(can_sum_func(can_sum,arr,memo))
if __name__ == "__main__":
    main()