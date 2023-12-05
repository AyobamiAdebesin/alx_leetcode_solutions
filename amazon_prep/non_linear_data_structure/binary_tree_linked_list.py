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
