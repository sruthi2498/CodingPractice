class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        n = len(buses)
        m = len(passengers)
        # print(buses)
        # print(passengers)
        
        i = 0
        j = 0
        while i<n:
            currentCap = 0
            while j<m and passengers[j]<=buses[i] and currentCap<capacity:
                currentCap+=1
                j+=1
            # print("bus ",i,buses[i])
            # print("\tcurrentCap ",currentCap)
            # print("\ttill passenger ",j-1)
            
            i+=1
        if i<n:
            return buses[-1]
        
        k = j-1
        if currentCap < capacity:
            time = buses[i-1]
        else:
            time = passengers[k]
        
        # print("starting at k=",k,"time = ",time)
        while k>=0 and passengers[k]==time:
            k-=1
            time-=1
        return time
        