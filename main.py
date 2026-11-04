import array_program
import singly_linked_list
import doubly_linked_list
import stack
import queue


def main():
    while True:
        print("\n|================================================|")
        print("|   ASSESSMENT 3.2: LINEAR DATA STRUCTURES       |")
        print("|           Surname: ROSALITA                    |")
        print("|================================================|")
        print("|1. Array Program                                |")
        print("|2. Singly Linked List Program                   |")
        print("|3. Doubly Linked List Program                   |")
        print("|4. Stack Program (LIFO)                         |")
        print("|5. Queue Program (FIFO)                         |")
        print("|6. Exit / Quit                                  |")
        print("|================================================|")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            print("\n")
            array_program.main()
        elif choice == '2':
            print("\n")
            singly_linked_list.main()
        elif choice == '3':
            print("\n")
            doubly_linked_list.main()
        elif choice == '4':
            print("\n")
            stack.main()
        elif choice == '5':
            print("\n")
            queue.main()
        elif choice == '6':
            print("\nThank you! Exiting program.")
            break
        else:
            print("\nInvalid choice! Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()