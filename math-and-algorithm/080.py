class Dijkstra(object):
    """
    * edges: [(weight, vertex_1, vertex_2)]
    """

    def __init__(self, edges, n_vertex: int):
        from collections import defaultdict

        assert n_vertex > 0

        self.edges = edges
        self.n_vertex = n_vertex

        self.route = defaultdict(list)

        for e in edges:
            w, v1, v2 = e[:3]
            self.route[v1].append((w, v2))
            self.route[v2].append((w, v1))

    def dijkstra(self, start: int, goal: int):
        """ startで示す頂点からの最短経路を求める
            goal = Noneの場合は全頂点の最短距離を、
            goalに頂点番号が指定された場合はgoalまでの最短経路のみ求める。
        """
        import heapq

        assert start < self.n_vertex
        assert goal < self.n_vertex

        visited = [False] * self.n_vertex

        q = [(0, start)]
        while q:
            w, v = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True

            if v == goal:
                return w

            for wn, vn in self.route[v]:
                heapq.heappush(q, (w + wn, vn))

        return float('inf')


n, m = map(int, input().split())
edges = [None] * m
for i in range(m):
    a, b, c = map(int, input().split())
    edges[i] = (c, a, b)

dj = Dijkstra(edges, n + 1)
ans = dj.dijkstra(1, n)
if ans == float('inf'):
    print(-1)
else:
    print(ans)