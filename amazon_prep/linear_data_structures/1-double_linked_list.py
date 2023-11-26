#!/usr/bin/python3
""" Double Linked List """


class Node:
    def __init__(self, data: int, next_node: Node = None, prev_node: Node = None):
        """Initializes a  Node"""
        if not isinstance(data, int):
            raise TypeError("value must be an integer")
        self.__data = data
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
        if prev_node and not isinstance(prev_node, Node):
            raise TypeError("prev_node must be a Node object")
        self.__prev_node = prev_node

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

    @property
    def prev_node(self):
        """ Getter for prev_node attribute """
        return self.__prev_node

    @prev_node.setter
    def prev_node(self, val):
        """ Setter for next_node attribute """
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__prev_node = val


class DoubleLinkedList:
    def __init__(self):
        """Initialize the head of a list """
        self.head = None
    
    def insert_at_head(self, val:int):
        """ Insert a node at the head """
        