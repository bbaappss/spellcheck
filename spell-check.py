import difflib
import re

def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r') as file:
        return set(word.strip().lower() for word in file)

def spell_check(text_file, dictionary):
    with open(text_file, 'r') as file:
        lines = file.readlines()

    for line_num, line in enumerate(lines):
        words = re.findall(r'\b\w{2,}\b', line.lower())  # Adjusted regex to match words with 2 or more characters
        for word in words:
            if word not in dictionary:
                suggestion = difflib.get_close_matches(word, dictionary, n=1)
                print(f"Misspelled word '{word}' at line {line_num + 1}: {line.strip()}")
                if suggestion:
                    print(f"Suggestion: {suggestion[0]}")
                else:
                    print("No suggestion found.")
                print()

if __name__ == "__main__":
    dictionary_file = "dictionary.txt"  # Your dictionary file
    text_file = "text_to_check.txt"  # Your text file to check
    dictionary = load_dictionary(dictionary_file)
    spell_check(text_file, dictionary)
