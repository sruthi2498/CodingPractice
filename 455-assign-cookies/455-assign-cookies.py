class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        i = 0
        j = 0
        content = 0
        while i<n and j<m :
            #print(i,j)
            if g[i]<=s[j]:
                content+=1
                i+=1
            j+=1
        print(i,j,content)
        return content
                