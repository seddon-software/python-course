"""
Write a program that prints out the square, cubes and fourth 
power of the first 20 integers.
"""

print(f"{'N':>8s}{'N**2':>8s}{'N**3':>8s}{'N**4':>8s}")

for i in range(1,21):
    print(f"{i:>8}{i**2:>8}{i**3:>8}{i**4:>8}")
          
