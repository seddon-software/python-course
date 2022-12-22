from timeit import timeit

count = 10 * 1000 * 1000
format = "%16s%8.3f %s"

print("***** string concatenation *****")
print()

statement = "s += 'a'"
print(format % ("+=", timeit(statement, "s = ''", number=count), statement))

statement = "s = ''.join(array.array('u', ['a']*" + str(count) + "))"
print(format % ("array", timeit(statement, "import array", number=1), statement))

statement = "s = ''.join(['a' for n in range(" + str(count) + ")])"
print(format % ("comprehensions", timeit(statement, "", number=1), statement))
