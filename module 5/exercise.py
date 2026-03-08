def sort_characters():
    """
    Write a method that finds a node that holds a certain value
Given a basic BST structure (included), add a _find() method to it, to search for values in the tree. The basic definition of the method is already included. Start from the root node and move to the appropriate nodes searching for the wanted value. The method should return the node that holds the value or None if the value is not found.

Notice that the Node object, when printed, prints some odd code. This is done on purpose to help checking on the exercises.
    
"""
class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        
        current_node = self._root_node

        while current_node is not None:
            if data == current_node.data:
                return current_node
            elif data < current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        return None


def sort_characters():
    """
Write methods to find the minimum and maximum values of a tree
Given a basic BST structure (included), write two methods: one, called find_maximum(), to find the maximum value of the tree and another one, called find_minimum(), to find the minimum value of the tree. The methods should not accept parameters and return the nodes containing the maximum and minimum values of the tree respectively. The basic definition for the methods are already included.

"""

class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif data < current.data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def find_minimum(self):
       
        current = self._root_node
        if current is None:
            return None

        while current._left_child:
            current = current._left_child

        return current

    def find_maximum(self):
       
        current = self._root_node
        if current is None:
            return None

        while current._right_child:
            current = current._right_child

        return current


def sort_characters():
    """
    Write a method that detach a node from the tree
Given a basic BST structure (included), add a _detach_node() method to it, to search for values in the tree. The basic definition of the method is already included. The method accepts the node to be deleted as parameter and returns nothing.

The method should check on parent and possible children to change the connections and be sure that the tree remains functional after safely detaching the node from the tree. If the node to detach has two children, the method should raise a ValueError (it is not possible to just detach a node with two children from a BST). The method should also take into account when the node to detach is the root node.

Notice that the Node object, when printed, prints some odd code. This is done on purpose to help checking on the exercises.
    """


class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif data < current.data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        
        if node is None:
            return

       
        if node._left_child and node._right_child:
            raise ValueError

       
        child = node._left_child if node._left_child else node._right_child

        
        if node._parent is None:
            self._root_node = child
            if child:
                child._parent = None

        
        elif node._parent._left_child == node:
            node._parent._left_child = child
            if child:
                child._parent = node._parent

        
        else:
            node._parent._right_child = child
            if child:
                child._parent = node._parent

        
        node._parent = None
        node._left_child = None
        node._right_child = None