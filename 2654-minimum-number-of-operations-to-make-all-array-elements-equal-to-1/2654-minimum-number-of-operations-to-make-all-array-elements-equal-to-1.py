from math import gcd

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        overall_gcd = nums[0]
        for num in nums:
            overall_gcd = gcd(overall_gcd, num)
        
        # If gcd of all numbers > 1 → impossible
        if overall_gcd != 1:
            return -1
        
        # Case 1: already has at least one '1'
        if 1 in nums:
            return n - nums.count(1)
        
        # Case 2: need to create a '1'
        min_len = float('inf')
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        # (min_len - 1) to create 1 + (n - 1) to make all 1
        return (min_len - 1) + (n - 1)