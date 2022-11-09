from heapq import heappush,heappop
import math
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.maxHeapSize = 0
        self.minHeapSize = 0
        self.count = 0
        self.temp1 = None
        self.temp2 = None
        
    def addToMaxHeap(self,num):
        heappush(self.maxHeap, (-num,num))
        self.maxHeapSize+=1
        
    def addToMinHeap(self,num):
        heappush(self.minHeap, (num,num))
        self.minHeapSize+=1
        
    def peekMaxHeap(self):
        if self.maxHeapSize>0:
            return self.maxHeap[0][1]
        
    def popMaxHeap(self):
        if self.maxHeapSize>0:
            self.maxHeapSize-=1
            return heappop(self.maxHeap)[1]
        
    def popMinHeap(self):
        if self.minHeapSize>0:
            self.minHeapSize-=1
            return heappop(self.minHeap)[1]
        
    def peekMinHeap(self):
        if self.minHeapSize>0:
            return self.minHeap[0][1]
        
    def addNum(self, num):
        if self.count==0:
            self.temp1 = num
            self.count+=1
            return
        elif self.count==1:
            self.temp2 = num
            smaller,bigger = min(self.temp1,self.temp2),max(self.temp1,self.temp2)
            self.addToMaxHeap(smaller)
            self.addToMinHeap(bigger)
            self.count+=1
            return
        
        # print(num,self.peekMaxHeap())
        if num > self.peekMaxHeap():
            self.addToMinHeap(num)
        else:
            self.addToMaxHeap(num)
        if(abs(self.maxHeapSize-self.minHeapSize)>1):
            # print("need to reorder")
            if self.maxHeapSize>self.minHeapSize:
                elem = self.popMaxHeap()
                self.addToMinHeap(elem)
            else:
                elem = self.popMinHeap()
                self.addToMaxHeap(elem)
        # print(self.maxHeap,self.minHeap)
        return
        

    def findMedian(self):
        if self.count==0:
            return -1
        if self.count==1:
            return self.temp1
        if (self.maxHeapSize+self.minHeapSize)%2==0:
            num1= self.peekMaxHeap()
            num2= self.peekMinHeap()
            return (num1+num2)/2
        if self.maxHeapSize>self.minHeapSize:
            return self.peekMaxHeap()
        else:
            return self.peekMinHeap()
        return -1

# obj = MedianFinder()
# for num in [5,4,2,1,2,3]:
#     obj.addNum(num)
    
#     print(obj.findMedian())