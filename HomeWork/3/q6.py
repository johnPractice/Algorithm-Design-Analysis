
symbol_object={'.':".",'*':"*"}
def get_user_input():
    n=input().split(' ')
    row,column=map(lambda x:int(x),n)
    return {'row':row,'column':column}

def check(r,c):
    arr = []
    result = 0
    resultArr = []
    temp = []
    for i in range(c):
        temp.append(0)
    v_list = []
    for i in range(0, c):
        v_list.append([])
        for j in range(0, c):
            v_list[i].append(0)
    for x in range(r):
        arr.append([y for y in input()])

    for x in range(r):
        temp = [0 for i in range(c)]
        for y in range(c):
            result = 0
            v_list = [[0 for i in range(c)] for j in range(r)]
            symbol=symbol_object[arr[x][y] ]
            if symbol == symbol_object['*']:
                result += 1
                result = travers(arr, x, y, result, r, c, v_list)
                result %= 10
                temp[y] = str(result)
            symbol=symbol_object[arr[x][y] ]
            if arr[x][y] == '.':
                temp[y] = "."

        resultArr.append(temp)

    return {'result':resultArr,'r':r,'c':c}


def print_result(v):
    result=''
    r=v['r']
    c=v['c']
    arr=v['result']
    for x in range(r):
        for y in range(c):
            result=result+str(arr[x][y])+''
        result=result+'\n'
    return result
def main():
    n=get_user_input()
    r=n['row']
    c=n['column']
    v=check(r,c)
    print(print_result(v))


# give help
def travers(arr, x, y, result, r, c, v_list):
    if y + 1 < c:
        if arr[x][y + 1] == '.':
            if v_list[x][y + 1] == 0:
                result += 1
                v_list[x][y + 1] = 1
                result = travers(arr, x, y + 1, result, r, c, v_list)


    if y - 1 >= 0:
        if arr[x][y - 1] == '.':
            if v_list[x][y - 1] == 0:
                result += 1
                v_list[x][y - 1] = 1
                result = travers(arr, x, y - 1, result, r, c, v_list)

    if x + 1 < r:
        if arr[x + 1][y] == '.':
            if v_list[x + 1][y] == 0:
                result += 1
                v_list[x + 1][y] = 1
                result = travers(arr, x + 1, y, result, r, c, v_list)

    if x - 1 >= 0:
        if arr[x - 1][y] == '.':
            if v_list[x - 1][y] == 0:
                result += 1
                v_list[x - 1][y] = 1
                result = travers(arr, x - 1, y, result, r, c, v_list)

    return result



if __name__ == '__main__':
    main()