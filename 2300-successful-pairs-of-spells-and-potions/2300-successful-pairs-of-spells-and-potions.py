from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort potions for binary search
        m = len(potions)
        result = []

        for spell in spells:
            # Minimum potion strength needed
            min_potion = (success + spell - 1) // spell  # Ceiling of success / spell

            # Find index of first potion >= min_potion
            idx = bisect_left(potions, min_potion)

            # Number of successful pairs
            result.append(m - idx)

        return result
