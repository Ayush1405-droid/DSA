from collections import deque

q = deque() #create an empty queue
q.append(1) #enqueue an element to the queue
q.append(2) #enqueue another element to the queue
q.popleft() #dequeue the front element from the queue
q[0] #front
len(q) #size
