def shortestDistance(N,M,A,X,Y):
    #code here
    flag = False
    print("Hello")
    def dfs(i,j,m,n):
        print(i,j)
        if i<0 or i>N or j<0 or j>M or A[i][j]==0:
            print("Here")
            return float('inf')
        if (i,j)==(m,n):
            return 0
        up = dfs(i-1,j,m,n)
        down = dfs(i+1,j,m,n)
        left = dfs(i,j-1,m,n)
        right = dfs(i,j+1,m,n)
        
        return 1+min(up,down,left,right)
    return dfs(0,0,X,Y)

N=3
M=4
A=[
    [1,0,0,0], 
    [1,1,0,1],
    [0,1,1,1]
]
X=2
Y=3 
print(shortestDistance(N,M,A,X,Y))