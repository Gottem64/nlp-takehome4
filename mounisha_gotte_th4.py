import nltk
from nltk.corpus import gutenberg
from string import punctuation
import matplotlib.pyplot as plt
from collections import Counter
import re
import requests

# free e-book titled "Don Quixote", written by Miguel de Cervantes
the_don_quixote = 'https://www.gutenberg.org/files/996/996-0.txt'


def get_book(url):
    # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Discards the metadata from the beginning of the book
    start = re.search(r"I: ABOUT THIS TRANSLATION", raw).end()
    # Discards the text starting Part 2 of the book
    stop = re.search(r"End of the Project Gutenberg EBook of The History of Don Quixote, by Miguel de Cervantes",
                     raw).start()
    print(start)
    print(stop)
    # Keeps the relevant text
    text = raw[start:stop]
    return text


def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+', ' ', sentence).lower()


book = get_book(the_don_quixote)
processed_book = preprocess(book)


def frequent_no(processed_book):
    arr = re.findall(r'[0-9]+', processed_book)
    max_freq = 0
    ele = 0
    count = Counter(arr)
    for i in list(count.keys()):
        if count[i] >= max_freq:
            max_freq = count[i]
            ele = int(i)
    return ele

outputFile = open("results.txt", "w")
# Find the number of the verbs "is" in the corpus.
outputFile.write("1. Number of is verbs: " + str(len(re.findall(r'is', processed_book))))
# regex = r"\b(?:123|234|345|456|567|678|789)\b"
# instances = re.findall(r"^\d{1,3}(?:,\d{3})*$", processed_book)
outputFile.write("\n2. Number of continuous number sequences: " + str(re.findall(r"(?<!\d)(?:123|234|345|456|567|678"
                                                                                 r"|789)(?!\d)", processed_book)))

index = processed_book.find(' 23')
print(index)

context = processed_book[index-200:index+100]
print(context)

outputFile.write("\n4. The number is used to tell the day of the month.")

outputFile.write("\n5. It is an important day because on the 23rd of april 1616 England lost Shakespeare .")


outputFile.close()

