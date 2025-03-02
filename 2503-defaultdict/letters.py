from collections import defaultdict

word_mapping: dict[str, set[str]] = defaultdict(set)

if __name__ == "__main__":
    with open("lyrics.txt") as f:
        for line in f:
            for word in line.lower().split():
                word_mapping[word[0]].add(word)

    for letter, words in word_mapping.items():
        print(f"{letter}: {', '.join(words)}")
