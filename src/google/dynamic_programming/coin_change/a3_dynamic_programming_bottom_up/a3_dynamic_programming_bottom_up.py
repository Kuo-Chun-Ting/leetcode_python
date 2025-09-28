class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            min_coin_num = float("inf")
            for coin in coins:
                if i < coin:
                    continue

                min_coin_num = min(min_coin_num, dp[i - coin] + 1)
            dp[i] = min_coin_num

        if dp[amount] == float("inf"):
            return -1

        return int(dp[amount])
