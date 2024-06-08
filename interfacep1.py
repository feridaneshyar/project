from p1 import Stack,Queue,linklist
linked_list = linklist()
stack = Stack()
queue = Queue()

while True:
    print("\nChoose an operation:")
    print("1. Create Linked List")
    print("2. Delete Prime Numbers from Linked List")
    print("3. Print Linked List")
    print("4. Stack Operations")
    print("5. Queue Operations")
    print("6. Merge Sort Linked Lists")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Enter elements for Linked List (comma-separated):")
        elements = list(map(int, input().split(',')))
        linked_list = linklist()
        for item in elements:
            linked_list.insert(item)
        print('created.')
    elif choice == '2':
        linked_list.deleteprime()
        print("Prime numbers deleted from the linked list.")
    elif choice == '3':
        print("Linked List:")
        linked_list.printList()
    elif choice == '4':
        while True:
            print("\nStack Operations:")
            print("1. Push into Stack")
            print("2. Pop from Stack")
            print("3. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                value = int(input("Enter the value to push into the stack: "))
                stack.push(value)
            elif choice == '2':
                popped_value = stack.pop()
                if popped_value is not None:
                    print("Popped value from stack:", popped_value)
                else:
                    print("Stack is empty.")
            elif choice == '3':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please enter again.")

    elif choice == '5':
        while True:
            print("\nQueue Operations:")
            print("1. Add Item into Queue")
            print("2. Delete Item from Queue")
            print("3. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                value = int(input("Enter the value to add into the queue: "))
                queue.addItem(value)
            elif choice == '2':
                deleted_item = queue.deleteItem()
                if deleted_item is not None:
                    print("Deleted item from queue:", deleted_item)
                else:
                    print("Queue is empty.")
            elif choice == '3':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please enter again.")
    elif choice == '6':
        print("Enter elements for Linked List 1 (comma-separated):")
        elements_1 = list(map(int, input().split(',')))
        linked_list_1 = linklist()
        for item in elements_1:
            linked_list_1.insert(item)
        
        print("Enter elements for Linked List 2 (comma-separated):")
        elements_2 = list(map(int, input().split(',')))
        linked_list_2 = linklist()
        for item in elements_2:
            linked_list_2.insert(item)
        
        print("Linked List 1:")
        linked_list_1.printList()
        print("Linked List 2:")
        linked_list_2.printList()
        linked_list.mergeSort(linked_list_1, linked_list_2)
        print("Merged sorted linked list:")
        linked_list.printList()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter again.")


