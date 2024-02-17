from collections import deque

if __name__ == "__main__":
    fruits = deque(["mango", "apple", "orange", "banana"])
    print(fruits[2])

    fruits.rotate(-2)
    print(fruits.popleft())
    fruits.rotate(2)
    print(fruits)
