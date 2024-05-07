def read_book():
   with open("./books/frankenstein.txt") as f:
        return f.read()

def get_word_count(book):
    return len(book.split())

def sort_on(dict):
    return dict["count"]

def get_letter_counts(book):
    letter_counts = []
    letter_dict = {}
    raw_book = book.lower()
    for char in raw_book:
        if(char in letter_dict):
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
        
    for char, count in letter_dict.items():
        if(char.isalpha()):
            letter_counts.append({"char": char, "count": count})

    letter_counts.sort(reverse=True, key=sort_on)

    return letter_counts

def generate_report(word_count, letter_counts):
    print("===== Begin report of books/frankenstein.txt =====")
    print(word_count, "words found in the document")
    for letter in letter_counts:
        print("The", letter['char'], "character was found", letter['count'], "times")
    print("===== End Report =====")

def main():
    book = read_book()
    word_count = get_word_count(book)
    letter_counts = get_letter_counts(book)
    generate_report(word_count, letter_counts)

main()

