# QUEUE IMPLEMENTATION (FIFO)

from collections import deque

queue = deque()
letters = ['J', 'A', 'V', 'I', 'E', 'R']

print("===== QUEUE IMPLEMENTATION (FIFO) =====")

print("\nEnqueuing letters into the Queue:")
for letter in letters:
    queue.append(letter)
    print(f"ENQUEUE {letter} | Front -> {list(queue)} <- Rear")

print("\nDequeuing letters from the Queue:")
while len(queue) > 0:
    dequeued = queue.popleft()

    remaining = list(queue) if queue else "Empty"
    print(f"DEQUEUE {dequeued} | Remaining Queue: {remaining}")

print("\nQueue is empty!")