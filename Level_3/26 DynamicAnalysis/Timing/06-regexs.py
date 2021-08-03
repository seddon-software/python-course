from timeit import timeit


count = 100 * 1000

print("compiled regex  ", \
      timeit('result = pattern.search(text)', \
             'import re;' + \
             'text = "This line contains the numbers 8.73 and 4.67";' + \
             'numberPattern = r"\d+\.\d+";' + \
             'pattern = re.compile(numberPattern)', \
             number = count))

print("uncompiled regex", \
      timeit('result = re.search(numberPattern, text)', \
             'import re;' + \
             'text = "This line contains the numbers 8.73 and 4.67";' + \
             'numberPattern = r"\d+\.\d+";', \
             number = count))

