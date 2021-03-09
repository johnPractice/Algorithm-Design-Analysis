def get_user_input():
    return int(input())
def count_friend(m,n):
    for i in range(n+1):
        if i <=2:
            m[i]=i
        else:
            m[i]=m[i-1]+(i-1)*m[i-2]

        
    # print(m)
    return m[n]
    
def main():
    n=get_user_input()
    m=[0]*(n+1)
    m[1]=1
    print(count_friend(m,n))

if __name__ == "__main__":
    main()