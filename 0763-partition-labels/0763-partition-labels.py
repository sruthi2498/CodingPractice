class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        n = len(s)
        char_map = {}
        for i in range(n):
            if s[i] not in char_map:
                char_map[s[i]]=[i,i]
            else:
                char_map[s[i]][1]=i
        # print(char_map)
        
        
        i=0
        result = []
        while i<n:
            start = char_map[s[i]][0]
            end = char_map[s[i]][1]
            j = start+1
            while j<end:
                if char_map[s[j]][1] >end :
                    end = char_map[s[j]][1]
                j+=1
            # print(s[start:end+1],len(s[start:end+1]))
            result.append(end-start+1)
            i = end+1
        return result
        