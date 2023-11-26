#!/usr/bin/python3
from collections import deque
from multiprocessing import Queue
import queue

custom_queue = queue.Queue(maxsize=3)
Queue(maxsize=5)

new_queue = deque(maxlen=3)
new_queue.append(1)
new_queue.append(2)
new_queue.append(3)
new_queue.popleft()
new_queue.append(4)
print(new_queue)
