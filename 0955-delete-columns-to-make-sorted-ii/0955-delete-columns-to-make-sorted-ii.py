class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        
        deleted = 0
        sorted_pair = [False] * (n - 1)

        for col in range(m):
            bad = False
            
            # Check if this column breaks ordering
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break
            
            if bad:
                deleted += 1
                continue
            
            # Update sorted pairs
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

        return deleted