from collections import deque

if __name__ == "__main__":
    fruits: deque[str] = deque(["apple", "orange", "banana"])
    fruits.append("tomato")
    fruits.appendleft("mango")
    print(fruits)

    print(fruits.pop())
    print(fruits.popleft())
    print(fruits)

    fruits.remove("apple")
    del fruits[0]
    print(fruits)

    fruits.pop()
