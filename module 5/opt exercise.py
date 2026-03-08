def sort_characaters():
    """
Implement the remove node method without helper functions
Implement a remove node method called "delete_node" without using the helper functions you saw on the course. 
You should, of course use the functionality of the helper functions, but including the relevant parts in your own code. 
You have an algorithm example in the Wikipedia page about Binary Search Trees. 
The method should accept a value of the data that the node to be deleted contains (this is for making the method easier to the end user of the class). 
The method should find the node to be deleted based on the given value (it's allow to use the _find helper method of the class)

To be fair, the algorithm presented in the Wikipedia page uses its own small "shift_nodes" helper function. You can use that as well.
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

    def delete_node(self, data):
        """
        Deletes the node containing 'data'
        """
        node = self._find(data)
        if node is None:
            return  # Value not found

        def shift_nodes(u, v):
            """
            Replaces subtree rooted at u with subtree rooted at v
            """
            if u._parent is None:
                self._root_node = v
            elif u == u._parent._left_child:
                u._parent._left_child = v
            else:
                u._parent._right_child = v

            if v is not None:
                v._parent = u._parent

        # Case 1: No left child
        if node._left_child is None:
            shift_nodes(node, node._right_child)

        # Case 2: No right child
        elif node._right_child is None:
            shift_nodes(node, node._left_child)

        # Case 3: Two children
        else:
            # Find successor (minimum of right subtree)
            successor = node._right_child
            while successor._left_child:
                successor = successor._left_child

            if successor._parent != node:
                shift_nodes(successor, successor._right_child)
                successor._right_child = node._right_child
                successor._right_child._parent = successor

            shift_nodes(node, successor)
            successor._left_child = node._left_child
            successor._left_child._parent = successor