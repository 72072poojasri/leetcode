class Solution:
    def countTrapezoids(self, points):
        from collections import defaultdict
        MOD = 10**9 + 7

        ycount = defaultdict(int)
        for x, y in points:
            ycount[y] += 1

        comb = []
        for y in ycount:
            c = ycount[y]
            if c >= 2:
                comb.append(c * (c - 1) // 2)

        if len(comb) < 2:
            return 0

        comb.sort()

        total = 0
        prefix = 0
        for v in comb:
            total = (total + prefix * v) % MOD
            prefix = (prefix + v) % MOD

        return total % MOD