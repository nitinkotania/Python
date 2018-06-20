class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

    def insert_data(self,data):
        new_node =  Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_ll(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
  
    def insert_end(self,data):
	if not self.head:
		self.head = Node(data)
		return 
	
	curr = self.head
	while curr.next:
		curr = curr.next
	curr.next = Node(data)


ll = Linked_list()

for i in range(5):
    ll.insert_data(i)

ll.print_ll()

ll.insert_end(55)
ll.print_ll()
