from collections import defaultdict

word_mapping: dict[str, int] = defaultdict(int)

if __name__ == "__main__":
    with open("lyrics.txt") as f:
        for line in f:
            for word in line.lower().split():
                word_mapping[word] += 1

    for word, count in word_mapping.items():
        print(f"{word}: {count}")
