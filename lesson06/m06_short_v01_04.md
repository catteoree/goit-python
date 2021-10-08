# 1 video

fh = open('test.txt')
fh
fh.read()
fh.tell()
fh.seek(0)
fh.read(3)
fh.close()

# 2 video

with open('test.txt') as fh:
...     print(fh.read())
...
fh.closed 

with open('test.txt') as fh:
...     1 / 0
...     x = 1/0
...  
Traceback (most recent call last):   
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero 

fh.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.

fh.read  
<built-in method read of _io.TextIOWrapper object at 0x00000231D1A721E0>
fh.closed
True


fh.close
<built-in method close of _io.TextIOWrapper object at 0x00000231D1A721E0>


with open('test.txt') as fh:
...     fh.write('q')
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
io.UnsupportedOperation: not writable

with open('test.txt', 'w') as fh:
...     fh.write('World!!!')
... 
8

with open('test.txt') as fh:
...     print(fh.read())
... 
World!!!

with open('test.txt', 'a') as fh: 
...     fh.write('Hello!')   
... 
6

with open('test.txt') as fh:
...     print(fh.read())
... 
World!!!Hello!

with open('test.txt', 'r+') as fh:
...     fh.write('\nnew line')
...     print(fh.read())
... 
9
llo!

# 3 video

with open('m05regexr.PNG') as fh:  
...     data = fh.read(12)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "C:\Users\User\AppData\Local\Programs\Python\Python39\lib\encodings\cp1251.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 139: character maps to <undefined>

with open('m05regexr.PNG', 'b') as fh:
...     data = fh.read(12)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Must have exactly one of create/read/write/append mode and at most one plus

with open('m05regexr.PNG', 'rb') as fh:
...     data = fh.read(12)
... 
data
b'\x89PNG\r\n\x1a\n\x00\x00\x00\r'
for b in data:
...     print(b)
... 
137
80
78
71
13
10
26
10
0
0
0
13

with open('first12bytes.PNG', 'wb') as fh:
...     fh.write(data)
... 
12

type(data)
<class 'bytes'>

# 4 video

import shutil


archive_name = shutil.make_archive('backup', 'zip', 'lesson06/img')
shutil.unpack_archive(archive_name, 'lesson06/new_folder_for_data')
shutil.rmtree('lesson06/new_folder_for_data')
shutil.copytree('lesson06/img', 'lesson06/new_folder_for_data')

