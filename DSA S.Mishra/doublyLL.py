#One-line interview answer: “A doubly linked list is a bidirectional linked data structure where each node stores data along with pointers to both the next and previous nodes, enabling efficient traversal and updates in either direction.”


class Node:
    def __init__(self , val , next = None , prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)  

head = tail = Node(1)
print(tail)      

#Display

def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(element))    

display(head)  

#insert at the beginneung - O(1)

def insert_at_the_beginning(head, tail, val):
    new_node = Node(val, next=head)
    head.prev = new_node
    return new_node, tail
head, tail = insert_at_the_beginning(head, tail, 3)
display(head)

