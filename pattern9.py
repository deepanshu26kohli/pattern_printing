n=5
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n*2-i*2-1):
        print("*",end="")
    for k in range(0,i):
        print(" ",end="")
    print("\n")