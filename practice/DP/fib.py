def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    n=int(input('enter your nimber\n'))
    print(fib(n))
    return 1

main()