'''
Formatting Floats
=================

Formatting floats consists of specifying a width and precision in the form:
    width.precision
followed by "f" or "e" (scientific notation).  The width can be omitted and the thousands separator can be added.
'''

n = 76.12786
print(f"precision 2:           <{n:.2f}>")
print(f"width 12, precision 2: <{n:8.2f}>")
print(f"percentage:            <{n/100:8.3%}>")
print(f"left justify:          <{n:<12.2f}>")
print(f"right justify:         <{n:>12.2f}>")
print(f"left justify:          <{n:<012.2f}>")
print(f"right justify:         <{n:>012.2f}>")


n = 12345678901.2345
print(f"comma separator:       <{n:,.2f}>")

num = 2343552.6516251625
print(f"scientific notation:   <{num:e}>")

