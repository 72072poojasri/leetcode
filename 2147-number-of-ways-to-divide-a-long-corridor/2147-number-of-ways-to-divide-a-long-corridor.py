class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = 0
        ways = 1
        plants_between = 0
        
        for ch in corridor:
            if ch == 'S':
                seats += 1
                # Multiply only AFTER the first pair
                if seats % 2 == 0 and seats > 2:
                    ways = (ways * (plants_between + 1)) % MOD
                    plants_between = 0
            else:  # ch == 'P'
                if seats % 2 == 0 and seats > 0:
                    plants_between += 1
        
        # Total seats must be even and non-zero
        if seats == 0 or seats % 2 != 0:
            return 0
        
        return ways
