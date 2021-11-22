class Node:
    def __init__(self,state, parent, cost, other=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.other = other
        self.next = None 

    def display(self):
        print("\t",self.state, self.parent, self.cost,self.other)

class MinHeap:
    def __init__(self):
        self.H = []
        self.elementDict={}

    def heapifyUpwards(self,n, i):
        smallest = i; 
        parent = (i-1)//2
        if parent >= 0 and self.H[smallest].cost < self.H[parent].cost:
            smallest = parent
        if smallest != i:
            self.H[i], self.H[smallest] = self.H[smallest], self.H[i]
            return self.heapifyUpwards( n, parent)
        return smallest

    def heapifyDownwards(self, n, i):
        smallest = i; 
        l = 2 * i + 1; 
        r = 2 * i + 2; 
    
        if l < n and self.H[l].cost < self.H[smallest].cost:
            smallest = l;
    
        if r < n and self.H[r].cost < self.H[smallest].cost:
            smallest = r;
        if smallest != i:
            self.H[i], self.H[smallest] = self.H[smallest], self.H[i];
            self.heapifyDownwards(n, smallest);

    def display(self):
        print(self.H)

    def extractMin(self):
        if len(self.H == 0):
            return
        minVal = self.H[0]
        lastVal = self.H[len(self.H)-1]
        self.H[0]=lastVal
        self.H.pop()
        self.heapifyDownwards(self.H, len(self.H), 0)
        self.elementDict[minVal.state]=None
        return minVal

    def extractAtIndex(self,index):
        if len(self.H)==0 or index>(len(self.H)-1):
            return
        val = self.H[index]
        lastVal = self.H[len(self.H)-1]
        self.H[index]=lastVal
        self.H.pop()
        self.heapifyDownwards(self.H, len(self.H), index)
        self.heapifyUpwards(self.H, len(self.H), index)
        self.elementDict[val.state]=None
        return val

    def insert(self,state,parent,cost,other = None):
        node = Node(state,parent,cost,other)
        self.H.append(node)
        self.elementDict[state]=self.heapifyUpwards(self.H, len(self.H), len(self.H) -1 )

    
    def doesElementExist(self,state):
        return state in self.elementDict and  self.elementDict[state]

    def getSize(self):
        return len(self.H)


    def getNodeForState(self,state):
        if len(self.H == 0):
            return
        index = self.elementDict[state]
        if index :
            return self.H[index]

    def removeNodeForElement(self,state):
        index = self.elementDict[state]
        if index:
            self.extractAtIndex(index)
        
class Queue:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0
        self.elementPointerDict = {}


    def insertWithPriority(self,state,parent,cost,other = None):
        #print("Inserting ",state,parent,cost)
        self.size = self.size+1
        
        if not self.head :
            self.head = Node(state,parent,cost,other)
            self.elementPointerDict[state]=self.head
            return

        newNode = Node(state,parent,cost,other)

        if(self.head.cost > cost):
            newNode.next = self.head
            self.head = newNode 
            self.elementPointerDict[state]= self.head
            return

        temp = self.head
        prev = None
        while temp and temp.cost<=cost :
            prev = temp
            temp = temp.next 

        if not prev :
            newNode.next = temp
            self.elementPointerDict[state]= newNode

        else:
            prev.next = newNode
            self.elementPointerDict[state]= prev.next
            
        if temp: #last node
            newNode.next = temp 


    
    def popFirstNode(self):
        if not self.head:
            return None 

        temp = self.head 
        self.head = self.head.next 
        self.size = self.size-1
        self.elementPointerDict[temp.state]=None
        return temp
    
    def doesElementExist(self,element):
       # print(self.elementPresentDict)
        return element in self.elementPointerDict and  self.elementPointerDict[element]

    def getSize(self):
        return self.size

    def getNodeForElement(self,element):
        if not self.head:
            return
        return self.elementPointerDict[element]

    def removeNodeForElement(self,element):
        if(self.head == None):
            return
        if(self.head.state == element):
            self.head = self.head.next 
            self.size = self.size-1
            self.elementPointerDict[element]=None
            return
        prev = self.head
        temp = prev.next 
        while(temp.next!=None):
            if(temp.state == element):
                prev.next = temp.next
                self.size = self.size-1
                self.elementPointerDict[element]=None
                return
            prev = temp
            temp = temp.next

        if(temp.state == element):
            prev.next = None
            self.size = self.size-1
            self.elementPointerDict[element]=None

    def display(self):
        print("Queue Display : ")
        temp = self.head
        while temp:
            temp.display()
            temp= temp.next
             