from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] = number of ways to partition nums[0..i-1]
        dp = [0] * (n + 1)
        dp[0] = 1

        # prefix[i] = sum(dp[0..i])  (so prefix[0] = dp[0])
        prefix = [0] * (n + 1)
        prefix[0] = dp[0]

        max_dq = deque()  # indices with decreasing nums[]
        min_dq = deque()  # indices with increasing nums[]
        left = 0

        for right in range(n):
            # push right into max_dq (decreasing)
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()
            max_dq.append(right)

            # push right into min_dq (increasing)
            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()
            min_dq.append(right)

            # move left until window [left..right] is valid
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                if max_dq and max_dq[0] == left:
                    max_dq.popleft()
                if min_dq and min_dq[0] == left:
                    min_dq.popleft()
                left += 1

            # dp[right+1] is sum of dp[left]..dp[right]
            sum_left_to_right = prefix[right] - (prefix[left-1] if left > 0 else 0)
            dp[right+1] = sum_left_to_right % MOD

            # update prefix
            prefix[right+1] = (prefix[right] + dp[right+1]) % MOD

        return dp[n] % MOD
