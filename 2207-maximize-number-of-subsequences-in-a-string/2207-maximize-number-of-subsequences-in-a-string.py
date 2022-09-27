class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cnt1 =0
        cnt2 = 0
        n = len(text)
        i = 0
        res = 0
        while i<n:
            if text[i]==pattern[1]:
                res+=cnt1
                cnt2+=1
            
            if text[i]==pattern[0]:
                cnt1+=1
                
            i+=1
        print(cnt1,cnt2,res)
        return res+max(cnt2, cnt1)