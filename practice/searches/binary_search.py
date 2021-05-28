from math import ceil
def binary_search(datas:list,find:int):
    # first need sort array
    datas.sort()  
    start=0
    end=len(datas)
    mid=ceil((start+end)/2)
    while start!=end:
        print(mid)
        check_data=datas[mid]
        if check_data==find:
            return {"result":mid,"list":datas}
        elif check_data>find:
            end=mid-1
            mid=ceil((start+end)/2)
        elif check_data<find:
            start=mid+1
            mid=ceil((start+end)/2)
    return -1

def main():
    datas=list(map(lambda x: int(x),input().split(' ')))
    find=int(input())
    print(binary_search(datas,find))
if __name__ == "__main__":
    main()