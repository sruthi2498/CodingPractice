from collections import Counter
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        n = len(t)
        m = len(s)
        l = 0
        r = l+n-1
        minlen = math.inf 
        minStr = ""
        s_count = None
        while l<m and r<m:
            # print("l",l,"r",r)
            if s_count is None:
                s_count = Counter(s[l:r+1])
            inter = t_count & s_count
            # print("\t",s_count,inter)
            while l+n-1<=r and inter>=t_count:
                # print("\t found subset l",l,"r",r)
                if (r-l+1)<minlen:
                    minlen = r-l+1
                    minStr = s[l:r+1]
                s_count[s[l]]-=1
                if s_count[s[l]]<=0:
                    s_count.pop(s[l])
                inter = t_count & s_count
                l+=1
                
            else:
                r+=1
                if r<m:
                    s_count[s[r]] = s_count.setdefault(s[r],0)+1
        return minStr
                