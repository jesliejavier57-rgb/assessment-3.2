# ARRAY IMPLEMENTATION

array_data = []
letters = ['J', 'A', 'V', 'I', 'E', 'R']

print("===== ARRAY IMPLEMENTATION =====")

print("\nAdding letters to the Array:")
for letter in letters:
    array_data.append(letter)
    print(f"Inserted {letter}. Current Array: {array_data}")

print("\nRemoving letters from the Array (from index 0):")
while len(array_data) > 0:
    removed = array_data.pop(0)
    print(f"Deleted {removed}. Remaining Array: {array_data}")

print("Array is empty!")