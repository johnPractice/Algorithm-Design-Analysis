import sys
def min_value(d,i,j,result):
    if j==i:
        return 0
    if result[i][j]!=-1:
        return result[i][j]
    result[i][j]=sys.maxsize
    for k in range(i,j):
        result[i][j]=min(result[i][j],(min_value(d,i,k,result)+min_value(d,k+1,j,result)+(d[i-1]*d[k]*d[j])))
    print(result)
    return result[i][j]


def get_input():
    dims=input('Enter the diomations...\n')
    dims=list(int(d) for d in dims.split(' '))
    # print(dims)
    return dims
def main():
    d=get_input()
    result=[[-1] *len(d)]*len(d)
    print(min_value(d,1,len(d)-1,result))
    return 1

main()