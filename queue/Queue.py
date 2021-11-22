import sys 
sys.path.append("/Users/sruthiv/Desktop/CodingPractice")

from linkedList.LinkedList import LinkedList, Node

class Queue:
    def __init__(self) :
        self.linkedList = LinkedList()

    def queue(self,node):
        self.linkedList.insertNodeAtEnd(node)

    def dequeue(self):
        node = self.linkedList.popFirst()
        return node

    def display(self):
        self.linkedList.display()

def main():
    q = Queue()
    q.queue(Node(1))
    q.queue(Node(2))
    q.queue(Node(3))
    q.display()

    print(q.dequeue().val)
    q.display()

if __name__ == "__main__":
    main()