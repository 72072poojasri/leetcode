class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 0
        
        # Sum for complete weeks
        total += 28 * weeks + 7 * (weeks * (weeks - 1)) // 2
        
        # Sum for remaining days in the last week
        start = weeks + 1
        total += days * start + (days * (days - 1)) // 2
        
        return total