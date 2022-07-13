class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}
        trust_counts = [0]*(n+1)
        for a,b in trust:
            graph[a].append(b)
            trust_counts[b]+=1
        for k,v in graph.items():
            if len(v)==0 and trust_counts[k]==n-1:
                return k
        return -1