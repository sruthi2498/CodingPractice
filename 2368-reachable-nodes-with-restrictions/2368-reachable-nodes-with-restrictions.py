class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = {}
        for a,b in edges:
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        queue = [0]
        restricted = set(restricted)
        while queue:
            node = queue.pop(0)
            if node not in restricted:
                visited.add(node)
                for x in graph[node]:
                    if x not in visited and x not in restricted:
                        queue.append(x)
        return len(visited)