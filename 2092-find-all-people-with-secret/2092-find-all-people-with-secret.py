from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # People who know the secret
        knows = set([0, firstPerson])
        
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            graph = defaultdict(list)
            people = set()
            
            # Collect all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1
            
            # BFS only from people who already know the secret
            queue = deque()
            visited = set()
            
            for p in people:
                if p in knows:
                    queue.append(p)
                    visited.add(p)
            
            while queue:
                cur = queue.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            
            # All visited people get the secret
            knows.update(visited)
        
        return list(knows)
