def textWordCount(bookText):
    wordCount = bookText.split()
    return (f"{len(wordCount)} words found in the document")

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
        reportString += f"The '{item[0]}' character was found {item[1]} times\n"

    return (reportString)

with open("books/frankenstein.txt") as f:
    fileContents = f.read()
    wordCountString = textWordCount(fileContents)
    letterCountString = textLetterCount(fileContents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(wordCountString + "\n")
    print(letterCountString)
    print("--- End report ---")