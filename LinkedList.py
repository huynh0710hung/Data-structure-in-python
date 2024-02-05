# Create a Singly LinkedList with below Properties (1.Head,2.Tail,3.Length)
# methods (1.Push,2.Pop,3.Shift,4.Unshift,5.Get,6.Set,7.Insert,8.Remove,9.Reverse)
import treevizer
import os
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        treevizer.to_png(self.head, structure_type="ll", dot_path=r"sll.dot", png_path=r"sll.png")

    def push(self,nval):
        nd = Node(nval)
        if self.head is None:
            self.head = nd
            self.tail = self.head
        else:
            self.tail.next = nd
            self.tail = nd
            self.length +=1

    def pop(self):
        if self.length == 0: return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            cNode = self.head
            for x in range(1, self.length-1):
                cNode = cNode.next
            self.tail = cNode
            cNode.next =None

        self.length -=1
        return self

    def get(self, index):
        if self.length > index and index >= 0:
            cNode = self.head
            if index == 0: return cNode.data
            for x in range(1, index+1):
                cNode = cNode.next
            return cNode.data
        return None

    def set(self, index,nval):
        if self.length > index and index >= 0:
            cNode = self.head
            if index == 0:
                cNode.data = nval
                return True
            for x in range(1, index+1):
                cNode = cNode.next
            cNode.data = nval
            return True
        return False

    def reverse(self):
        prevNode, curNode = None, self.head
        self.tail = curNode
        while (curNode):
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        self.head = prevNode

    def reversePos(self,start,end):
        if start > 0 and end <self.length -1:
            sNode = eNode = self.head
            for x in range(1,start):
                sNode = sNode.next
            for x in range(1,end+1):
                eNode = eNode.next
            headNode = sNode
            tailNode = eNode.next
            prevNode = tailNode
            curNode = headNode.next
            while(curNode is not tailNode):
                nextNode = curNode.next
                curNode.next = prevNode
                prevNode = curNode
                curNode = nextNode
            headNode.next = prevNode

    def printSll(self):
        cNode = self.head
        lst = []
        while(cNode):
            lst.append(cNode.data)
            cNode = cNode.next
        print(lst)

if __name__ == '__main__':
    sll = SinglyLinkedList()
    for x in range(1,11): sll.push(x)

    sll.print()
    sll.printSll()
    sll.reversePos(1,7)
    sll.printSll()
    print('Head [', sll.head.data,']')
    print('Tail [',sll.tail.data,']')

