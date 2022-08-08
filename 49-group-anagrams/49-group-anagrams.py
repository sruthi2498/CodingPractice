class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedstrs= ["".join(sorted(list(x))) for x in strs]
        anagrams = {}
        n = len(strs)
        for i in range(n):
            if sortedstrs[i] not in anagrams:
                anagrams[sortedstrs[i]] = []
            
            anagrams[sortedstrs[i]].append(strs[i])
        return [v for k,v in anagrams.items()]