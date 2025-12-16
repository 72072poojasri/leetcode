class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(10**7)

        tree = defaultdict(list)
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        NEG = -10**15

        from functools import lru_cache

        @lru_cache(None)
        def dfs(u, parentBought):
            # dp[b] = max profit with budget b
            dp = [NEG] * (budget + 1)
            dp[0] = 0

            # Merge children when u is NOT bought
            base = [0]
            for v in tree[u]:
                child_dp = dfs(v, False)
                new = [NEG] * (budget + 1)
                for i in range(len(base)):
                    for j in range(len(child_dp)):
                        if i + j <= budget and base[i] != NEG and child_dp[j] != NEG:
                            new[i + j] = max(new[i + j], base[i] + child_dp[j])
                base = new

            for b in range(len(base)):
                dp[b] = max(dp[b], base[b])

            # Option: buy u
            cost = present[u] // 2 if parentBought else present[u]
            profit = future[u] - cost

            base = [0]
            for v in tree[u]:
                child_dp = dfs(v, True)
                new = [NEG] * (budget + 1)
                for i in range(len(base)):
                    for j in range(len(child_dp)):
                        if i + j <= budget and base[i] != NEG and child_dp[j] != NEG:
                            new[i + j] = max(new[i + j], base[i] + child_dp[j])
                base = new

            for b in range(len(base)):
                if b + cost <= budget:
                    dp[b + cost] = max(dp[b + cost], base[b] + profit)

            return dp

        res = dfs(0, False)
        return max(res)