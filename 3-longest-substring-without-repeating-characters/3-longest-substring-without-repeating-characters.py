class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        current_dict = dict()
        i = 0
        j = 1
        maxLen = 1
        current_dict[s[i]]=i
        while i<n and j<n:
            # print(i,j)
            if s[j] in current_dict and current_dict[s[j]]>=i:
                i = current_dict[s[j]]+1
            current_dict[s[j]] = j
            j+=1
            if j-i>maxLen:
                maxLen = j-i
        return maxLen