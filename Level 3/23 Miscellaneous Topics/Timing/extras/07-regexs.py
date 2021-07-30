from timings import Timings

t1 = Timings(title = "compiled regex",   setup = (
                                                  'import re' '\n'
                                                  'text = "This line contains the numbers 8.73 and 4.67"' '\n'
                                                  'numberPattern = r"\d+\.\d+"' '\n'
                                                  'pattern = re.compile(numberPattern)'
                                                 ), 
                                         statement = "result = pattern.search(text)")
t2 = Timings(title = "uncompiled regex", setup = (
                                                  'import re' '\n'
                                                  'text = "This line contains the numbers 8.73 and 4.67"' '\n'
                                                  'numberPattern = r"\d+\.\d+"'
                                                 ),
                                         statement = "result = re.search(numberPattern, text)")

Timings.titles()
t1.run(1000000)
t2.run(1000000)
