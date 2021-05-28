def linear_search(datas:list,find:int):
    result=0
    for d in datas:
        if d==find:
            return result
        else: result+=1
    return -1

def main():
    datas=map(lambda x: int(x),input().split(' '))
    find=int(input())
    print(linear_search(datas,find))
if __name__ == "__main__":
    main()