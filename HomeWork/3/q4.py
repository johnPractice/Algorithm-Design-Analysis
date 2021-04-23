import sys
sys.setrecursionlimit(10**6)

def get_input():
    n,s,a,b=map(lambda x: int(x),input().split(','))
    return {'n':n,'s':s,'a':a,'b':b}

def check_step(n,s,a,b,r):
    if s>n or s<1 or s in r: 
        return
    else:
        r.add(s)
        check_step(n,s-a,a,b,r)
        check_step(n,s-b,a,b,r)
        check_step(n,s+a,a,b,r)
        check_step(n,s+b,a,b,r)



def main():
    result=set()
    n=get_input()
    s=n['s']
    a=n['a']
    b=n['b']
    n=n['n']
    check_step(n,s,a,b,result)
    print(len(result))
    result=(sorted(result))
    out_put=''
    for r in result:
        out_put=out_put+str(r)+' '
    print(out_put)

if __name__ == "__main__":
    main()