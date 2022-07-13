from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d = Counter(s1)
        window = len(s1)-1
        i = 0
        subD = None
        while i+window<len(s2):
            j = i+window
            # print("i",i,"j",j)
            if subD is None:
                subD = Counter(s2[i:j+1])
            else:
                subD[s2[j]] = subD.setdefault(s2[j], 0) + 1
            # print("\tsubD",subD)
            if d==subD:
                return True
            subD[s2[i]]-=1
            if subD[s2[i]]<=0:
                subD.pop(s2[i])
            i+=1
        return False