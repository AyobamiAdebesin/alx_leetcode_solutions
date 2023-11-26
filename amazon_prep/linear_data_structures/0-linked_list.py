#!/usr/bin/python3
""" Singly Linked List """


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


class SinglyLinkedList:
    """ Singly Linked List class """

    def __init__(self):
        """ Initializes head of a Singly Linked List"""
        self.head = None

    def insert_at_head(self, data: int):
        """ Insert a Node at the head of a singly linked list """
        try:
            new_node = Node(data)
        except TypeError:
            print("node data must be an integer")
            return
        if self.head is None:
            new_node.next_node = None
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_tail(self, val: int):
        """ Insert a node at the end of a singly linked list """
        try:
            new_node = Node(val)
        except TypeError:
            print("node data must be an integer")
        temp = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        assert temp.next_node == None, 'this should be the last node in the list!'
        temp.next_node = new_node
        new_node.next_node = None
        return

    def insert_node_at(self, val: int, n: int):
        """ Insert a node after node n """
        count = 1
        temp = self.head
        new_node = Node(val)
        while temp is not None and count != n:
            temp = temp.next_node
            count += 1
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    def __str__(self):
        """ Print the elements of the list """
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))

    def find_node(self, node_value: int) -> Node:
        """ Find the value of a node in a Single linked list """
        temp = self.head
        while temp is not None:
            if temp.data == node_value:
                return temp.data
            else:
                temp = temp.next_node
        return f"The value {node_value} does not exists in this list"

    def delete_first_node(self):
        """ Delete the first node in a Single linked list """
        temp = self.head
        if temp.next_node is None:
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
        """ Delete the last node in a Singly Linked List"""
        temp = self.head
        if temp is not None:
            while temp.next_node.next_node is not None:
                 temp = temp.next_node
            temp.next_node = None
        return
    
    def delete_list(self):
        self.head = None
        return
    
    def list_size(self) -> int:
        """ Return the length of the list """
        temp = self.head
        count = 1
        if temp is not None:
            while temp.next_node is not None:
                temp = temp.next_node
                count += 1
        else:
            return 0
        return count
            

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_head(4)
    sll.insert_at_head(3)
    sll.insert_at_head(2)
    sll.insert_at_head(1)
    sll.insert_node_at(7, 3)
    print(sll)
    print("++++++++++++")
    # sll.delete_list()
    # print(sll)
    print(f"Size of the list: {sll.list_size()}")

