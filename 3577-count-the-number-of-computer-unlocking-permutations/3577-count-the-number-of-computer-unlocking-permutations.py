class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)

        # check if complexity[0] is strictly the smallest
        base = complexity[0]
        for i in range(1, n):
            if complexity[i] <= base:
                return 0

        # compute (n-1)! % MOD
        fact = 1
        for x in range(1, n):
            fact = (fact * x) % MOD
        
        return fact