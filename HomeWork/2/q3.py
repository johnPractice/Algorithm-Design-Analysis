import math
def input_user():
    n=int(input())
    return n


def change_coin(n,coins):
    m=0
    m=m+(n//coins[0])
    n=(n%coins[0])
    m=m+(n//coins[1])
    n=(n%coins[1])
    m=m+int(n/coins[2])
    return m
def main():
    # 10 5 1 coins are valid
    coins=[10,5,1]
    n=input_user()
    print(change_coin(n,coins))
    

if __name__ == "__main__":
    main()