#!/usr/bin/python3

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


class Stack:
    """ Stack class with a Linked List
    peek(), isEmpty(), delete(), pop(), push()
    """
    def __init__(self):
        self.head = None
    
    def push(self, val: int):
        """
        Push a node to the stack
        
        When you push a node to to stack, the new node becomes
        the head of the linked list
        """
        temp = self.head
        try:
            new_node = Node(val)
        except TypeError:
            print("node value must be an integer")
            return
        if temp is not None:
            new_node.next_node = temp
            self.head = new_node
        else:
            self.head = new_node
    
    def isEmpty(self):
        """ Check if stack is empty """
        return self.head == None
    
    def peek(self):
        """ Peek at the topmost element of the stack """
        return self.head.data
    
    def pop(self):
        """ Pop the topmost element of the stack """
        temp = self.head
        if not self.isEmpty():
            top_node = temp
            self.head = temp.next_node
            return top_node.data
        else:
            return "Empty stack!"
    
    def __str__(self):
        """ Print the elements of the stack """
        temp: Node = self.head
        values = []
        while temp is not None:
            values.append(temp.data)
            temp = temp.next_node
        values = [str(x) for x in values]
        return '\n==\n'.join(values)
    
    def delete(self):
        """ Delete the stack """
        self.head = None
        return

if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    #stack.delete()
    print(stack)
