import sqlite3
print("SQLite Version:", sqlite3.version)
print("Database Version:", sqlite3.sqlite_version)

import os

os.system("rm test.db")
conn = sqlite3.connect("test.db")
os.system("ls -l *.db")

