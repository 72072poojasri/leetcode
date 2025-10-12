class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials and inv factorials up to m
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        # Precompute nums[i]^c for c=0..m
        pow_table = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m + 1):
                pow_table[i][c] = (pow_table[i][c - 1] * nums[i]) % MOD

        # DP arrays: dp[used][carry][ones] = sum of products of (nums^c / c!)
        # We'll use two layers for index iteration
        # Dimensions sizes: used:0..m, carry:0..m, ones:0..k
        from itertools import product

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(m + 1)]
        # start before any index: used=0, carry=0, ones=0 -> value 1
        dp[0][0][0] = 1

        for idx in range(n):
            ndp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(m + 1)]
            # iterate reachable states
            for used in range(0, m + 1):
                max_carry = m  # carry never exceeds m
                for carry in range(0, max_carry + 1):
                    for ones in range(0, k + 1):
                        base = dp[used][carry][ones]
                        if base == 0:
                            continue
                        # choose c = how many times we pick index idx
                        max_take = m - used
                        for c in range(0, max_take + 1):
                            new_used = used + c
                            cur = carry + c
                            bit = cur & 1
                            new_ones = ones + bit
                            if new_ones > k:
                                # pruning: too many ones already
                                continue
                            new_carry = cur >> 1
                            # multiply by nums[idx]^c / c!
                            add = base * pow_table[idx][c] % MOD
                            add = add * invfact[c] % MOD
                            ndp[new_used][new_carry][new_ones] = (ndp[new_used][new_carry][new_ones] + add) % MOD
            dp = ndp

        # After processing all indices, remaining carry may have bits; add popcount(carry)
        ans = 0
        for carry in range(0, m + 1):
            carry_pop = bin(carry).count("1")
            for ones in range(0, k + 1):
                total_ones = ones + carry_pop
                if total_ones != k:
                    continue
                val = dp[m][carry][ones]
                if val:
                    ans = (ans + val) % MOD

        # Multiply by m! to convert from product of (nums^c / c!) to sequences count
        ans = ans * fact[m] % MOD
        return ans