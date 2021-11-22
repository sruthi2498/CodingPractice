import re

def longestCommonSubsequence(text1: str, text2: str) -> int:
    n = len(text1)
    m = len(text2)
    if n==0 or m==0:
        return 0
    opt=[ [0  for _ in range(m+1)] for _ in range(n+1) ]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1]==text2[j-1] : 
                opt[i][j] = max(1+ opt[i-1][j-1], opt[i-1][j],opt[i][j-1])
            else:
                opt[i][j] = max(opt[i-1][j-1], opt[i-1][j],opt[i][j-1])

    i = n
    j = m
    res = ""
    while i>0 and j>0:
        if text1[i-1]==text2[j-1]:
            res=text1[i-1]+res
            i-=1
            j-=1
        elif opt[i-1][j]>opt[i][j-1]:
            i-=1
        else:
            j-=1
    return res

def solution(s):
    # Your code here
    r = s[1:]
    
        

# solution("abcabc")

print(longestCommonSubsequence("bmnop","mnopqqqq"))