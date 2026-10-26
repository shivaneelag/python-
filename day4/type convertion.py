Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b = 10.4
b
10.4
int(b)
10
complex(b)
(10.4+0j)
str(b)
'10.4'
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c = 3+4j
c
(3+4j)
int(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
list(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
bool(c)
True
tuple(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
str(c)
'(3+4j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
s = codegnan
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s = codegnan
NameError: name 'codegnan' is not defined
s = "codegnan"
s
'codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
dict(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
t = (1,2,3,4)
t
(1, 2, 3, 4)
int(t)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
list(t)
[1, 2, 3, 4]
float(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
dict(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> set(t)
{1, 2, 3, 4}
>>> bool(t)
True
>>> str(t)
'(1, 2, 3, 4)'
>>> l = [1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> tuple(l)
(1, 2, 3, 4)
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> str(l)
'[1, 2, 3, 4]'
>>> dic = [1:2, 2:2, 3:3]
SyntaxError: invalid syntax
