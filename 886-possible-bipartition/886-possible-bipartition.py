class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i:[] for i in range(1,n+1)}
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)
        
        
        visited = set()
        queue = []
        first = set()
        second = set()
        
        for i in range(1,n+1):
            if i not in visited:
                queue.append(i)
                first.add(i)
            while queue:
                node = queue.pop()
                # print("node",node)
                visited.add(node)

                for neighb in graph[node]:
                    if neighb not in visited:
                        # print("\tunvisited neighb ",neighb)
                        queue.append(neighb)
                        if node in first:
                            second.add(neighb)
                        else:
                            first.add(neighb)
                # print("first",first,"second",second)
                    
        # print(first,second)
        for a,b in dislikes:
            if (a in first and b in first ) or (a in second and b in second ):
                return False
            
        return True