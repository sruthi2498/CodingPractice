class Solution:
    def getKey(self,i,j):
        return str(i)+"_"+str(j)
    
    def getNum(self,key):
        return key.split("_")
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        graph = {"p":[],"a":[]}
        
        n = len(heights)
        m = len(heights[0])
        
        for i in range(n):
            for j in range(m):
                graph[self.getKey(i,j)] = []
                
        for i in range(n):
            graph["p"].append(self.getKey(i,0))
            graph["a"].append(self.getKey(i,m-1))
        
        for j in range(m):
            graph["p"].append(self.getKey(0,j))
            graph["a"].append(self.getKey(n-1,j))
            
        for i in range(n):
            for j in range(m):
                if i>0 and heights[i-1][j]>=heights[i][j]:
                    graph[self.getKey(i,j)].append(self.getKey(i-1,j))
                
                if j>0 and heights[i][j-1]>=heights[i][j]:
                    graph[self.getKey(i,j)].append(self.getKey(i,j-1))
                
                if i<n-1 and heights[i+1][j]>=heights[i][j]:
                    graph[self.getKey(i,j)].append(self.getKey(i+1,j))
                
                if j<m-1 and heights[i][j+1]>=heights[i][j]:
                    graph[self.getKey(i,j)].append(self.getKey(i,j+1))

    
        p = set()
        queue = ["p"]
        while len(queue)>0:
            node = queue.pop(0)
            p.add(node)
            for neighb in graph[node]:
                if neighb not in p:
                    queue.append(neighb)

        q = set()
        
        queue = ["a"]
        while len(queue)>0:
            node = queue.pop(0)
            q.add(node)
            for neighb in graph[node]:
                if neighb not in q:
                    queue.append(neighb)
                    
        
        # print(q)
        res = q.intersection(p)
        return [self.getNum(k) for k in res]