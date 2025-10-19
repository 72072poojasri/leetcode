class Solution:
    def findLexSmallestString(self, s, a, b):
        from collections import deque
        seen = set([s])
        q = deque([s])
        res = s
        while q:
            cur = q.popleft()
            res = min(res, cur)
            t1 = list(cur)
            for i in range(1, len(t1), 2):
                t1[i] = str((int(t1[i]) + a) % 10)
            t1 = ''.join(t1)
            if t1 not in seen:
                seen.add(t1)
                q.append(t1)
            t2 = cur[-b:] + cur[:-b]
            if t2 not in seen:
                seen.add(t2)
                q.append(t2)
        return res