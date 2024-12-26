from collections import defaultdict

def countChar(text):
    count = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            count[char] += 1
    return count

def main(book):
    print(f"--- Begin report of {book} ---")
    with open(book) as f:
        text = f.read()
        print(f"{len(text.split())} words found in the document")
        print()
        count = list(countChar(text).items())
        count.sort(reverse=True, key=lambda x: x[1])
        for char, num in count:
            print(f"The '{char}' character was found {num} times")
    print("--- End report ---")

main("books/frankenstein.txt")