class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0
        while i<n :
            # print(stack)
            if s[i]!="]":
                stack.append(s[i])
            else:
                char = stack.pop()
                pattern = ""
                while char!="[":
                    pattern = char + pattern 
                    if stack:
                        char = stack.pop()
                        
                num_char = stack.pop()
                k = ""
                # print(num_char,num_char.isnumeric())
                while num_char.isnumeric():
                    k = num_char + k 
                    if stack:
                        num_char = stack[-1]
                        if num_char.isnumeric():
                            stack.pop()
                        # print(num_char,num_char.isnumeric())
                    else:
                        num_char = "x"
                # print(k)
                res = ""
                k = int(k)
                while k>0:
                    k-=1
                    res+=pattern
                stack.append(res)
            i+=1
        print(stack)
        return "".join(stack)
                
                