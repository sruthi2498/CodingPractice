class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        i = 1
        while i<len(strs):
            word = strs[i]
            j = 0
            while j<min(len(prefix),len(word)) and word[j]==prefix[j]:
                j+=1
            prefix = prefix[:j]
            if len(prefix)<=0:
                return ""
            i+=1
        return prefix