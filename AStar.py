
"""
graph = {
    "src":[("A",10),("B",11)],
    "A":[("C",12),("D",15)],
    "B" :[("E",5),("F",34)],
    "C":[],
    "D":[],
    "E":[],
    "F" :[("dest",2)],
    "dest":[]
    }

heuristicValue = {
    "src":100,
    "A":90,
    "B":80,
    "C":70,
    "D":60,
    "E":50,
    "F":40,
    "dest":0
    }

needToVisit = [("src",0)]

while needToVisit :
    bestNode = needToVisit[0]
    for currentNode in needToVisit :
        if currentNode[1] + heuristicValue[currentNode[0]] < bestNode[1] + heuristicValue[bestNode[0]] :
            bestNode = currentNode
    needToVisit.remove(bestNode)

    node = bestNode[0]
    cost = bestNode[1]

    print(node ,cost , end=" ")

    if(node == "dest") :
        print("Goal Node found")
        break
        

    for child , edgeCost in graph[node]:
        needToVisit.append((child,cost + edgeCost))


needToVisit = [("src",0)]

while needToVisit :
    bestNode = needToVisit[0]
    for currentNode in needToVisit :
        if currentNode[1] + heuristicValue[currentNode[0]] < bestNode[1] + heuristicValue[bestNode[0]] :
            bestNode = currentNode

    needToVisit.remove(bestNode)

    node = bestNode[0]
    cost = bestNode[1]

    print("\n node:" ,node , ",cost:",cost , "\n")

    if node == "dest" :
        print("Goal Node found")
        break

    for child, edgeCost in graph[node]:
        needToVisit.append((child,edgeCost + cost))


"""
"""
graph = {
    "S" : ["A","B","C"],
    "A" : ["B","D"],
    "B" : ["D"],
    "C" : ["E","F","D"],
    "D" : ["H","I","F"],
    "E" : ["G"],
    "F" : ["G"],
    "G" : ["dest"],
    "H" : ["I","J"],
    "I" : ["J","K","G"],
    "J" : ["K"],
    "K" : ["G"]
    }

"""
graph = {
    "S" : [("A",4),("B",10),("C",11)],
    "A" : [("B",8),("D",5)],
    "B" : [("D",15)],
    "C" : [("E",20),("F",2),("D",8)],
    "D" : [("H",16),("I",20),("F",1)],
    "E" : [("G",19)],
    "F" : [("G",13)],
    "G" : [],
    "H" : [("I",1),("J",2)],
    "I" : [("J",5),("K",13),("G",5)],
    "J" : [("K",7)],
    "K" : [("G",16)],
    
    }

heuristicValue = {

    "S":7,
    "A" :8 ,
    "B" : 6,
    "C" : 5 ,
    "D" : 5,
    "E" :3,
    "F" :3 ,
    "G" : 0 ,
    "H" : 7 ,
    "I":4,
    "J" :5 ,
    "K" :3 
    }
needToVisit = [("S",0)]

while needToVisit :
    bestNode = needToVisit[0]
    for currentNode in needToVisit :
        if heuristicValue[currentNode[0]] + currentNode[1] < heuristicValue[bestNode[0]] + bestNode[1]:
            bestNode = currentNode

    needToVisit.remove(bestNode)
    node = bestNode[0]
    cost = bestNode[1]
    
    print("\n Node : " , bestNode , "cost : " , cost )

    if node == "G" :
        print("Goal Node found ")
        break

    for child,edgeCost in graph[node]:
        needToVisit.append((child,cost+edgeCost))

#    needToVisit.extend(graph[bestNode])








