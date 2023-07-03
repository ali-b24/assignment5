N = int(input("Enter N: "))
Triangle = [[0 for i in range(N)] for j in range(N)]
Triangle[0][0]=1
Triangle[1][0]=1
for i in range(1,N):
    Triangle[i][0]=1
    for j in range(1,i+1):
        Triangle[i][j]=Triangle[i-1][j]+Triangle[i-1][j-1]
for i in range(N):
    for j in range(N):
        if Triangle[i][j]!=0:
            print(Triangle[i][j],' ',end='')
    print()