
import sys 
sys.path.append("/Users/sruthiv/Desktop/CodingPractice")

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
    def display(self):
        print(self.val)
    
class QueueNode:
    def __init__(self,data):
        self.data = data
        self.next = None 

class MyQueue:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def dequeue(self):
        if not self.head:
            return
        temp = self.head 
        self.head = self.head.next 
        self.size = self.size -1
        return temp

    def queue(self,data):
        self.size = self.size+1
        if self.head is None:
            self.head = QueueNode(data)
            self.end = self.head
            return
        else:
            self.end.next = QueueNode(data)
            self.end = self.end.next
            
    def display(self):
        temp = self.head 
        while temp:
            if(temp.data):
                temp.data.display()
            temp=temp.next

    def getSize(self):
        return self.size

class Tree:
    def __init__(self):
        self.root = None
    
    def insertLevelOrder(self,val):
        if not self.root:
            self.root = TreeNode(val)
            return
        q = MyQueue()
        q.queue(self.root)
        while q.getSize()>0:
            queueNode = q.dequeue()
            treeNode = queueNode.data
            if not treeNode.left:
                treeNode.left = TreeNode(val)
                return
            elif not treeNode.right:
                treeNode.right = TreeNode(val)
                return
            else:
                q.queue(treeNode.left)
                q.queue(treeNode.right)

   

    def preorderDisplay(self):
        self.__preorder(self.root)

    def __preorder(self, temp):
        if not temp:
            return 
        print(temp.val)
        self.__preorder(temp.left)
        self.__preorder(temp.right)

def main():
    t = Tree()
    t.insertLevelOrder(1)
    t.insertLevelOrder(2)
    t.insertLevelOrder(3)
    t.insertLevelOrder(4)
    t.insertLevelOrder(5)
    t.preorderDisplay()

if __name__ == "__main__":
    main()
        
