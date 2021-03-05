def binomial_coefficient(n,k):
    if k==n or k==0:
        return 1
    else:
       return binomial_coefficient(n-1,k-1)+binomial_coefficient(n-1,k)

n=int(input("enter n : \n"))
k=int(input("enter k : \n"))
print(binomial_coefficient(n,k))