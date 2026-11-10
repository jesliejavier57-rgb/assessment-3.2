# LINKED LIST IMPLEMENTATION

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_first(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        return None

    def display(self):
        elements = []
        current = self.head

        while current:
            elements.append(f"[{current.data}]")
            current = current.next

        return " -> ".join(elements) + " -> NULL"


letters = ['J', 'A', 'V', 'I', 'E', 'R']
my_list = LinkedList()

print("===== LINKED LIST IMPLEMENTATION =====")

print("\nAdding letters to the Linked List:")
for letter in letters:
    my_list.insert_end(letter)
    print(f"Inserted {letter} at the end.")

print("\nCurrent Linked List:")
print(my_list.display())

print("\nRemoving nodes from the Linked List:")
while my_list.head is not None:
    removed = my_list.delete_first()
    print(f"Deleted node with value {removed}.")

    if my_list.head:
        print("Current Linked List:", my_list.display())
    else:
        print("Linked List is empty!")