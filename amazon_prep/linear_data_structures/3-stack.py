#!/usr/bin/python3
""" Stack using list without size limit """
import copy

class Stack:
    def __init__(self):
        self.__list = []
    
    def __str__(self):
        """ Print the stack """
        list_copy = copy.deepcopy(self.__list)
        list_copy.reverse()
        values = [str(x) for x in list_copy]
        return '\n==\n'.join(values)

    def isEmpty(self):
        """ Check if a stack is empty """
        return self.__list == []
    
    def push(self, value: int):
        """ Push a method to the stack """
        self.__list.append(value)
    
    def pop(self):
        """ Pop an element from a stack """
        if not self.isEmpty():
            return self.__list.pop()
        else:
            return "Empty stack!"
    
    def peek(self):
        """ Peek at the top most element in a stack """
        if not self.isEmpty():
            return self.__list[len(self.__list)-1]
        else:
            return "Empty stack"



if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack)
    print(stack.peek())