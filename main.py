import sys
import os

path = './text.txt'
with open(path, 'r') as f:
    content = file.read()
    print(content)

with open(path, 'w') as f:
    file.write(content + "\nAppended content from main.py")
