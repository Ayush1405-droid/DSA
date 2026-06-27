#One-line interview answer: “A singly linked list is a dynamic linear data structure in which each node stores data and a pointer to the next node, allowing efficient insertions and deletions without contiguous memory allocation.”

class Node:
    def __init__(self , val , next=None) :
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

Head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

Head.next = A
A.next = B
B.next = C

#Traverse

curr = Head

while curr:
    print(curr)
    curr = curr.next
print(Head)    

#Dispalay

def display(Head):
    curr = Head
    element = []

    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(element))
display(Head)        

#search for node value
def search(head,val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False   


print(search(Head, 10))