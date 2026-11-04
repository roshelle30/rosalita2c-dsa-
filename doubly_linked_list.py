class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete_front(self):
        if not self.head:
            return None
        removed_data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_data

    def display(self):
        if not self.head:
            return "none (Empty)"
        elems = []
        current = self.head
        while current:
            elems.append(f"[{current.data}]")
            current = current.next
        return " <=> ".join(elems) + " -> none"

def main():
    print("\n3. DOUBLY LINKED LIST")
    dll = DoublyLinkedList()
    letters = ['R', 'O', 'S', 'A', 'L', 'I', 'T', 'A']

    print("\n|=== INSERTION (ADDING) ===|")
    for letter in letters:
        dll.insert(letter)
        print(f"Head -> {dll.display()}")

    print("\n|=== DELETION (BREAKING CHAIN FROM FRONT) ===|")
    while dll.head:
        dll.delete_front()
        print(f"Head -> {dll.display()}")

if __name__ == "__main__":
    main()