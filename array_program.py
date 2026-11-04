def main():
    print("\n1. ARRAY DATA STRUCTURE ")
    name_letters = ['R', 'O', 'S', 'A', 'L', 'I', 'T', 'A']
    arr = []

    print("\n|=== INSERTION / ADD PHASE ===|")
    for item in name_letters:
        arr.append(item)
        print(f"Added '{item}': {arr}")

    print(f"\nFinal Array State: {arr}")
    print(f"Indices: {[i for i in range(len(arr))]}")

    print("\n|=== DELETION / REMOVE PHASE ===|")
    while len(arr) > 0:
        index_removed = len(arr) - 1
        removed = arr.pop()
        print(f"Remove index {index_removed} -> {arr if arr else '[] (Empty)'}")


if __name__ == "__main__":
    main()