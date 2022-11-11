class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        incoming_edges = {i:[] for i in range(numCourses)} 
        
        for a,b in prerequisites:
            graph[a].append(b)
            incoming_edges[b].append(a)
        
        
        visited = set()
        queue = []
        for node,edges in incoming_edges.items():
            if not edges:
                queue.append(node)
        if not queue:
            return False
        
        while queue:
            print(queue)
            node = queue.pop(0)
            print("Starting with ",node)
            visited.add(node)
            for neighb in graph[node]:
                print("\tRemoving it from ",neighb)
                incoming_edges[neighb].remove(node)
                if not incoming_edges[neighb] and neighb not in visited:
                    queue.append(neighb)
        print(incoming_edges)  
        print("visited",visited)
        return len(visited)==numCourses