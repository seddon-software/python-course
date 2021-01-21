import pprint as pp

string = "supercalafragilisticexpialidocious"
dictionary = {char:string.count(char) for char in string}
print(dictionary)
pp.pprint(dictionary)


