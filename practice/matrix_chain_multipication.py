
# import sys for using big value
import sys

def min_value(d,i,j):
    # base case 
    if j<=i+1:
        return 0
    result = sys.maxsize
    for k in range(i+1,j):
        coast=min_value(d,i,k)
        coast+=min_value(d,k,j)
        coast+=d[i]*d[k]*d[j]
        if result>coast:
            result=coast

    return result

def get_input():
    dims=input('Enter the diomations...\n')
    dims=list(int(d) for d in dims.split(' '))
    print(dims)
    return dims
def main():
    d=get_input()
    print(min_value(d,0,len(d)-1))

    return 1

main()