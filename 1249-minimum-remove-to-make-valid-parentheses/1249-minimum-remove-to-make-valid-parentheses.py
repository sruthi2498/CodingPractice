class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        i=0
        indices=set()
        n=len(s)
        while i<n:
            if s[i]=="(":
                stack.append([s[i],i])
            elif s[i]==")":
                if len(stack)==0:
                    indices.add(i)
                else:
                    char,ind=stack.pop()
                    # print(char)
                    if char!="(":
                        indices.add(i) 
            i+=1
        while len(stack)>0:
            _,ind=stack.pop()
            indices.add(ind)
        i=0
        res=""
        while i<n:
            if i not in indices:
                res=res+s[i]
            i+=1
        return res