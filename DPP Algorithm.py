##Copyrights belongs to Sirius Hou
## DPP Algorithm


## Sequence of Resolution [## MANUAL INPUT REQUIRED ##]
seq = ["R", "P", "Q", "W"]
num = len(seq)

## Set of clauses [## MANUAL INPUT REQUIRED ##]
## FORMAT: ("SYMBOL", NEGATION?("N":YES; 0:NO))
##  Sample: ("P", "N") -> ¬P
S = [[("P", "N"), ("Q", "N"), ("R", "N"), ("W", "N")],
     [("P", "N"), ("Q", "N"), ("R", 0), ("W", 0)],
     [("P", "N"), ("Q", "N"), ("R", "N"), ("W", 0)],
     [("P", 0), ("Q", "N"), ("R", "N"), ("W", "N")],
     [("P", 0), ("Q", 0), ("R", "N")],
     [("P", 0), ("Q", 0), ("W", "N")],
     [("P", "N"), ("R", 0), ("W", 0)],
     [("Q", "N"), ("R", 0), ("W", 0)],
     [("P", "N"), ("Q", 0)],
     [("P", 0), ("Q", "N")],
     [("R", 0)]]


###### HELPER FUNCTIONS ######

def sortSet(s):
    result=[]
    for clauses in s:
        tempSorted = []
        for clause in clauses:
            index = 0
            while index < len(tempSorted):
                if tempSorted[index][0] > clause[0]:
                    break
                elif tempSorted[index][0] == clause[0]:
                    if tempSorted[index][1] == 0:
                        index+=1
                    break
                index += 1
            tempSorted.insert(index, clause)
        result.append(tempSorted)
    return result


def sortClause(clause):
    tempSorted = []
    for c in clause:
        index = 0
        while index < len(tempSorted):
            if tempSorted[index][0] > c[0]:
                break
            elif tempSorted[index][0] == c[0]:
                if tempSorted[index][1] == 0:
                    index+=1
                break
            index += 1
        tempSorted.insert(index, c)
    return tempSorted


def removeContradiction1(s,seq):
    result = []
    for clauses in s:
        temp = clauses
        for element in seq:
            if (element, "N") in clauses and (element, 0) in clauses:
                temp.remove((element, "N"))
                temp.remove((element, 0))
        result.append(temp)
    return result

def removeContradiction(s,seq):
    result = s[:]
    for clause in s:
        for element in seq:
            if (element, "N") in clause and (element, 0) in clause:
                result.remove(clause)
                break
    return result

# (By default, set1 is normal set and set2 is negation set)
def resolve(set1, set1Index, set2, set2Index, target):
    result = []
    index = 0
    record = dict()
    for i in range(len(set1)):
        for j in range(len(set2)):
            temp = set1[i][:]
            temp.remove((target,0))
            for item in set2[j]:
                if item != (target, "N") and item not in temp:
                    temp.append(item)
            temp = sortClause(temp)
            if temp not in result:
                result.append(temp)
                pair = [set1Index[i],set2Index[j]]
                pair.sort()
                record[index] = [pair]
                index += 1
            else:
                pair = [set1Index[i],set2Index[j]]
                pair.sort()
                record[result.index(temp)].append(pair)
    return result, record
            

def printLine(s):
    result = []
    for item in s:
        if item[1] == "N":
            result.append("¬"+item[0])
        else:
            result.append(item[0])
    print(result)


def printSetWithIndex(s,name,indexSet):
    print(name + " {")
    for i in range(len(s)):
        print("Index: " + str(indexSet[i]))
        printLine(s[i])
    print("}")
    print("Size = " + str(i+1))
    print()


def printSet(s,name):
    print(name + " {")
    for i in range(len(s)):
        print("Index: " + str(i+1))
        printLine(s[i])
    print("}")
    print("Size = " + str(i+1))
    print()


def printResolvent(s,name,record):
    print(name + " {")
    for i in range(len(s)):
        print("  Pairs: " + str(record[i]))
        printLine(s[i])
    print("}")
    print("Size = " + str(i+1))
    print()



############ ALGORITHM STARTS ############

currT = []
currU = [] # list of resolvents
currG = [] # list of remainings
currS = sortSet(S)
currSp = removeContradiction(currS,seq)


for r in range(num):
    print("################ ROUND " + str(r+1) + " ################")
    neg = []
    negIndex = []
    normal = []
    normalIndex = []
    TIndex = []
    for i in range(len(currSp)):
        if (seq[r], 0) in currSp[i] or (seq[r], "N") in currSp[i]:
            currT.append(currSp[i])
        else:
            currG.append(currSp[i])


    for i in range(len(currT)):
        TIndex.append(i+1)
        if (seq[r], 0) in currT[i]:
            normal.append(currT[i])
            normalIndex.append(TIndex[i])
        elif (seq[r], "N") in currT[i]:
            neg.append(currT[i])
            negIndex.append(TIndex[i])

    ## PRINTER ##
            
    printSetWithIndex(currT, "T"+str(r+1) , TIndex)
    
    ## DEBUGGERS ##
    
    #printSetWithIndex(normal, "Non-negation Set", normalIndex)
    #printSetWithIndex(neg, "Negation Set", negIndex)
    #printSet(currG,"currG")

    currU, URecords = resolve(normal, normalIndex, neg, negIndex, seq[r])
    printResolvent(currU, "U"+str(r+1), URecords)

    currS = currG + currU
    printSet(currS, "S"+str(r+2))
    currSp = removeContradiction(currS,seq)
    printSet(currSp, "S'"+str(r+2))

    currT = []
    currG = []
    currU = []


