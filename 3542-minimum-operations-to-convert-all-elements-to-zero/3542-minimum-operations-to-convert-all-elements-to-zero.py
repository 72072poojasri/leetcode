import bisect
import sys
sys.setrecursionlimit(1_000_000)

class SegmentTree:
    # store (value, index) with comparison by value, then index
    def __init__(self, arr):  # <-- fixed: __init__ (double underscores)
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [(10**18, -1)] * (2 * size)
        for i, v in enumerate(arr):
            self.tree[size + i] = (v, i)
        for i in range(size - 1, 0, -1):
            left = self.tree[2 * i]
            right = self.tree[2 * i + 1]
            if left[0] < right[0] or (left[0] == right[0] and left[1] < right[1]):
                self.tree[i] = left
            else:
                self.tree[i] = right

    def range_min(self, l, r):
        # inclusive l, r
        l += self.size
        r += self.size
        best = (10**18, -1)
        while l <= r:
            if (l & 1) == 1:
                a = self.tree[l]
                if a[0] < best[0] or (a[0] == best[0] and a[1] < best[1]):
                    best = a
                l += 1
            if (r & 1) == 0:
                a = self.tree[r]
                if a[0] < best[0] or (a[0] == best[0] and a[1] < best[1]):
                    best = a
                r -= 1
            l //= 2
            r //= 2
        return best


class Solution:
    def minOperations(self, nums):
        n = len(nums)
        if all(v == 0 for v in nums):
            return 0

        # build positions map: value -> sorted list of indices
        posmap = {}
        for i, v in enumerate(nums):
            posmap.setdefault(v, []).append(i)

        zeros = posmap.get(0, [])

        seg = SegmentTree(nums)
        from functools import lru_cache

        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            # if there is any zero in [l, r], split by zeros and sum
            if zeros:
                i = bisect.bisect_left(zeros, l)
                if i < len(zeros) and zeros[i] <= r:
                    res = 0
                    start = l
                    while i < len(zeros) and zeros[i] <= r:
                        z = zeros[i]
                        if start <= z - 1:
                            res += dp(start, z - 1)
                        start = z + 1
                        i += 1
                    if start <= r:
                        res += dp(start, r)
                    return res

            # no zeros in [l, r]
            option1 = r - l + 1

            mn_val, _ = seg.range_min(l, r)
            poslist = posmap[mn_val]
            lb = bisect.bisect_left(poslist, l)
            ub = bisect.bisect_right(poslist, r)
            positions = poslist[lb:ub]

            if not positions:
                return option1

            cost = 1
            start = l
            for p in positions:
                if start <= p - 1:
                    cost += dp(start, p - 1)
                start = p + 1
            if start <= r:
                cost += dp(start, r)

            return min(option1, cost)

        return dp(0, n - 1)
