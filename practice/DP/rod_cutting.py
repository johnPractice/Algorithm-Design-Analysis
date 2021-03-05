import sys 

def max(a,b):
    return a if a>b else b

def rod_cut(p,c):
    max_value=0
    for i in range(0,c):
        max_value=max(max_value,p[i]+rod_cut(p,c-i-1))
    return max_value

def main():
    n=input('please enter the  value of each rod\n')
    n=n.split(' ')
    n=list((int(x) for x in n))
    print(rod_cut(n,len(n)))
    return 1

main()
