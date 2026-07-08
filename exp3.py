import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX

        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1

        return True


def kruskal(n, edges):
    edges.sort()

    uf = UnionFind(n)
    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


def prim(n, adj, start=0):
    INF = float('inf')

    key = [INF] * n
    parent = [-1] * n
    inMST = [False] * n

    key[start] = 0

    priority_queue = [(0, start)]

    mst = []
    total_cost = 0

    while priority_queue:
        weight, u = heapq.heappop(priority_queue)

        if inMST[u]:
            continue

        inMST[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            total_cost += weight

        for v, wt in adj.get(u, []):
            if not inMST[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(priority_queue, (wt, v))

    return mst, total_cost


n = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]

adj = {}

for weight, u, v in edges:
    adj.setdefault(u, []).append((v, weight))
    adj.setdefault(v, []).append((u, weight))

kruskal_mst, kruskal_cost = kruskal(n, edges[:])
prim_mst, prim_cost = prim(n, adj)

print("Kruskal's MST")

for u, v, weight in kruskal_mst:
    print(f"Edge ({u} - {v}) Weight = {weight}")

print("Total Cost =", kruskal_cost)

print()

print("Prim's MST")

for u, v, weight in prim_mst:
    print(f"Edge ({u} - {v}) Weight = {weight}")

print("Total Cost =", prim_cost)