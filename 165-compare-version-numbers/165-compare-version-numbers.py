class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 =[ v.lstrip("0") for v in  version1.split(".")]
        version1 = [int(v) if v else 0 for v in version1]
        version2 =[ v.lstrip("0") for v in  version2.split(".")]
        version2 = [int(v) if v else 0 for v in version2]
        print(version1, version2)
        n = len(version1)
        m = len(version2)
        for i in range(min(n,m)):
            if version1[i]<version2[i]:
                return -1
            elif version1[i]>version2[i]:
                return 1
        
        if i==n-1 and i==m-1:
            return 0
        i+=1
        if i<n:
            while i<n and version1[i]==0:
                i+=1
            if i==n:
                return 0
            return 1
        else:
            while i<m and version2[i]==0:
                i+=1
            if i==m:
                return 0
            return -1