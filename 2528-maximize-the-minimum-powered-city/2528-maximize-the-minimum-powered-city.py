class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        # prefix sums to compute initial power quickly
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]

        def initial_power(i):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            return pref[R + 1] - pref[L]

        # compute initial powers array
        init = [initial_power(i) for i in range(n)]

        # check if we can make every city have power >= target using at most k additions
        def can(target):
            # addDiff length must allow indexing up to pos + r + 1 where pos can be n-1
            addDiff = [0] * (n + r + 3)
            window_add = 0
            used = 0
            for i in range(n):
                window_add += addDiff[i]
                curr = init[i] + window_add
                if curr < target:
                    need = target - curr
                    used += need
                    if used > k:
                        return False
                    # place all 'need' stations at position pos = min(n-1, i + r)
                    pos = min(n - 1, i + r)
                    # they immediately affect current and future cities
                    window_add += need
                    # schedule removal after pos + r
                    end = pos + r + 1
                    addDiff[end] -= need
            return True

        low, high = 0, sum(stations) + k  # upper bound safe
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans