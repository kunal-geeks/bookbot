with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
def count_letters(text):
    words = text.split()
    letters_count = {}
    for letter in range(97,123):
        letters_count[chr(letter)] = 0
    for word in words:
        for letter in word.lower():
            if letter in letters_count:
                letters_count[letter] += 1
    return letters_count

def print_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"The frankenstein book has a total of {count_words(file_contents)} words!\n")
    letters_count = count_letters(file_contents)
    for letter in letters_count:
        print(f"The '{letter}' character was found {letters_count[letter]} times")
    print("\n--- End report ---")

def main():
    print_report()
    
main()