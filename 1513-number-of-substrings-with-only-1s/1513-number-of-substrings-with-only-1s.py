class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        ans = 0
        count = 0
        for c in s:
            if c == '1':
                count += 1
            else:
                ans = (ans + count*(count+1)//2) % mod
                count = 0
        ans = (ans + count*(count+1)//2) % mod
        return ans