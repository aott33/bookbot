import sys
from stats import get_num_words

def takeSecond(elem):
    return elem[1]

def textLetterCount(bookText):
    letters = {}
    lowerText = bookText.lower()
    letterReportList = []
    reportString = ""

    for char in lowerText:
        if char.isalpha() and char not in letters:
            letters[char] = 1
        elif char.isalpha() and char in letters:
            letters[char] += 1

    letterReportList = list(letters.items())
    letterReportList.sort(key=takeSecond, reverse=True)

    for item in letterReportList:
        reportString += f"{item[0]}: {item[1]}\n"

    return (reportString)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:
    book_path = sys.argv[1]
    with open(book_path) as f:
        fileContents = f.read()
        wordCountString = get_num_words(fileContents)
        letterCountString = textLetterCount(fileContents)
        print(f"--- Begin report of {book_path} ---")
        print(wordCountString + "\n")
        print(letterCountString)
        print("--- End report ---")
