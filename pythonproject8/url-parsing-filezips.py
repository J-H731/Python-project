# downloading, importing, extracting, sorting, and some xlsx magic

import urllib.request

urlOfFileName = "http://www.nseindia.com/content/historical/EQUITIES/2015/JUL/cm17JUL2015bhav.csv.zip"

localZipFilePath = "C:\Users\jacin\OneDrive\Documents\(7) GitHub\Python project\pythonproject8/cm17JUL2015bhav2.csv.zip"

hdr = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
       'Accept-Charset':'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
       'Accept-Encoding':'none',
       'Accept-Language':'en-US,en;q=0.8',
       'Connection':'keep-alive'
      }

webRequest = urllib.request.Request(urlOfFileName,headers=hdr)

try:
    page = urllib.request.urlopen(webRequest)
    content = page.read()
    output = open(localZipFilePath,"wb")
    output.write(bytearray(content))
    output.close()
except(urllib.request.HTTPError, e):
    print(e.fp.read())
    print("Looks like the file download did not go through, for url = ",urlOfFileName)

import zipfile, os

localExtractFilePath = "C:\Users\jacin\OneDrive\Documents\(7) GitHub\Python project\pythonproject8/"

if os.path.exists(localZipFilePath):
    print("Cool!" + localZipFilePath + " exists..proceeding")
    listOfFiles = []
    fh = open(localZipFilePath,'rb')
    zipFileHandler = zipfile.ZipFile(fh)
    for filename in zipFileHandler.namelist():
        zipFileHandler.extract(filename,localExtractFilePath)
        listOfFiles.append(localExtractFilePath + filename)
        print("Extracted " + filename + " from the zip file to " + (localExtractFilePath + filename))
    print("In total, we extracted ", str(len(listOfFiles)), " files")
    fh.close()

import csv

oneFileName = listOfFiles[0]

lineNum = 0

listOfLists = []

with open(oneFileName,'r') as csvfile:
    lineReader = csv.reader(csvfile,delimiter=",",quotechar="\"")
    for row in lineReader:
        lineNum = lineNum + 1
        if lineNum == 1:
            print("Skipping the header row")
            continue
        symbol = row[0]
        close = row[5]
        prevClose = row[7]
        tradedQty = row[9]
        pctChange = float(close)/float(prevClose) - 1
        oneResultRow = [symbol,pctChange,float(tradedQty)]
        listOfLists.append(oneResultRow)
        print(symbol, "{:,.1f}".format(float(tradedQty)/1e6) + "M INR", "{:,.1f}".format(pctChange*100)+"%")
    print("Done iterating over the file contents - the file is closed now!")
    print("We have stock info for " + str(len(listOfLists)) + " stocks")


listOfListsSortedByQty = sorted(listOfLists, key=lambda x:x[2], reverse=True)

listOfListsSortedByQty = sorted(listOfLists, key=lambda x: x[1], reverse=True)

import xlsxwriter

excelFileName = "C:\Users\jacin\OneDrive\Documents\(7) GitHub\Python project\pythonproject8/cm17JUL2015bhav.xlsx"

workbook = xlsxwriter.Workbook(excelFileName)

worksheet = workbook.add_worksheet("Summary")

worksheet.write_row("A1",["Top Traded Stocks"])
worksheet.write_row("A2",["Stock","% Change","Value Traded (INR)"])

for rowNum in range(5):
    oneRowToWrite = listOfListsSortedByQty[rowNum]
    worksheet.write_row("A" + str(rowNum + 3), oneRowToWrite)
workbook.close()
