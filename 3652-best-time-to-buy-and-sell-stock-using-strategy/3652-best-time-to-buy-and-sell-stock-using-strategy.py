class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)

        # Original profit
        original_profit = 0
        for i in range(n):
            original_profit += strategy[i] * prices[i]

        half = k // 2

        # Prefix sums
        strat_val = [strategy[i] * prices[i] for i in range(n)]
        sell_val = [prices[i] for i in range(n)]

        pref_strat = [0] * (n + 1)
        pref_sell = [0] * (n + 1)

        for i in range(n):
            pref_strat[i + 1] = pref_strat[i] + strat_val[i]
            pref_sell[i + 1] = pref_sell[i] + sell_val[i]

        best_gain = 0

        for l in range(0, n - k + 1):
            mid = l + half
            r = l + k

            # Old contribution
            old = pref_strat[r] - pref_strat[l]

            # New contribution
            new = pref_sell[r] - pref_sell[mid]

            gain = new - old
            best_gain = max(best_gain, gain)

        return original_profit + best_gain