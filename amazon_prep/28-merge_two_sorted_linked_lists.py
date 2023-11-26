#!/usr/bin/python3
""" Given 2 sorted linked lists, merge them together; sorted"""


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
    def __init__(self):
        self.head : Node = None

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

    def __str__(self):
        """ Print the elements of the list """
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('->'.join(values))


def mergeLists(head1: Node, head2: Node):
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data < head2.data:
            current.next_node = head1
            head1 = head1.next_node
        else:
            current.next_node = head2
            head2 = head2.next_node
        current = current.next_node

    if head1:
        current.next_node = head1
    elif head2:
        current.next_node = head2
    
    return dummy.next_node
    # temp1 = head1
    # temp2 = head2
    # if temp1 is None:
    #     return temp2
    # if temp2 is None:
    #     return temp1
    
    # while temp1 and temp2:
    #     if temp1.data <= temp2.data:
    #         temp1

    # while temp2.data <= temp1.data <= temp1.next_node.data:
    #     if temp1.next is None:
    #         temp1.next = temp2
    #         temp2.next = None
    #     else:
    #         temp2.next = temp1.next
    #         temp1.next = temp2
    #     temp1 = temp1.next
    # return temp1


if __name__ == "__main__":
    sll = SinglyLinkedList()
    print(sll.head)
    # sll_1 = SinglyLinkedList()
    # sll_1.insert_at_head(3)
    # sll_1.insert_at_head(2)
    # sll_1.insert_at_head(1)
    # print(sll_1)
    # sll_2 = SinglyLinkedList()
    # sll_2.insert_at_head(6)
    # sll_2.insert_at_head(5)
    # sll_2.insert_at_head(4)
    # print(sll_2)
    # new_head = mergeLists(sll_1.head, sll_2.head)
    # new_list = SinglyLinkedList()
    # new_list.head = new_head
    # print(new_list)