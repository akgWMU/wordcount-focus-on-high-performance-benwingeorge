import re
from collections import defaultdict
import matplotlib.pyplot as plt
import os

class WordCounter:
    def __init__(self):
        self.word_map = defaultdict(int)

    def insert(self, word):
        word = word.lower()
        self.word_map[word] += 1

    def load_file_line_buffered(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:

            for line in file:  # buffered iteration (doesn't load the whole file)
                words = re.findall(r"\b[a-zA-Z]+\b", line)
                for word in words:
                    self.insert(word)

    def load_file_custom_buffer(self, file_path, buffer_size=1024):
        with open(file_path, "r", encoding="utf-8", buffering=buffer_size) as file:
            for line in file:
                words = re.findall(r"\b[a-zA-Z]+\b", line)
                for word in words:
                    self.insert(word)

    def load_file_char_by_char(self, file_path):
        # Character by character reading (very slow)
        current_word = ""
        with open(file_path, "r", encoding="utf-8", buffering=1) as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                
                if char.isalpha():
                    current_word += char
                else:
                    if current_word:
                        self.insert(current_word)
                        current_word = ""
            
            # Handle final word
            if current_word:
                self.insert(current_word)

    def load_files(self, file_list):
        for file_path in file_list:
            self.load_file_line_buffered(file_path)

    def display_sorted(self):
        sorted_words = sorted(self.word_map.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_words:
            print(f"{word}: {count}")

    def plot_top_words(self, top_n=50):
        sorted_words = sorted(self.word_map.items(), key=lambda x: x[1], reverse=True)[:top_n]
        # print("sorted_words: ", sorted_words)
        words, counts = zip(*sorted_words)
        plt.figure(figsize=(12,6))
        plt.bar(words, counts)
        plt.xticks(rotation=90)
        plt.title(f"Top {top_n} Words")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.show()

if __name__ == "__main__":
    wc = WordCounter()
    directory = "test_files"
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")]
    wc.load_files(files)
    wc.display_sorted()
    wc.plot_top_words(50)
