
class MinHeap:
    def __init__(self, arr):
        self.H = arr
        self.buildHeap(arr,len(arr))

    def heapify(self,arr, n, i):
        smallest = i; 
        l = 2 * i + 1; 
        r = 2 * i + 2; 
    
        if l < n and arr[l] < arr[smallest]:
            smallest = l;
    
        if r < n and arr[r] < arr[smallest]:
            smallest = r;
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i];
            self.heapify(arr, n, smallest);

    def heapifyUpwards(self,arr, n, i):
        #print(i)
        smallest = i; 
        parent = (i-1)//2
        if parent >= 0 and arr[smallest] < arr[parent]:
            smallest = parent;
        
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i];
            return self.heapifyUpwards(arr, n, parent);
        return smallest
    
    
    def buildHeap(self,arr, n):
        start = n // 2 - 1;
        for i in range(start, -1, -1):
            self.heapify(arr, n, i);

        self.H = arr

    def display(self):
        print(self.H)

    def extractMin(self):
        minVal = self.H[0]
        lastVal = self.H[len(self.H)-1]
        self.H[0]=lastVal
        self.H.pop()
        self.heapify(self.H, len(self.H), 0)
        return minVal

    def extractAtIndex(self,index):
        if len(self.H) == 0 or index>(len(self.H)-1):
            return
        val = self.H[index]
        lastVal = self.H[len(self.H)-1]
        self.H[index]=lastVal
        self.H.pop()
        self.heapify(self.H, len(self.H), index)
        self.heapifyUpwards(self.H, len(self.H), index)
        return val

    def insert(self,val):
        self.H.append(val)
        i = self.heapifyUpwards(self.H, len(self.H), len(self.H) -1 )
        print(i)

arr = [4,5,2,1,6,7,9]
print(arr)
minH = MinHeap(arr)
minH.display()
minH.insert(3)
minH.display()
print(minH.extractAtIndex(4))
minH.display()
# print(minH.extractMin())
# minH.display()