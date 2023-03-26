import math
from heapq import heapify, heappop, heappush

class Node:
    def __init__(self) -> None:
        self.n_in = 0
        self.data = 0
        self.edges = []


class Graph:
    def __init__(self, n) -> None:
        self.nodes = [Node() for i in range(n)]
        self.n = n

    def add_edge(self, u, v):
        self.nodes[u].edges.append(v)
        self.nodes[v].n_in += 1

    def dfs(self, v, visited, post):
        visited[v] = True
        for u in self.nodes[v].edges:
            if not visited[u]:
                self.dfs(u, visited, post)
        post.append(v)

    def toposort(self):
        visited = [False for i in range(self.n)]
        post = []
        for i in range(self.n):
            if not visited[i]:
                self.dfs(i, visited, post)
        post.reverse()
        return post

    def get_max_fun(self):
        fun = [None for j in range(self.n)]
        for i in range(self.n):
            fun[i] = [-math.inf for j in range(self.nodes[i].n_in - 1)]
            fun[i].append(self.nodes[i].data)
        post = self.toposort()
        for v in post:
            s = 0
            for j in fun[v]:
                s += j
            for u in self.nodes[v].edges:
                m = 0
                for k in range(len(fun[u])):
                    if fun[u][k] < fun[u][m]:
                        m = k
                fun[u][m] = max(fun[u][m], s)
        s = 0
        for i in fun[0]:
            s += i
        return s


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self):
        self.t = int(input())
        for i in range(self.t):
            # Create graph
            n = int(input())
            line = input().split(' ')
            g = Graph(n + 1)
            g.nodes[0].data = 0
            for j in range(len(line)):
                g.nodes[j + 1].data = int(line[j])
            # Add edges
            line = input().split(' ')
            for j in range(len(line)):
                g.add_edge(j + 1, int(line[j]))
            fun = g.get_max_fun()
            print("Case #{}: {}".format(i + 1, fun))


sol = Solution()
sol.solve()