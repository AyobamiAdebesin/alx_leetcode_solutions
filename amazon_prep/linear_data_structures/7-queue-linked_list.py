#!/usr/bin/python3
""" Queue Data Structure """


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



if __name__ == "__main__":
    queue = Queue()
    print(f"Before enqueue: is queue empty? {queue.isEmpty()}")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"After enqueue: is queue empty? {queue.isEmpty()}")
    print(queue)
    for i in range(5):
        queue.rotate()
        print(queue)

    