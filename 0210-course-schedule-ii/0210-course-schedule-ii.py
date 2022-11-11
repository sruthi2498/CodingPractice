class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        incoming_edges = {i:[] for i in range(numCourses)} 
        
        for a,b in prerequisites:
            graph[b].append(a)
            incoming_edges[a].append(b)
        
        
        visited = set()
        order = []
        queue = []
        for node,edges in incoming_edges.items():
            if not edges:
                queue.append(node)
        if not queue:
            return []
        
        while queue:
            node = queue.pop(0)
            visited.add(node)
            order.append(node)
            for neighb in graph[node]:
                incoming_edges[neighb].remove(node)
                if not incoming_edges[neighb] and neighb not in visited:
                    queue.append(neighb)
        if len(visited)==numCourses:
            return order
        return []