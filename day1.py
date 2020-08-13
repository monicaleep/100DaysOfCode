class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self,value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

a_node = BinaryTree('a')
a_node.insert_right('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')


def pre_order(self):
    print(self.value)
    if self.left_child:
        self.left_child.pre_order()
    if self.right_child:
        self.right_child.pre_order()

def in_order(self):
    if self.left_child:
        self.left_child.in_order()
    print(self.value)
    if self.right_child:
        self.right_child.in_order()

# todo post-order

## Search in a Binary Search Tree
def find_node(self,value):
    if value < self.value and self.left_child:
        return self.left_child.find_node(value)
    if value > self.value and self.right_child:
        return self.right_child.find_node(value)
    return value == self.value
