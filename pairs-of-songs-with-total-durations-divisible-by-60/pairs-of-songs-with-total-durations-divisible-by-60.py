class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_counts=dict()
        x = 0
        for i,t in enumerate(time):
            x = t%60
            if x in mod_counts:
                mod_counts[x].append(i)
            else:
                mod_counts[x]=[i]
                
        print(mod_counts)
        res = 0
        n = 0
        for m,indices in mod_counts.items():
            
            n = len(indices)
            print(m,n,res)
            if m==30 or m==0:
                if n>1:
                    res+= (n*(n-1))/2
                
            elif 60-m in mod_counts:
                res+= n*len(mod_counts[60-m])
                mod_counts[60-m]=[]
        return int(res)
                
            