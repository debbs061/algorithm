from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # return the fewest num of coins that you need to make up that amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1
