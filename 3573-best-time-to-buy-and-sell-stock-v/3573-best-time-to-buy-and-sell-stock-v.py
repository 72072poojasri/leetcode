class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        NEG = -10**18

        # dp[t][state]
        # state: 0 = no position, 1 = long, 2 = short
        dp = [[NEG]*3 for _ in range(k+1)]
        dp[0][0] = 0

        for price in prices:
            new_dp = [row[:] for row in dp]
            for t in range(k+1):
                if dp[t][0] != NEG:
                    new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)  # start long
                    new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)  # start short

                if dp[t][1] != NEG and t < k:
                    new_dp[t+1][0] = max(new_dp[t+1][0], dp[t][1] + price)  # close long

                if dp[t][2] != NEG and t < k:
                    new_dp[t+1][0] = max(new_dp[t+1][0], dp[t][2] - price)  # close short

            dp = new_dp

        return max(dp[t][0] for t in range(k+1))