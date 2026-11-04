class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"append('{data}') -> Current stack: {self.stack}")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"pop() removes {removed} -> Remaining stack: {self.stack if self.stack else '[] \"(Empty)\"'}")
            return removed
        return None

    def is_empty(self):
        return len(self.stack) == 0

def main():
    print("\n4. STACK DATA STRUCTURE (LIFO)")
    s = Stack()
    letters = ['R', 'O', 'S', 'A', 'L', 'I', 'T', 'A']

    print("\n|=== APPEND() / PUSH (ADDING) ===|")
    for letter in letters:
        s.push(letter)

    print("\n|=== POP() (REMOVING FROM TOP) ===|")
    while not s.is_empty():
        s.pop()

if __name__ == "__main__":
    main()