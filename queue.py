from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)
        print(f"[Front] {' -> '.join(self.queue)} [Back]")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.popleft()
            remaining = list(self.queue)
            print(f"popleft() removes {removed} -> Remaining {remaining if remaining else '[] \"(Empty)\"'}")
            return removed
        return None

    def is_empty(self):
        return len(self.queue) == 0

def main():
    print("\n5. QUEUE DATA STRUCTURE (FIFO)")
    q = Queue()
    letters = ['R', 'O', 'S', 'A', 'L', 'I', 'T', 'A']

    print("\n|=== APPEND() (ADDING TO BACK) ===|")
    for letter in letters:
        q.enqueue(letter)

    print("\n|=== POPLEFT() (REMOVING FROM FRONT) ===|")
    while not q.is_empty():
        q.dequeue()

if __name__ == "__main__":
    main()