# Stack using Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        nd = Node(value)
        nd.next = self.top
        self.top = nd
        self.size+=1

    def pop(self):
        if self.top is None: return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.top is None: return None
        return self.top.value

    def length(self): return self.size

    def print(self):
        cnode = self.top
        while cnode:
            print(cnode.value,end=" -> ")
            cnode=cnode.next
        print("None")

# Using List
class stacklist():
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self,val):
        self.arr.append(val)
        self.size = len(self.arr)

    def pop(self):
        self.arr.pop()
        self.size = len(self.arr)

    def peek(self):
        if self.size >0:
            return (self.arr[self.size - 1])
        else:
            return None

    def lookup(self, val):
        print(self.arr.index(val)) if val in self.arr else print('Not found')

    def printStack(self):
        print(self.arr)

if __name__ == '__main__':
    stk = Stack()
    for i in range(1,11,2): stk.push(i)
    stk.print()
    stk.push(100)
    stk.print()
    print(stk.length())
    print(stk.peek())
    stk.pop()
    stk.print()
    while stk.length(): val = stk.pop(); print(val)

    stklst = stacklist()
    stklst.push('Joy')
    stklst.push('deep')
    stklst.push('Basu')
    stklst.lookup('Basu')
    print(stklst.peek())
    stk.pop()
    print(stk.peek())