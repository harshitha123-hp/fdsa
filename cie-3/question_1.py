class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node  
        else:
            temp = self.head
            
            while temp.next != self.head:
                temp = temp.next
            
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node  # Update head to new node

    def delete_node(self, data):
        if not self.head:
            print("List is empty.")
            return
        
        curr = self.head
        prev = None

        while True:
            if curr.data == data:  # Found the node to delete
                if curr == self.head: 
                    #  one node in the list
                    if curr.next == self.head:
                        self.head = None
                    else:
                        temp = self.head

                        while temp.next != self.head:
                            temp = temp.next
                        self.head = self.head.next  
                        temp.next = self.head  
                else:  
                    prev.next = curr.next  
                print(f"Node with data {data} deleted.")
                return

            prev = curr
            curr = curr.next

            if curr == self.head: 
                break

        print(f"Node with data {data} not found.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


cll = CircularLinkedList()

# Insert nodes
print("Inserting nodes at the beginning:")
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)
cll.display() 


print("\nDeleting node with data 20:")
cll.delete_node(20)
cll.display()  


print("\nAttempting to delete node with data 40:")
cll.delete_node(40)
cll.display() 


print("\nDeleting head node with data 30:")
cll.delete_node(30)
cll.display()  
