def scheduling_linear(n1,n2,t1,t2,e1,e2,x1,x2):
    n=len(n1)
    f1=[0]*(len(n1)+1)
    f2=[0]*(len(n2)+1)
    f1[1]=e1+n1[0]
    f2[1]=e2+n2[0]
    l1=[0]*(len(n1)+1)
    l2=[0]*(len(n2)+1)
    l1[0]=l1[1]=0
    l2[0]=l2[1]=0
    for j in range(2,n+1):
        if f1[j-1]+n1[j-1]<=f2[j-1]+t2[j-2]+n1[j-1]:
            f1[j]=f1[j-1]+n1[j-1]
            l1[j]=1
        else:
            f1[j]=f2[j-1]+t2[j-2]+n1[j-1]
            l1[j]=2
        if f2[j-1]+n2[j-1]<=f1[j-1]+t1[j-2]+n2[j-1]:
            f2[j]=f2[j-1]+n2[j-1]
            l2[j]=2
        else:
            f2[j]=f1[j-1]+t1[j-2]+n2[j-1]
            l2[j]=1 

    print(f1)
    print(f2)
    if f1[n]+x1<f2[n]+x2:
        print("min value {} \n road {}".format(f1[n]+x1,1))
    else:
        print("min value {} \n road {}".format(f2[n]+x2,2))
        

def main():
    # input for scheduling_linear
    # 7 9 3 4 8 4
    # 8 5 6 4 5 7
    # 2 3 1 3 4
    # 2 1 2 2 1
    # 2
    # 4
    # 3
    # 2
    n1=input("enter  line1 input:\n")
    n1=list((int(n)for n in n1.split(' ')))
    n2=input("enter  line2 input:\n")
    n2=list((int(n)for n in n2.split(' ')))
    t1=input("enter  coast1 input:\n")
    t1=list((int(n)for n in t1.split(' ')))
    t2=input("enter  coast2 input:\n")
    t2=list((int(n)for n in t2.split(' ')))
    e1=int(input("enter  base1 input:\n"))
    e2=int(input("enter  base2 input:\n"))
    x1=int(input("enter  end1 input:\n"))
    x2=int(input("enter  end2 input:\n"))
    scheduling_linear(n1,n2,t1,t2,e1,e2,x1,x2)

main()