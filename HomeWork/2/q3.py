def input_user():
    n=int(input())
    return n


def change_coin(n,coins):
    i=0
    m=0
    while n>=0 and i <len(coins):
        if n>=coins[i]:
            m+=1
            n=n-coins[i]
        else:
            i+=1
    return m
def main():
    # 10 5 1 coins are valid
    coins=[10,5,1]
    n=input_user()
    print(change_coin(n,coins))
    

if __name__ == "__main__":
    main()