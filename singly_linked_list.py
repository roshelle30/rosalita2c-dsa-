class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_front(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def display(self):
        if not self.head:
            return "none (Empty)"
        elems = []
        current = self.head
        while current:
            elems.append(f"[{current.data}]")
            current = current.next
        return " -> ".join(elems) + " -> none"


def main():
    print("\n2. SINGLY LINKED LIST\n")
    sll = SinglyLinkedList()
    letters = ['R', 'O', 'S', 'A', 'L', 'I', 'T', 'A']

    print("|=== INSERTION (ADDING) ===|")
    for letter in letters:
        sll.insert(letter)
        print(f"Head -> {sll.display()}")

    print("\n|=== DELETION (REMOVING FROM FRONT) ===|")
    print(f"Head -> {sll.display()}")
    while sll.head.next:
        sll.delete_front()
        print(f"Head -> {sll.display()}")
    sll.delete_front()
    print("Head -> none (Empty)")


if __name__ == "__main__":
    main()