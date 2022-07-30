class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pattern = list(pattern)
        if len(s)!=len(pattern):
            return False
        
        pMap = {}
        start = 0
        for c in pattern:
            if c not in pMap:
                pMap[c] = str(start)
                start+=1
        for i,c in enumerate(pattern):
            pattern[i] = pMap[c]
        # print(pMap, "".join(pattern))
        
        start = 0
        pMap.clear()
        for word in s:
            if word not in pMap:
                pMap[word] = str(start)
                start+=1
        for i,word in enumerate(s):
            s[i] = pMap[word]
        # print(pMap, "".join(s))
        return "".join(pattern)=="".join(s)
        
        