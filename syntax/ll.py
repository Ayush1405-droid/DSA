class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = node(1)           #Create a node with data 1
head.next = node(2)      #Create a node with data 2 and link it to the first node
head.data                #Access the data of the first node
