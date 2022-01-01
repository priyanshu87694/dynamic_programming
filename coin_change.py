def change(amount):

    coins = [1, 3, 4]
    dp = [[int(amt) for amt in range(amount+1)] for coin in range(4)]

    for i in range(4):
        for j in range(amount+1):
            if coins[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coins[i -1]], dp[i-1][j])

    return dp[3][amount]

print(change(int(input())))