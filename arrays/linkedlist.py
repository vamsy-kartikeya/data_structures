class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def visualize(self):
        """Visualize the current state of the linked list."""
        if not self.head:
            print("Empty List: None")
            return
            
        current = self.head
        list_str = ""
        while current:
            list_str += f"{current.data} -> "
            current = current.next
        list_str += "None"
        print(list_str)
    
    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        print(f"\nInserting {data} at beginning...")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.visualize()
    
    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        print(f"\nInserting {data} at end...")
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.visualize()
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.visualize()
    
    def delete_node(self, key):
        """Delete the first occurrence of a node with the given key."""
        print(f"\nDeleting node with value {key}...")
        current = self.head
        
        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            self.visualize()
            return
            
        # Search for the key to be deleted
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                self.visualize()
                return
            current = current.next
            
        print(f"Value {key} not found in the list")
        self.visualize()
    
    def search(self, key):
        """Search for a node with the given key."""
        print(f"\nSearching for value {key}...")
        current = self.head
        position = 0
        
        while current:
            if current.data == key:
                print(f"Value {key} found at position {position}")
                return True
            current = current.next
            position += 1
            
        print(f"Value {key} not found in the list")
        return False
    
    def reverse(self):
        """Reverse the linked list."""
        print("\nReversing the linked list...")
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
        self.visualize()
    
    def get_length(self):
        """Get the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count 