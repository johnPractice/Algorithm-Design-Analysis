def max_divide(n,d):
    while n%d==0:
        n=n/d
    return n
def is_ugly(no):
    no = max_divide(no, 2)
    no = max_divide(no, 3)   
    no = max_divide(no, 5)
    return 1 if no == 1 else 0
    
def ugly_number (n):
    memo=[0]*(n)
    memo[0]=0
    memo[1]=1
    index=2
    i=2
    while i<n:
        if is_ugly(i):
           memo[index]=i
           index=index+1
           print(memo)
        i=i+1
    return memo[index-1]

def main():
    n=int(input('Enter number\n'))
    print(ugly_number(n))
    return 1

main()