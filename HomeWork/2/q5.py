def input_user():
    n=input()
    n=n.split(' ')
    k=int(n[1])
    n=int(n[0])
    # print(n)
    # print(k)
    inputs=[]
    for i in range(n):
        a,b=map(int,input().split())
        d=a-b
        # print(d)
        inputs.append((a,b,d))
    # print(inputs)
    return {"inputs":inputs,'k':k,'n':n}

def return_diff(a):
    return a[1]-a[0]
def sort_inputs(a):
    return sorted(a,key=lambda x :(x[1],x[2]) )
def valid_chat(i,k):
    return True if i>k else False
def check_answer(inp,k):
    i=0
    check=True
    while len(inp)!=0:
        p=inp.pop()
        # print(p)
        if valid_chat(i,k):
            check=False
            # check= not check
            break

        if return_diff(p)==0:
            i=i+1
            if valid_chat(i,k):
                check=False
                break
        else:
            i=0
    # print(check)
    return "YES" if check ==True else "NO"

def main():
    user_input=input_user()
    inputs=user_input['inputs']
    # print(inputs)
    inputs=(sort_inputs(inputs))
    number_chat=user_input['k']
    # print(number_chat)
    print(check_answer(inputs,number_chat))


if __name__ == "__main__":
    main()