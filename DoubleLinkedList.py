# Create a Doubly LinkedList with below properties (1.Head,2.Tail,3.Length)
# Problem: DLL FLattening with ChildDLLs or SubChildDLLs
import treevizer

class Node:
    def __init__(self,val=None):
        self.next = None
        self.prev = None
        self.data = val
        self.child = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        treevizer.to_png(self.head, structure_type="ll", dot_path="dll.dot",png_path="dll.png")

    def addChildDLL(self,index,chlDLL):
        if index<0 or index>self.length-1: return None
        if index==0:
            cNode = self.head
        elif index==self.length-1:
            cNode = self.tail
        else:
            cNode = self.head
            for x in range(1,index+1): cNode = cNode.next
        cNode.child = chlDLL.head

    def flattenDLL(self):
        psNode = self.head
        while(psNode):
            if psNode.child is not None:
                peNode = psNode.next
                csNode = psNode.child
                while(csNode): ceNode = csNode; csNode = csNode.next

                psNode.next = psNode.child
                psNode.child.prev = psNode

                ceNode.next = peNode
                peNode.prev = ceNode

                psNode.child = None

            psNode = psNode.next


    def push(self,nval):
        nd = Node(nval)
        if self.head is None:
            self.head = nd
            self.tail = self.head
        else:
            self.tail.next = nd
            nd.prev = self.tail
            self.tail = nd
        self.length +=1

    def printDll(self):
    # nd=self.head
    # while nd: print(nd.stage,end='<->'); nd=nd.next
    # print("\n")
        print(self.buildMap(self.head))

    def buildMap(self,pNode):
        tempMap = {}
        while(pNode):
            if pNode.child is not None:
                tempMap[pNode.data] = self.buildMap(pNode.child)
            else:
                tempMap[pNode.data] = {}
            pNode = pNode.next
        return tempMap

if __name__ == '__main__':
    dll = DoublyLinkedList(); dll1 = DoublyLinkedList(); dll3 = DoublyLinkedList()
    dll11 = DoublyLinkedList(); dll33 = DoublyLinkedList()
    for x in range(0,10): dll.push(x)
    for x in range(10,15): dll1.push(x)
    for x in range(30,40): dll3.push(x)
    for x in range(120,125): dll11.push(x)
    for x in range(330,333): dll33.push(x)
    dll1.addChildDLL(2,dll11)
    dll3.addChildDLL(3,dll33)
    dll.addChildDLL(1,dll1); dll.addChildDLL(3,dll3)
    dll.printDll()
    dll.flattenDLL() # DLL Flattening Test
    dll.printDll()