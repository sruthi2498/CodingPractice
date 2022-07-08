class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x :x[1], reverse=True)
        print(boxTypes)
        count = 0 
        i = 0
        s = 0
        while i<len(boxTypes) and count<truckSize:
            # print("count",count,"s",s, "box",boxTypes[i])
            if count+boxTypes[i][0]<=truckSize:
                # print(i,"can fit full")
                count+=boxTypes[i][0]
                s+=(boxTypes[i][0]*boxTypes[i][1])
            else:
                remaining = truckSize - count
                # print(i,"can take only ",remaining)
                count+=remaining
                s+=(remaining*boxTypes[i][1])
            i+=1
        return s