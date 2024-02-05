# Using LinkedList
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,val):
        nd = Node(val)
        if (self.head is None):
            self.head = nd
            self.tail = self.head
        else:
            self.tail.next = nd
            self.tail = nd
        self.size +=1

    def dequeue(self):
        if self.size == 0: return None
        val = self.head.val
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return val

    def peek(self):
        return self.head.val if self.head else None

    def printQ(self):
        if self.size == 0: return None
        cNode = self.head
        while(cNode):
            print(cNode.val, end=' <- ')
        cNode = cNode.next
        print('\n')

# Usin stack
class queueFromStack():
    def __init__(self):
        self.stk1 = [] # stack enqueue or push operation
        self.stk2 = [] # stack dequeue or pop operation
        self.size = 0

    def isEmpty(self):
        return self.size==0

    def enqueue(self,item):
        self.stk1.append(item)
        self.size +=1

    def dequeue(self):
        if self.size==0: return None
        if not self.stk2:
            while self.stk1: self.stk2.append(self.stk1.pop())
        self.size -=1
        return self.stk2.pop()

    def peek(self):
        if self.size == 0: return None
        if not self.stk2:
            while self.stk1: self.stk2.append(self.stk1.pop())
        return self.stk2[-1]

    def print(self):
        print(" <- ".join(self.stk1))

if __name__ == '__main__':
    q = Queue()
    q.enqueue('Joy'); q.enqueue('Deep'); q.enqueue('Basu')
    print(q.peek())
    q.printQ()
    print(q.dequeue());print(q.dequeue());
    q.printQ()
    q.enqueue('Joy');
    print(q.peek());
    print(q.size)

    qs = queueFromStack()
    for i in range(3): qs.enqueue(i)
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.dequeue())
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.isEmpty())
    qs.enqueue(3);
    qs.enqueue(4);
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.dequeue())
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.dequeue())
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.dequeue())
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.dequeue())
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    print(qs.dequeue())
    print("Stack1: ", qs.stk1, "\nStack2: ", qs.stk2)
    ##############################################
    for i in range(3): qs.enqueue(i)
    qs.dequeue()
    print(qs.peek())
    print(qs.isEmpty())