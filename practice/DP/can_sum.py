def get_input():
    n=int(int(input()))
    result=input()
    result=result.split(' ')
    result=list(int(t) for t in result)
    return {"canSum":n,"arr":result}
def can_sum_func(c,a,memo):
    if c==0:
        return True
    if c<0 :
        return False
    for i in a:
        key=str(c-i)
        memo[key]=memo[key] if  key in memo else can_sum_func(c-i,a,memo)
        if  memo[key] == True:
            return True
    return False
def main():
    # memo dictionary save true or false for DP 
    memo={}
    user_input=get_input()
    can_sum=user_input['canSum'] 
    arr=user_input['arr']
    print(can_sum_func(can_sum,arr,memo))
if __name__ == "__main__":
    main()