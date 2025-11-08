class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def helper(x):
            if x == 0:
                return 0
            msb = x.bit_length() - 1   # find most significant bit position
            mask = 1 << msb
            return (1 << (msb + 1)) - 1 - helper(x ^ mask)
        
        return helper(n)