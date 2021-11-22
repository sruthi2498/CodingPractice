

def prefixMatchBF(a,b):
    prefixStrings=[a[0]]

    for i in range(1,len(a)):
        s=prefixStrings[i-1]+a[i]
        prefixStrings.append(s)
    print(prefixStrings)

    for word in b:
        if word not in prefixStrings:
            return False

    return True



def prefixMatch(a,b):

    res=True

    for i,word in enumerate(b):
        aIndex = 0
        bWordIndex = 0
        aWordIndex = 0


        while bWordIndex<len(word) and aIndex<len(a):

            while aWordIndex<len(a[aIndex]) and bWordIndex<len(word) and a[aIndex][aWordIndex]==word[bWordIndex]:
                aWordIndex+=1
                bWordIndex+=1

            if aWordIndex<len(a[aIndex]) and bWordIndex<len(word) and a[aIndex][aWordIndex]!=word[bWordIndex]:
                return False

            aIndex+=1

            
        if bWordIndex!=len(word):
            return False


a= ["one","two","three"]
b=["onetwo","one"]
print(prefixMatchBF(a,b))