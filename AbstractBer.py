import os, sys
import tempfile
import win32print
import json
import random
#p = win32print.OpenPrinter (printer_name)


def getRandomPoem():
    size = len(data)
    r = random.randint(0, size-1)
    print(data[r]['titleEN'], "/", data[r]['titleKZ'],  "\n")
    print(data[r]['textEN'], "\n\n")


with open('poems.json', mode="r", encoding="utf-8") as f:
    data = json.load(f)

for i in range(len(data)):
    print(i+1, ":", len(data[i]['textRU']) - len(data[i]['textKZ']))


#getRandomPoem()


filename = tempfile.mktemp (".txt")
open (filename, "w").write ("This is a test")

p = win32print.OpenPrinter("OneNote")

job = win32print.StartDocPrinter (p, 1, ("test of raw data", None, "RAW"))
win32print.StartPagePrinter(p)
win32print.WritePrinter(p, "data to print")
win32print.EndPagePrinter(p)

os.startfile("C:/Users/TestFile.txt", "print")
