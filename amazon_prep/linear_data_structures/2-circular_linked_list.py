#!/usr/bin/python3
""" Circular Linked List """


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


class CircularSinglyLinkedList:
    def __init__(self):
        """ Initialize head and tail reference for a Circular Linked List"""
        self.head = None
        self.tail = None

    def insert_at_head(self, val: int) -> None:
        """ Insert a node at the head """
        try:
            new_node = Node(val)
        except TypeError:
            print("node value must be an integer")
            return
        temp = self.head
        if temp is None:
            self.head = new_node
            self.head.next_node = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return

    def insert_at_tail(self, val: int) -> None:
        """ Insert a node at the end of the list """
        temp = self.head
        try:
            new_node = Node(val)
        except TypeError:
            print("node value must be an integer")
            return
        if temp is not None:
            while temp.next_node != self.head:
                temp = temp.next_node
            new_node.next_node = self.head
            temp.next_node = new_node
        else:
            self.insert_at_head(val)
        return

    def __str__(self):
        """ Print the elements of the list """
        values = []
        temp = self.head
        if temp is not None:
            while temp.next_node != self.head:
                values.append(str(temp.data))
                temp = temp.next_node
            values.append(str(temp.data))
        return ('->'.join(values))

    def insert_node_at(self, val:int, pos:int) -> None:
        """ Insert a node in the middle of the list """
        temp = self.head
        curr_pos = 1
        if not isinstance(pos, int) or pos < 0:
            print("position must be an integer greater than zero")
            return
        if pos > self.list_size():
            print("invalid position!")
            return
        if temp is not None:
            try:
                new_node = Node(val)
            except TypeError:
                print("node value must be an integer")
                return
            while curr_pos < pos and temp is not None:
                if curr_pos == pos-1:
                    break
                temp = temp.next_node
                curr_pos += 1
            new_node.next_node = temp.next_node
            temp.next_node = new_node
        return
    
    def list_size(self) -> int:
        """ Return the length of the list """
        temp = self.head
        count = 1
        if temp is not None:
            while temp.next_node != self.head:
                temp = temp.next_node
                count += 1
        else:
            return 0
        return count
    
    def find_node(self, node_value: int):
        """ Find the value of a node in a list"""
        temp = self.head
        while temp is not None:
            if temp.data == node_value:
                return temp.data
            else:
                temp = temp.next_node
        return f"{node_value} does not exists in the list"
    
    def delete_first_node(self):
        """ Delete the first node """
        temp = self.head
        if temp.next_node == self.head:
            self.head = None
        else:
            self.head = temp.next_node
            temp = None
    
    def delete_node_at(self, node_pos):
        """ Delete a given node """
        temp = self.head
        count = 1
        next_node: Node = None
        if temp is not None:
            while count < node_pos-1:
                count += 1
                temp = temp.next_node
            if temp.next_node is not None:
                next_node = temp.next_node
                temp.next_node = next_node.next_node
        return
    
    def delete_last_node(self):
        """ Delete the last node in the list """
        temp = self.head
        while temp is not None:
            return


if __name__ == "__main__":
    dll = CircularSinglyLinkedList()
    dll.insert_at_head(1)
    dll.insert_at_tail(2)
    dll.insert_at_tail(3)
    dll.insert_node_at(5, -10)
    print(dll)
    print(f"Size of the list: {dll.list_size()}")