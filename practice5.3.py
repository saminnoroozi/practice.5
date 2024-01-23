m=int(input("Enter m: "))
n=int(input("Enter n: "))
def shatrangi(m,n):
    for i in range(m):
        for j in range(n):
            if (i+j)%2==0:
              print("*",end=" ")
            else:
                print("#",end=" ")
        print()
shatrangi(m,n)
