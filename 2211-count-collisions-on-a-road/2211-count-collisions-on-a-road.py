class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        
        # Remove leading L's
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        
        # Remove trailing R's
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # Count all moving cars in the remaining region
        ans = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                ans += 1
        
        return ans