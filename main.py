from stats import getWordCount, getCharacterCount
import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    wordCount = getWordCount(text)
    dict = getCharacterCount(text)
    charList = list(dict)
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {wordCount} total words
--------- Character Count -------""")

    charList.sort(reverse=True, key=wrapperSortDict(dict))
    for c in charList:
        print(f"{c}: {dict[c]}")

    print('============= END ===============')


def wrapperSortDict(dict):
    def sortDict(c):
        return dict[c]
    return sortDict

def get_book_text(path):
    text = ''
    with open(path,'r') as f:
        text = f.read();
    return text;


main()
