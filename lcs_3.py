a = int(input())
X = input().split()
b = int(input())
Y = input().split()
c = int(input())
Z = input().split()


dp = [[[0 for k in range(c+1)] for j in range(b+1)] for i in range(a+1)]

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i==0 or j==0 or k==0:
                dp[i][j][k] = 0
            elif X[i-1] == Y[j-1] == Z[k-1]:
                dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[a][b][c])