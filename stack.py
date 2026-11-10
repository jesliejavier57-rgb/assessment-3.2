# STACK IMPLEMENTATION (LIFO)

stack = []

letters = ['J', 'A', 'V', 'I', 'E', 'R']

print("===== STACK IMPLEMENTATION (LIFO) =====")

# PUSH operation
print("\nPUSH: Adding elements")
for letter in letters:
    stack.append(letter)
    print(f"PUSH {letter} | Stack: {stack}")

print("\nTOP ->", " -> ".join(reversed(stack)), "-> BOTTOM")

# POP operation
print("\nPOP: Removing elements")

while len(stack) > 0:
    removed = stack.pop()
    print("Removed:", removed)
    print("Stack:", stack)

print("\nStack is empty!")