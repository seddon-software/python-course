############################################################
#
#    random access
#
############################################################

myFile = open('data/myfile2.bin', 'w')

myFile.seek(40, 0)
myFile.write("ABCDEFGH")

myFile.seek(140, 0)
myFile.write("ABCDEFGH")

myFile.seek(240, 0)
myFile.write("ABCDEFGH")

myFile.seek(2560240, 0)
myFile.write("X")

myFile.close()

