import os
import string
from collections import Counter


def create_sample_file():
    text = input("Enter text to create sample.txt: ")
    with open("sample.txt", "w") as file:
        file.write(text)
    print("sample.txt created successfully!\n")


def read_file():
    if not os.path.exists("sample.txt"):
        print("sample.txt not found.")
        create_sample_file()
    with open("sample.txt", "r") as file:
        return file.read()


def count_word_frequency(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return Counter(words)


def display_top_words(word_counts, top_n):
    total_words = sum(word_counts.values())
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")
    return total_words


def save_report(word_counts, total_words, top_n):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")
    print("word_count_report.txt saved successfully!\n")


def main():
    text = read_file()
    word_counts = count_word_frequency(text)

    top_n = int(input("Enter number of top common words to display: "))
    total_words = display_top_words(word_counts, top_n)
    save_report(word_counts, total_words, top_n)


if __name__ == "__main__":
    main()
