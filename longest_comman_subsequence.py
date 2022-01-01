a = int(input())
X = input().split()
b = int(input())
Y = input().split()

dp = [[0 for j in range(b+1)] for i in range(a+1)]

for i in range(a+1):
    for j in range(b+1):
        if i==0 or j==0:
            dp[i][j] = 0
        elif X[i-1] == Y[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[a][b])