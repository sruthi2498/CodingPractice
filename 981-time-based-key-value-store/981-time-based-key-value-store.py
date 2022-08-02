class TimeMap:

    def __init__(self):
        self.dict = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [ [value,timestamp] ]
        else:
            self.dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        index = self.search(key,timestamp)
        # print(timestamp,index, self.dict[key])
        
        if index>=len(self.dict[key]):
            return self.dict[key][-1][0]
        if self.dict[key][index][1]==timestamp:
            return self.dict[key][index][0]
        if index == 0:
            return ""
        return self.dict[key][index-1][0]
        
    
    def search(self, key, target: int) -> int:
        l = 0
        r = len(self.dict[key])-1
        while l<=r:
            mid = (l+r)//2
            if self.dict[key][mid][1]==target:
                return mid
            if self.dict[key][mid][1]<target:
                l=mid+1
            else:
                r=mid-1
        return max(l,r)
        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)