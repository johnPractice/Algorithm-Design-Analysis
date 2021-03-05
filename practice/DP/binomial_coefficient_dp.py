def binomial_coefficient_dp(n,k):
    memo=[[0 for x in range(k+1)]  for y in range(n+1)]
    for i in range(n+1): 
        for j in range(min(i,k)+1):
            if i == j:
                memo[i][j]=1
            else:
                memo[i][j]=memo[i-1][j-1]+memo[i-1][j]
    return memo[n][k]

n=int(input("enter n : \n"))
k=int(input("enter k : \n"))
print(binomial_coefficient_dp(n,k))


