class Solution:
    def replaceDigits(self, s: str) -> str:
        res=""
        i = 0
        n = len(s)
        char = s[0]
        while i<n:
            if s[i].isnumeric():
                num=int(s[i])%26
                # print(char,ord(char),num,ord(char)+num, chr())
                res+=(chr(ord(char)+num))
                
            else:
                char = s[i]
                res+=s[i]
            i+=1
        return res