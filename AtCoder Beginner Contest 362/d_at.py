class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.weightV = []
 
    def printSolution(self, dist):
        sol = []
        for node in range(self.V):
            sol.append(int(dist[node] + a[0] / 2 + a[node] / 2))
        
        print(*sol[1:])
 
    def minDistance(self, dist, sptSet):
 
        min = 2**32 - 1
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self, src):
 
        dist = [2**32 - 1] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)

n, m = (map(int, input().split()))
a = list(map(int, input().split()))
g = Graph(n)

mp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    u, v, b = (map(int, input().split()))
    x = b + (a[u - 1] + a[v - 1]) / 2
    mp[u - 1][v - 1] = x
    mp[v - 1][u - 1] = x
    

g.graph = mp
g.weightV = a
g.dijkstra(0)
