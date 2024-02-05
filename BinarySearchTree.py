# Design a Binary Search Tree (BST) with methods
# 1. Insert, 2. Lookup, 3. Remove, 4. BFS, 5. DFS_InOrder, 6. DFS_PreOrder, 7.DFS_PostOrder
from tree import drawTree
from collections import deque

class binaryNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self): self.root = None

    def print(self): drawTree(self.root)

    def insert(self, val):
        bNode = binaryNode(val)
        if self.root is None: self.root = bNode
        curNode = self.root
        while curNode:
            if bNode.value == curNode.value: return
            if bNode.value > curNode.value:
                if curNode.right: curNode = curNode.right; continue
                curNode.right = bNode; return
            else:
                if curNode.left: curNode = curNode.left; continue
                curNode.left = bNode; return

    def search(self, val):
        if self.root is None: return None
        curNode = self.root
        while curNode:
            if curNode.value == val: return curNode
            if val > curNode.value: curNode = curNode.right; continue
            if val < curNode.value: curNode = curNode.left; continue
        return None

    def remove(self, input_val): ## Not working ##
        def helper(node, searchVal):
            if node is None: return None
            if searchVal < node.value:
                node.left = helper(node.left, searchVal)
            elif searchVal > node.value:
                node.right = helper(node.right, searchVal)
            else:
                if node.left is None: return node.right
                if node.right is None: return node.left
# Node with two children: Get the in-order successor (smallest in the right subtree)
                min_node = node.right
                while min_node.left: min_node = min_node.left
                node.right = helper(min_node, min_node.value)
            return node
        self.root = helper(self.root, input_val)

    def BFS(self):
        q, arr = deque(), []
        if self.root is None: return []
        q.append(self.root)
        while q:
            curNode = q.popleft()
            arr.append(curNode.value)
            if curNode.left: q.append(curNode.left)
            if curNode.right: q.append(curNode.right)
        return arr

    def DFS_InOrder(self):
        def traverseInOrder(node, arr): # InOrder: Left Node (recursive) -> Parent Node -> Right Node (recursive)
            if node.left: traverseInOrder(node.left, arr)
            arr.append(node.value)
            if node.right: traverseInOrder(node.right, arr)
            return arr
        return traverseInOrder(self.root, []) # recursive call from stage

    def DFS_PreOrder(self):
        def traversePreOrder(node, arr): # PreOrder: Parent Node -> Left Node (R) ->
            Right Node (R)
            arr.append(node.value)
            if node.left: traversePreOrder(node.left, arr)
            if node.right: traversePreOrder(node.right, arr)
            return arr
        return traversePreOrder(self.root, []) # recursive call from stage

    def DFS_PostOrder(self):
        def traversePostOrder(node, arr): # PreOrder: Left Node (R) -> Right Node (R) -> Parent Node
            if node.left: traversePostOrder(node.left, arr)
            if node.right: traversePostOrder(node.right, arr)
            arr.append(node.value)
            return arr
        return traversePostOrder(self.root, []) # recursive call from stage

####################################################################

if __name__ == '__main__':
    myBST = binarySearchTree()
    for num in [20, 40, 8, 45, 43, 36, 19, 1, 47, 29, 42, 44, 30]: myBST.insert(num)
    # for num in [x for x in range(10)]: myBST.insert(num)
    myBST.print()
    # exit(0)
    print('BFS list:', myBST.BFS())
    print('DFS In Order: ', myBST.DFS_InOrder())
    print('DFS Pre Order: ', myBST.DFS_PreOrder())
    print('DFS Post Order: ', myBST.DFS_PostOrder())
    print('Looking up for value (28):', myBST.search(30))
    for num in [40, 42, 20]: myBST.remove(num)
    myBST.print()
    print(myBST.depth())