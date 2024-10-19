import os
os.system("pipx run build")
os.system("pip install .")
import example
print(example.square(5))

