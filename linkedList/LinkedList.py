import random

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def popFirst(self):
        temp = self.head 
        self.head = self.head.next 
        return temp

    def insertAtEnd(self,val):
        if self.head is None:
            self.head = Node(val)
            self.end = self.head
            return
        else:
            self.end.next = Node(val)
            self.end = self.end.next
            
            
    def insertAtStart(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        else:
            temp = Node(val)
            temp.next = self.head 
            self.head = temp

    def display(self):
        temp = self.head 
        l = []
        while(temp!=None):
            l.append(str(temp.val))
            temp  = temp.next 
        print(",".join(l))

    def deleteFirstOccurence(self,val):
        if(self.head == None):
            print("List empty cannot delete")
            return
        if(self.head.val == val):
            self.head = self.head.next 
            return
        prev = self.head
        temp = prev.next 
        while(temp.next!=None):
            if(temp.val == val):
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        if(temp.val == val):
            prev.next = None
            return 
        print("Could not find element to delete")

    def deleteAtIndex(self,index):
        if(self.head == None):
            print("List empty cannot delete")
            return
        if(index == 0):
            self.head = self.head.next 
            return
        i = 1
        prev = self.head
        temp = prev.next 
        while(temp.next!=None):
            if(i == index):
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
            i = i+1

        if(i == index):
            prev.next = None
            return 
        print("Index out of range")

    def countIterative(self):
        count = 0
        temp = self.head
        while(temp!=None):
            count = count+1
            temp = temp.next
        return count

    def countRecursive(self):
        return self.__countRecursive(self.head)

    def __countRecursive(self, temp):
        if(temp == None):
            return 0
        return 1 + self.__countRecursive(temp.next)

    def searchIterative(self, val):
        if(self.head == None):
            return False
        temp = self.head
        while(temp!=None):
            if(temp.val == val):
                return True
            temp = temp.next 
        return False

    def searchRecursive(self,val):
        return self.__searchRecursive(self.head,val)

    def __searchRecursive(self, temp,val):
        if(temp == None):
            return False
        if(temp.val == val):
            return True
        return self.__searchRecursive(temp.next,val)


    def createCycle(self):
        count = self.countIterative()
        index = random.randint(0,count-2)
        print("cycleEndIndex = ",index)
        temp = self.head
        cycleEnd = None 
        i = 0
        while(temp.next!=None):
            if(i == index):
                cycleEnd = temp
            temp = temp.next 
            i = i+1
        temp.next = cycleEnd
        print("Created cycle from "+str(temp.val)+" to "+str(cycleEnd.val))

    def detectCycleFloyd(self):
        if(self.head == None):
            return False
        if(self.head.next == None):
            return False
        slowP = self.head 
        fastP = self.head.next 
        while(slowP and fastP and fastP.next):
            if(slowP == fastP):
                return True
            slowP = slowP.next
            fastP = fastP.next.next
        return False

    def countLoopLength(self):
        if(self.head == None):
            return 0
        if(self.head.next == None):
            return 0 
        slowP = self.head 
        fastP = self.head.next 
        while(slowP and fastP and fastP.next):
            if(slowP == fastP):
                count = 1
                temp = slowP.next
                while(temp!=slowP):
                    temp = temp.next
                    count=count+1
                return count
            slowP = slowP.next
            fastP = fastP.next.next
        return 0


    def swapNodes(self,val1, val2):
        if(not self.head or not self.head.next):
            return
        prevA = None
        A = self.head 
        while(A.next and A.val!=val1):
            prevA = A
            A= A.next 
        if(not A):
            return
        prevB = None
        B = self.head 
        while(B.next and B.val!=val2):
            prevB = B
            B = B.next
        if(not B):
            return

        if(A==B):
            return

        tempBNext = B.next 
        
        if(not prevA): # A is the head
            print(prevB.val, A.val, B.val)
            prevB.next = A 
        elif(not prevB) : # B is the head
            print(prevA.val, A.val, B.val)
            prevA.next = B
        else:
            prevA.next = B
            prevB.next = A 
        
        AisHead = True if A == self.head  else False
        BisHead = True if B == self.head  else False

        B.next = A.next 
        A.next = tempBNext

        if(AisHead):
            self.head = B
        elif(BisHead):
            self.head = A

    def insertNodeAtEnd(self,node):
        if self.head is None:
            self.head =node
            self.end = self.head
            return
        else:
            self.end.next = node
            self.end = self.end.next  

    

def main():
    LL = LinkedList()
    LL.insertAtEnd(1)
    LL.insertAtEnd(2)
    LL.insertAtEnd(3)
    LL.insertAtEnd(4)
    LL.insertAtEnd(5)

    LL.display()

    # print(LL.countIterative())
    # print(LL.countRecursive())

    # print(LL.searchIterative(3))
    # print(LL.searchIterative(7))
    # print(LL.searchRecursive(3))
    # print(LL.searchRecursive(7))
    
    # print(LL.detectCycleFloyd())
    # LL.createCycle()
    # print(LL.detectCycleFloyd())
    # print(LL.countLoopLength())

    #LL.swapNodes(2,5)

    #LL.reverseIterative()
    LL.display()

if __name__ == "__main__":
    main()