class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append_node(10)
    sll.append_node(20)
    sll.append_node(30)
    
    sll.display_list()
    
    print("Search 20:", sll.search_node(20))  # True
    print("Search 40:", sll.search_node(40))  # False
