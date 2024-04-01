import difflib
import re
import os

def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r') as file:
        return set(word.strip().lower() for word in file)

def spell_check(text_file, dictionary):
    with open(text_file, 'r') as file:
        lines = file.readlines()

    for line_num, line in enumerate(lines):
        words = re.findall(r'\b\w{2,}\b', line.lower())  # match words with at least 2 characters
        for match in re.finditer(r'\b\w{2,}\b', line.lower()):
            word = match.group()
            col_num = match.start()  # Column number of the word
            if word not in dictionary:
                suggestions = difflib.get_close_matches(word, dictionary, n=3)  # Get three suggestions
                highlighted_line = line[:col_num] + '\033[1;31;40m' + word + '\033[0m' + line[col_num + len(word):]
                print(f"Misspelled word '{word}' at line {line_num + 1}, column {col_num + 1}:\n{highlighted_line.strip()}")
                if suggestions:
                    print("\nSuggestions:")
                    for suggestion in suggestions:
                        print(f"- {suggestion}")
                else:
                    print("No suggestions found.")
                print()

def is_file_empty(file_path):
    return os.stat(file_path).st_size == 0

if __name__ == "__main__":
    dictionary_file = "dictionary.txt"
    text_file = "text_to_check.txt"

    if os.path.exists(text_file):
        if not is_file_empty(text_file):
            dictionary = load_dictionary(dictionary_file)
            spell_check(text_file, dictionary)
        else:
            print("Text file is empty. Exiting without spell-checking.")
    else:
        print("Text file does not exist.")
