from bs4 import BeautifulSoup
import requests
import urllib
import argparse

count = 1
inputFile = "doi.txt"
outputFile = "output.txt"
praser = argparse.ArgumentParser()
praser.add_argument(
    "-i", "--input", help="name of input file")
praser.add_argument(
    "-c", "--count", help="start count for citations")
praser.add_argument(
    "-o", "--output", help="name of output file")
args = praser.parse_args()
if args.input:
    inputFile = args.input
if args.count:
    count = int(args.count)
if args.output:
    outputFile = args.output

print("Starting")
with open(outputFile, "a") as outFile:
    outFile.write("---CITATIONS---\n")
    with open(inputFile, "r") as inFile:
        for line in inFile:
            doi = line
            url = "https://citation.crosscite.org/format"
            payload = {'doi': doi, 'style': 'apa', 'lang': 'en-US'}
            raw = requests.get(url, params=payload)
            output = raw.text.encode("ascii", 'ignore')
            outFile.write("[{}] ".format(count))
            outFile.write(str(output)[2:-3])
            outFile.write("\n")
            count += 1
            print('.', end='')
    outFile.write("---END---\n")
print("\nFinished")
