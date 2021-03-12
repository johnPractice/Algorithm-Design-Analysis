
def editDistDP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j    
 
            elif j == 0:
                dp[i][j] = i   
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1]+1)    # Replace
 
    return dp[m][n]
 
 
def get_input():
    str1 = input()
    str2 = input()
    return {'str1':str1,'str2':str2}
 
def main():
    user=(get_input())
    print(editDistDP(user['str1'],user['str2'],len(user['str1']),len(user['str2'])))

if __name__ == "__main__":
    main()