#!/usr/bin/python3
""" Tree Data Structure with Linked Lists """
from __future__ import annotations
from typing import Union, List, Dict, Mapping, Sequence


class TreeNode:
    def __init__(self, data: int, left_child: TreeNode = None, right_child: TreeNode = None):
        """ Initialize the properties of a tree node """
        if not isinstance(data, int):
            raise TypeError("value must be an integer!")
        self.__data = data
        if left_child and not isinstance(left_child, TreeNode):
            raise TypeError(
                f"left child must be a {self.__class__.__name__} type")
        self.__left_child = left_child
        if right_child and not isinstance(right_child, TreeNode):
            raise TypeError(
                f"right child must be a {self.__class__.__name__} type")
        self.__right_child = right_child

    @property
    def data(self) -> int:
        """ Getter for data attribute """
        return self.__data

    @data.setter
    def data(self, val: int):
        """ Setter attribute for data """
        if not isinstance(val, (str, int)):
            raise TypeError("value must be an integer or a string")
        self.__data = val

    @property
    def left_child(self):
        """ Getter for left child attribute """
        return self.__left_child

    @left_child.setter
    def left_child(self, val: TreeNode):
        """ Setter for children attribute """
        if not isinstance(val, TreeNode) or val is None:
            raise TypeError(
                f"left child must be a {self.__class__.__name__} object")
        else:
            self.__left_child = val

    @property
    def right_child(self):
        """ Getter for left child attribute """
        return self.__right_child

    @right_child.setter
    def right_child(self, val: TreeNode):
        """ Setter for children attribute """
        if not isinstance(val, TreeNode) or val is None:
            raise TypeError(
                f"right child must be a {self.__class__.__name__} object")
        else:
            self.__right_child = val

    def __str__(self, level=0):
        """ String representation of a tree node"""
        ret = " " * level + str(self.__data) + "\n"
        for child in self.__children:
            ret += child.__str__(level + 1)
        return ret


class Node:
    """ Node Class """

    def __init__(self, data, next_node=None):
        """Initializes a  Node"""
        if not isinstance(data, int):
            raise TypeError("value must be an integer")
        self.__data = data
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """ Getter for value attribute """
        return self.__data

    @data.setter
    def data(self, val: int):
        """ Setter attribute for value """
        if not isinstance(val, int):
            raise TypeError("value must be an integer")
        self.__data = val

    @property
    def next_node(self):
        """ Getter for next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, val):
        """ Setter for next_node attribute """
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = val

class Queue:
    def __init__(self):
        """ Initialize the head node """
        self.head = None
    
    def isEmpty(self):
        """ check if a queue is empty """
        temp = self.head
        return temp == None
    def __str__(self):
        """Print a queue """
        if self.isEmpty():
            return "queue is empty"
        temp: Node = self.head
        values = []
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return "->".join(values)
    def enqueue(self, val: int):
        """ Enqueue an element to the back of the queue"""
        temp : Node = self.head
        try:
            new_node = Node(val)
        except Exception:
            print("node value must be an integer")
            return
        if temp is not None:
            while temp.next_node is not None:
                temp = temp.next_node
            temp.next_node = new_node
            new_node.next_node = None
        else:
            self.head = new_node
            new_node.next_node = None
    
    def dequeue(self):
        """ Dequeue an element at the front of the queue """
        temp = self.head
        if not self.isEmpty():
            self.head = temp.next_node
        else:
            return "queue is empty"
        return temp.data
    
    def peek(self):
        """ Peek at the element at the front of the queue """
        if not self.isEmpty():
            return self.head.data
        return "queue is empty"
    
    def delete(self):
        """ Delete a queue """
        self.head = None
    
    def rotate(self):
        """ Shuffle queue """
        temp = self.dequeue()
        self.enqueue(temp)





def pre_order_traversal(root_node: TreeNode):
    """
    Pre order traversal of a binary tree
    
    Root => Left child => Right Child
    """
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

def in_order_traversal(root_node: TreeNode):
    """
    Inorder traversal of a binary tree
    
    Left child => Root => Left Child
    """
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(f"{root_node.data}", end="=>")
    in_order_traversal(root_node.right_child)

def post_order_traversal(root_node: TreeNode):
    """
    Post order traversal for a binary tree
    
    Left Child => Right Child => Root
    """
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(f"{root_node.data}", end="=>")

def level_order_traversal(root_node: TreeNode):
    """ Use Queue data structure for level order traversal """
    if not root_node:
        return
    else:
        custom_queue = Queue()
        # Insert the root node into the Queue
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)



    

if __name__ == "__main__":
    root_node = TreeNode(1)
    left_child_root = TreeNode(2)
    right_child_root = TreeNode(3)
    left_child_2 = TreeNode(4)
    right_child_2 = TreeNode(5)
    left_child_3 = TreeNode(6)
    right_child_3 = TreeNode(7)
    left_child_4 = TreeNode(9)
    right_child_4 = TreeNode(10)

    
    root_node.left_child = left_child_root
    root_node.right_child = right_child_root
    
    left_child_root.left_child = left_child_2
    left_child_root.right_child = right_child_2
    
    left_child_2.left_child = left_child_4
    left_child_2.right_child = right_child_4
    
    right_child_root.left_child = left_child_3
    right_child_root.right_child = right_child_3
    
    #print(root_node)
    print(post_order_traversal(root_node))
