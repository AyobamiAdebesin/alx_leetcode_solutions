#!/usr/bin/python3
""" Queue Data Structure with no size limit - Python List """


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, val: int):
        """ Adds an element to the end of the list """
        if not isinstance(val, int):
            print("value must be an integer!")
            return
        self.__items.append(val)

    def __str__(self):
        values = [str(x) for x in self.__items]
        return '->'.join(values)

    def isEmpty(self):
        """ Check if Queue is empty """
        return len(self.__items) == 0

    def dequeue(self):
        """ Remove an element in the front of the list """
        if not self.isEmpty:
            return self.__items.pop(0)
        else:
            return "queue is empty!"

    def peek(self):
        """ Peek at the first element of the list """
        if not self.isEmpty():
            return self.__items[0]
        return None

    def delete(self):
        """ Delete the entire queue """
        self.__items = None


if __name__ == "__main__":
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue(4)
    queue.enqueue(3)
    print(queue)
