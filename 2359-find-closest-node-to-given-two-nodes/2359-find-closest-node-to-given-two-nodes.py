class Solution:
    
    def bfs(self,graph,n,start):
        queue = [(start,0)]
        visited = set()
        distances = [-1 for _ in range(n)]
        while queue:
            node,dist = queue.pop()
            distances[node]=dist
            visited.add(node)
            for neighb in graph[node]:
                if neighb not in visited:
                    queue.append((neighb,dist+1))
        return distances
    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = {i:[] for i in range(n)}
        for i,a in enumerate(edges):
            if a>-1:
                graph[i].append(a)
        print(graph)
        dist1 = self.bfs(graph,n,node1)
        dist2 = self.bfs(graph,n,node2)
        print(node1,dist1)
        print(node2,dist2)
        minDist = math.inf
        minNode = -1
        for i,(a,b) in enumerate(list(zip(dist1,dist2))):
            if a>=0 and b>=0:
                dist = max(a,b)
                if dist<minDist:
                    minDist=dist
                    minNode = i
        return minNode
        
        
        