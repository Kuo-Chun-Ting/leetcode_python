# TLE
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_count = float("inf")

        def dfs(curr_amount: int, curr_coin: int, curr_count: int):
            nonlocal min_count

            curr_amount -= curr_coin
            curr_count += 1

            if curr_amount == 0:
                min_count = min(min_count, curr_count)
                return

            elif curr_amount < 0:
                return

            else:
                for coin in coins:
                    dfs(curr_amount, coin, curr_count)

        for coin in coins:
            dfs(amount, coin, 0)

        if min_count == float("inf"):
            return -1

        return min_count
