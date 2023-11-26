#!/usr/bin/python3
""" Tree Data Structure with Python Lists """
from typing import Union, List, Dict, Mapping, Sequence


class TreeNode:
    def __init__(self, data: Union[str, int], children: List = []):
        """ Initialize the properties of a tree node """
        if not isinstance(data, (str, int)):
            raise TypeError("value must be an integer or a string")
        self.__data = data
        if children and not isinstance(children, list):
            raise TypeError("children must be a list object")
        self.__children = children

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
    def children(self):
        """ Getter for children attribute """
        return self.__children

    @children.setter
    def children(self, val):
        """ Setter for children attribute """
        if not isinstance(val, list) and val is not None:
            raise TypeError("children must be a list object")
        else:
            self.__children = val

    def __str__(self, level=0):
        """ String representation of a tree node"""
        ret = " " * level + str(self.__data) + "\n"
        for child in self.__children:
            ret += child.__str__(level + 1)
        return ret
        # lines = []
        # level = [self]
        # while level:
        #     lines.append(' '.join(str(node.__data) for node in level))
        #     next_level = list()
        #     for n in level:
        #         if n.__children:
        #             next_level.extend(n.__children)
        #     level = next_level
        # return '\n'.join(lines)

    def add_child(self, tree_node):
        """ Add a child to a node """
        if not len(self.__children) > 2:
            self.children.append(tree_node)
        else:
            raise ValueError("node can only have 2 children")


if __name__ == "__main__":
    tree = TreeNode("Drinks", [])
    
    cold = TreeNode("Cold", [])
    pepsi = TreeNode("Pepsi", [])
    fanta = TreeNode("Fanta", [])

    hot = TreeNode("Hot", [])
    tea = TreeNode("Tea", [])
    coffee = TreeNode("Coffee", [])
    
    tree.add_child(cold)
    tree.add_child(hot)
    cold.add_child(pepsi)
    cold.add_child(fanta)
    hot.add_child(tea)
    hot.add_child(coffee)
    print(tree)
