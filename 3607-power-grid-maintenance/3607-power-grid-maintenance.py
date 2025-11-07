from sortedcontainers import SortedSet

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        # online_nodes[i] is the set of online nodes in the component whose root is i
        self.online_nodes = [SortedSet([i]) for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

        # Merge online node sets: merge smaller into larger for efficiency
        if len(self.online_nodes[rb]) > len(self.online_nodes[ra]):
            self.online_nodes[ra], self.online_nodes[rb] = self.online_nodes[rb], self.online_nodes[ra]
        self.online_nodes[ra].update(self.online_nodes[rb])
        self.online_nodes[rb].clear()

    def go_offline(self, x):
        r = self.find(x)
        if x in self.online_nodes[r]:
            self.online_nodes[r].remove(x)

    def get_min_online(self, x):
        r = self.find(x)
        if x in self.online_nodes[r]:
            return x
        if not self.online_nodes[r]:
            return -1
        return self.online_nodes[r][0]


class Solution:
    def processQueries(self, c, connections, queries):
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        result = []
        for t, x in queries:
            if t == 1:
                result.append(dsu.get_min_online(x))
            else:
                dsu.go_offline(x)
        return result