def recItemizeList(title, fullList, level):
    for i in fullList:
        if(isinstance(i, list)):
            recItemizeList(title, i, level + 1)
        else:
            print(title, level, i)

def itemizeList(title, fullList):
    recItemizeList(title, fullList, 0)
    

l = ['a string', ['a','b',['1','2','3']], 'spam', ['eggs']]

itemizeList("Example", l)