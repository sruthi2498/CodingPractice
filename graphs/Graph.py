

class Graph:
    def __init__(self,adjacencyList):
        self.adjacencyList = adjacencyList
        self.adjacencyDict = {}
        for v,adj in self.adjacencyList:
            self.adjacencyDict[v]=adj

    def display(self):
        for v,adj in self.adjacencyList:
            print(v,"->",adj)

    def BFS(self):
        queue = []
        startVertex = self.adjacencyList[0][0]
        queue.append(startVertex)
        visited = set()
        while len(queue) > 0 :
            #print(queue)
            vertex = queue.pop()
            print(vertex)
            visited.add(vertex)
            for adjacentVertex in self.adjacencyDict[vertex]:
                if adjacentVertex not in visited and adjacentVertex not in queue:
                    queue.append(adjacentVertex)

            

adj = [[0,[1,2,3]],[1,[0,2]],[2,[0,1,3]],[3,[0,2]]]
g = Graph(adj)
g.display()
g.BFS()