def get_input():
    n=int(int(input()))
    result=input()
    result=result.split(' ')
    result=list(int(t) for t in result)
    return {"canSum":n,"arr":result}
def best_sum(c,a,memo):
    # if str(c) in memo :return memo[str(c)]
    if c==0:return []
    if c<0 :return None
    smallest_sum=None
    for i in a:
        reminder=c-i
        result= best_sum(reminder,a,memo)
        if result!=None:
            result.append(i)
            if smallest_sum==None or len(result)<len(smallest_sum):
                smallest_sum=result
    # memo[str(c)]=smallest_sum
    return smallest_sum
        
def main():
    # memo dictionary save true or false for DP 
    memo={}
    user_input=get_input()
    can_sum=user_input['canSum'] 
    arr=user_input['arr']
    print(best_sum(can_sum,arr,memo))
    # best_sum(can_sum,arr,memo)
    # print(memo)

if __name__ == "__main__":
    main()