def main():
    n=int(input('Enter number\n'))
    print(dp_fib(n))
    return 1
def dp_fib(n):
    memo=[0]*(n+1)
    memo[0]=memo[1]=1
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n]

main()