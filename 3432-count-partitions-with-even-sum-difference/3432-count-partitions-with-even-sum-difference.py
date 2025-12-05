class Solution:
    def countPartitions(self, nums):
        total = sum(nums)
        n = len(nums)
        
        # If total sum is odd, no partition yields even difference
        if total % 2 == 1:
            return 0
        
        # Otherwise all partitions yield even difference
        return n - 1