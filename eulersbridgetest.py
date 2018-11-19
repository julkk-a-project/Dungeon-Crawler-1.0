
class eulerNode():
        def __init__(self):
            self.Name = ""
            self.connections = []
        def setName(self, nName):
            self.Name = "Node"+str(nName)
        def setConnection(self, node):
            self.connections.append(node)
        def printConnections(self):
            print("I,",self.Name,"Have the following connections:\n---------------------------------------")
            for i in range(0,len(self.connections)):
                print(self.connections[i].Name)
            print("I,",self.Name,"Have Spoken.\n---------------------------------------")
        


def game():

    def eulerBridge(x):
        node0 = eulerNode()
        node0.setName(0)
        node1 = eulerNode()
        node1.setName(1)
        node2 = eulerNode()
        node2.setName(2)
        node3 = eulerNode()
        node3.setName(3)
        node4 = eulerNode()
        node4.setName(4)
        node5 = eulerNode()
        node5.setName(5)
        node6 = eulerNode()
        node6.setName(6)
        node7 = eulerNode()
        node7.setName(7)
        node8 = eulerNode()
        node8.setName(8)
        node9 = eulerNode()
        node9.setName(9)
        allNodes = [node0,node1,node2,node3,node4,node5,node6,node7,node8,node9]
        for i in range(0,10):
            for j in range(0,10):
                allNodes[i].setConnection(allNodes[j])
            allNodes[i].printConnections()
            def location(node0):
                node0.printConnections()
        location(node0)
        
        
    #def createNodes(n):


    def main():
        eulerBridge(5)
    
    main()

game()
