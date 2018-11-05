import pandas as pd
import numpy as np
import numbers

class tree():
    def __init__(self, value):
        self.value = value
        self.root = False
        self.depth = -1
        self.leftChild = None
        self.rightChild = None
    def insert_right(self, value):
        self.rightChild =tree()
        self.value = value
    def insert_right(self, value):
        self.leftChild =tree()
        self.value = value

def create_tree(queue_1, starTree):
    queue = queue_1.copy()
    print("queue", queue)
    while len(queue)>0:
        # if starTree.rightChild != None:
        #     return
        if starTree.root == True:
            starTree.rightChild = bTree('X')
            starTree.rightChild.depth = 0
            starTree = starTree.rightChild
            continue
        if isinstance(queue[0], numbers.Number):
            if starTree.rightChild == None:
                starTree.rightChild = bTree(queue[0])
                starTree.rightChild.depth = starTree.depth + 1
            print(queue[0])
            queue.pop(0)
            starTree = starTree.rightChild
        else:
            print('exception')
            # if starTree.rightChild != None:
            queue.pop(0)
            if starTree.rightChild == None:
                starTree.rightChild = bTree(0)
                starTree.rightChild.depth = starTree.depth + 1
                right_child = starTree.rightChild
                create_tree(queue.copy(), right_child)
            if starTree.leftChild == None:
                starTree.leftChild = bTree(1)
                starTree.leftChild.depth = starTree.depth + 1
                left_child = starTree.leftChild
                create_tree(queue.copy(), left_child)
    return(queue_1.copy())

list_values = [1, 2, 3, 4, 5, "?", "*", 6]
queue = list_values
bTree = tree
starTree = bTree('X')
starTree.root = True
main_root = starTree
create_tree(queue, starTree)
print(main_root)