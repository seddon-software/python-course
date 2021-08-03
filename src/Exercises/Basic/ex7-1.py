'''
Write a program that emulates the word count program: wc.
Use the file "zen.txt" as input and print out the number of
characters, words and lines in the file.
'''
import os

os.system("wc data/zen.txt")
with open("data/zen.txt", "r") as f:
    text = f.read()
    print(f"characters = {len(text)}")
    print(f"words = {len(text.split())}")
    print(f"lines = {len(text.split(chr(10)))-1}")

