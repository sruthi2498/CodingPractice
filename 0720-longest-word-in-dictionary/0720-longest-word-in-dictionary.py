import string
class Node:
    def __init__(self,char):
        self.char = char
        self.children = {}
        self.isWordEnd = False
    def addChild(self,child_char ):
        if child_char not in self.children:
            self.children[child_char] = Node(child_char)
            # print("add child",child_char, self.children) 
    def getChild(self,child_char):
        if child_char in self.children:
            return self.children[child_char] 
    def display(self):
        print(self.char, self.children.keys(),self.isWordEnd)
    def getChildren(self):
        return self.children
    def setWordEnd(self):
        self.isWordEnd = True
        
class Trie:

    def __init__(self):
        self.root = Node("")

    def display(self):
        print("##### TRIE ")
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            temp.display()
            for key,node in temp.getChildren().items():
                queue.append(node)
        print("#####  ")  
            
        
    def insert(self, word: str) -> None:
        exists,node,index = self.__search(word)
        # print("__search : ",exists)
        if not exists:
            # print("insert from ",index)
            i = index
            n = len(word)
            while i<n:
                node.addChild(word[i])
                node = node.getChild(word[i])
                i+=1
            node.setWordEnd()
            # print("inserted",word)
        else:
            node.setWordEnd()
            

    def search(self, word: str) -> bool:
        exists,node,index = self.__search(word)
        if exists and node.isWordEnd:
            return True
        return False
        
       
    def __search(self,word):
        temp = self.root
        i = 0
        n = len(word)
        while i<n:
            childNode = temp.getChild(word[i])
            if childNode:
                temp = childNode
            else:
                return False,temp,i
            i+=1
        if i==n:
            return True,temp,0
        
        return False,temp,0

    def startsWith(self, prefix: str) -> bool:
        exists,node,index = self.__search(prefix)
        return exists


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        maxLen = 0
        maxWord = ""
        words.sort()
        for word in words:
            n = len(word)
            i = n-1
            while i>0 and trie.search(word[:i]):
                i-=1
            if i<=0 and n>maxLen:
                maxLen = n
                maxWord = word
        return maxWord
                
            