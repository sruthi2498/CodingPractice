import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList+[beginWord])
        if endWord not in wordList:
            return 0
        graph = {w:set() for w in wordList}
        
        letters = list(string.ascii_lowercase)
        for word in wordList:
            chars = list(word)
            for i,char in enumerate(chars):
                for letter in letters:
                    if letter!=char:
                        new_w = "".join(word[:i]+letter+word[i+1:])
                        if new_w in wordList and new_w not in graph[word]:
                            graph[word].add(new_w)
                            graph[new_w].add(word)
        start = beginWord
        queue = [[start,1]]
        target = endWord
        visited = set()
        minDist = math.inf
        while queue:
            # print(queue)
            node,dist = queue.pop(0)
            if node==target:
                minDist = min(minDist,dist)
            # print("\t",node,dist)
            visited.add(node)
            for neighb in graph[node]:
                if neighb not in visited:
                    queue.append( [neighb,dist+1] )
        return minDist if minDist<math.inf else 0