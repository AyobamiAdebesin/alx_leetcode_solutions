#!/usr/bin/python3

class Queue:
    def __init__(self, max_size):
        """ Initialize queue attributes """
        self.__size = max_size
        self.__items = self.__size * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.__items]
        return ' '.join(values)

    def isFull(self):
        """ Check if the queue is full """
        return (self.start == 0 and self.top + 1 == self.__size) or (self.top + 1 == self.start)
    
    def isEmpty(self):
        """ Check if queue is empty """
        return self.top == -1 and self.start == -1
    
    def enqueue(self, val: int):
        """ Add an element to the end of the queue """
        if not self.isFull():
            if self.top + 1 == self.__size:
                self.top == 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.__items[self.top] = val
        else:
            return "queue is full"
    
    def dequeue(self):
        """ Remove an element at the front of the queue """
        if self.isEmpty():
            return "queue is element!"
        else:
            first_elem = self.__items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == self.__size:
                self.start = 0
            else:
                self.start += 1
            self.__items[start] = None
            return first_elem
    
    def peek(self):
        """ Peek at the first element in the queue """
        if not self.isEmpty():
            return self.__items[self.start]
        return "queue is empty"
    
    def delete(self):
        self.__items = self.__size * [None]
        self.start = -1
        self.top = -1
    


if __name__ == "__main__":
    queue = Queue(6)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.dequeue()
    queue.enqueue(12)
    print(queue)