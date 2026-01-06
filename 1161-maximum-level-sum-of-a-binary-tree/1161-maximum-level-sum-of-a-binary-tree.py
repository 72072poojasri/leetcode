from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        max_sum = float('-inf')
        ans_level = 1

        while q:
            level_sum = 0
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                ans_level = level

            level += 1

        return ans_level