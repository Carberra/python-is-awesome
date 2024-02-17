from collections import deque
from random import choice

if __name__ == "__main__":
    components = ["A", "B", "X"]
    belt: deque[str] = deque((), maxlen=5)

    for _ in range(50):
        belt.append(choice(components))
        print(belt)
