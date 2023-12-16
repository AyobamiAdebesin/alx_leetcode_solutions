#!/usr/bin/python3

class HashMap:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.buckets = [None] * capacity
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.buckets[index]):
                if existing_key == key:
                    self.buckets[index][i]