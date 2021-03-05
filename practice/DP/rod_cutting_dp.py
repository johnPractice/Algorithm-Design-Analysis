import sys 

def max(a,b):
    return a if a>b else b

def rod_cut_dp(p,c):
    memo=[0 for i in range(c+1)]
    for i in range(0,c+1):
        max_value=0
        for j in range(i):
            print(i,j)
            max_value=max(max_value,p[j]+memo[i-j-1])
        memo[i]=max_value
        print(memo)

    return memo[c]

def main():
    n=input('please enter the  value of each rod\n')
    n=n.split(' ')
    n=list((int(x) for x in n))
    print(rod_cut_dp(n,len(n)))
    return 1

main()