import re
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime
import subprocess
import os

def main():
    os.chdir("/home/chris/home/_Companies/CRS Accounts/Internet Bills/Downloads")

    response = subprocess.run('ls *.pdf', capture_output=True, universal_newlines=True, shell = True)
    fileNames = response.stdout.split()

    for oldFile in fileNames:
        newFile = getNewFileName(oldFile)
        cmd = f"mv {oldFile} {newFile}"
        os.system(cmd)

def getNewFileName(fileName):
    pdf = PdfFileReader(open(fileName, "rb"))
    text = ""
    for page in pdf.pages:
        text += page.extractText()
        for line in text.splitlines():
            if re.search('Bill Reference',  line):
                date = re.search('[(](.*)[^(]', line).group(1)
                # strip off unwanted parts of date
                date = date.replace('th', '')
                date = date.replace('st', '')
                date = date.replace('nd', '')
                date = date.replace('rd', '')
                date = date.replace('.', '')

                # is it a full month or abbreviation
                try:
                    date = datetime.strptime(date, "%d %B %Y")  # full
                except:
                    date = datetime.strptime(date, "%d %b %Y")  # abbreviation

                newFile = f"{date:%Y-%m-%d}.pdf"
                return f"{newFile}"

main()

