from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
input1 = open("out/python_tutorial.13.pdf", "rb")
input2 = open("out/python_tutorial.14.pdf", "rb")
input3 = open("out/python_tutorial.15.pdf", "rb")
input4 = open("out/python_tutorial.16.pdf", "rb")
input5 = open("out/python_tutorial.17.pdf", "rb")
input6 = open("out/python_tutorial.18.pdf", "rb")
input7 = open("out/python_tutorial.19.pdf", "rb")

# add pages to start of output
merger.append(fileobj = input1, pages = (0,1))
merger.append(fileobj = input2, pages = (0,1))
merger.append(fileobj = input5, pages = (0,1))
merger.append(fileobj = input6, pages = (0,1))

# add pages to middle of output
merger.merge(position = 2, fileobj = input3, pages = (0,1))
merger.merge(position = 3, fileobj = input4, pages = (0,1))

# add pages to end of output
merger.append(input7)

# Write to an output PDF document
output = open("pdfs/python_tutorial-merged.pdf", "wb")
merger.write(output)
