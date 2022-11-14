from PyPDF4 import PdfFileMerger
import os, regex as re

BASE = "/home/chris/temp"
os.chdir(BASE)
files = os.listdir(BASE)
files.sort()
years = ["2019", "2020", "2021", "2022"]
#years = ["20"]

for year in years:
    merger = PdfFileMerger(strict=False)
    thisYearsFiles = [file for file in files if re.match(rf'^{year}.*', file)]
    print(thisYearsFiles)
    for file in thisYearsFiles:
        print(f"\t{file}")
        merger.append(fileobj=open(file, 'rb'))
    merger.write(fileobj=open(f"{year}.pdf", 'wb'))
    merger.close()
