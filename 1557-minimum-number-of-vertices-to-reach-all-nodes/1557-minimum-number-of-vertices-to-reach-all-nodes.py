class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_graph = {i : [] for i in range(n)}
        for fro,to in edges:
            incoming_graph[to].append(fro)
            
        return [k for k,v in incoming_graph.items() if len(v)==0]