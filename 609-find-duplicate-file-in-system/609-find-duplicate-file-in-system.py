class Solution:
    def __init__(self):
        self.data = {}
    
    def parsePaths(self,paths):
        for path in paths:
            words = path.split(" ")
            direct = words[0]
            fulpaths = []
            for word in words[1:]:
                word= word.split("(")
                filename = word[0]
                content = word[1][:-1]
                if content not in self.data:
                    self.data[content] = []
                # print(filename,content)
                self.data[content].append(direct+"/"+filename)
                
        
    
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        self.parsePaths(paths)
        # print(self.data)
        result = [ v for k,v in self.data.items() if len(v)>1]
        return result
            