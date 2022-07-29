import os
os.system('clear')

f1 = open('file1.txt')
words1 = f1.read()

f2 = open('file2.txt')
words2 = f2.read()
f1w = open('file1.txt','w')
f2w = open('file2.txt','w')

f1w.write(words2)
f2w.write(words1)