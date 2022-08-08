class Solution:
    def countVowelPermutation(self, n: int) -> int:
        opt = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(n):
            opt.append([0]*(5))
            
        
        #dp[i][j] be the number of strings of length i that ends with the j-th vowel
        for j in range(5):
            opt[0][j] = 1
            
           
        for i in range(1,n):
            for vowelIndex in range(5):
                vowel = vowels[vowelIndex]
                if vowel =="a":
                    opt[i][vowelIndex] = opt[i-1][vowels.index("e")]+opt[i-1][vowels.index("u")]+opt[i-1][vowels.index("i")]
                elif vowel =="e":
                    opt[i][vowelIndex] = opt[i-1][vowels.index("a")]+opt[i-1][vowels.index("i")]
                elif vowel =="i":
                    opt[i][vowelIndex] = opt[i-1][vowels.index("o")]+opt[i-1][vowels.index("e")]
                elif vowel =="o":
                    opt[i][vowelIndex] = opt[i-1][vowels.index("i")]
                elif vowel =="u":
                    opt[i][vowelIndex] = opt[i-1][vowels.index("o")]+opt[i-1][vowels.index("i")]
                    
                
#         for row in opt:
#             print(row)
           
#         print("######")

        return sum(opt[-1])%1000000007