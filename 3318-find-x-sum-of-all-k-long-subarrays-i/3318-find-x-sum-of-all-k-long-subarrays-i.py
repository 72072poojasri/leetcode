from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)

            # Sort by frequency (descending), then value (descending)
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))

            # Take top x elements
            top_x = set(num for num, _ in sorted_items[:x])

            # Sum only elements in top_x
            total = sum(num for num in sub if num in top_x)
            ans.append(total)

        return ans
