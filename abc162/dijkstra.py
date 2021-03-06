def dijkstra(s, n, w, cost):
    # 始点sから各頂点への最短距離
    # n : 頂点
    # w : 辺の数
    # cost[u][v] : 辺uvのコスト（存在しないときはinf）
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0

    while True:
        v = -1
        # まだ使われていない頂点の中から最小の距離をものを探す
        for i in range(n):
            if used[i] == False and v == -1:
                v = i
            elif used[i] == False and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True

        for j in range(n):
            d[j] = min(d[j], d[v] + cost[v][j])

    return d


n, w = map(int, input().split())
cost = [[float("inf") for _ in range(n)] for _ in range(n)]
for i in range(w):
    x, y, z = map(int, input().split())
    cost[x][y] = z
    cost[y][x] = z
print(dijkstra(0, n, w, cost))
