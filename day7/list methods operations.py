Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s = 'Python Programming'
>>> s
'Python Programming'
>>> s.startswith('p')
False
>>> s.startswith('P')
True
>>> s.startswith('Pyt')
True
>>> s.endswith('img')
False
>>> s.startswith('ing')
False
>>> s.endswith('ing')
True
>>> 's'.islower ()
True
>>> 'U'.isupper()
True
>>> 'code' .isalpha()
True
>>> 'code12'.isalpha()
False
>>> 'code123'isalnum()
SyntaxError: invalid syntax
>>> 'code123'.isalnum()
True
>>> 'code'.isalnum()
True
>>> s
'Python Programming'
>>> s.istitle()
True
'myvar'.isidentifier()
True
'my@var'.isidentifier()
False
' '.isspace()
True
'     python'.isspace()
False
'123'.isdecimal()
True
'123'.isdigit()
True
'123'.isnumeric()
True
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
s="""
hello
world
python
"""
s
'\nhello\nworld\npython\n'
s.splitlines()
['', 'hello', 'world', 'python']
l=['a','b','c','d']
'-'.join(l)
'a-b-c-d'
'@'.join(l)
'a@b@c@d'
'*'.join(l)
'a*b*c*d'
''.join(l)
'abcd'
s
'\nhello\nworld\npython\n'
s='a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'.partition('.')
('python', '.', 'py')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
"encode decode"
'encode decode'
s= "holla"
s.encode()
b'holla'
t= "holla $"
t.encode
<built-in method encode of str object at 0x0000014E31A02AC0>
s= "holla 🙃"
t= "holla 🙃"
t.encode
<built-in method encode of str object at 0x0000014E319616F0>
t= "holla 🙃"
t.encode()
b'holla \xf0\x9f\x99\x83'
"list"
'list'
l=[]
l=list[]
SyntaxError: invalid syntax
l=list()
l=[1,2,3]
l=list([1,2,3,4])
l
[1, 2, 3, 4]
type(l)
<class 'list'>
#mutable ordered dublicate hetrogeneous dynamic
l=[2,3,4,5,5]
l
[2, 3, 4, 5, 5]
l[1,1,1,1]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l[1,1,1,1]
TypeError: list indices must be integers or slices, not tuple
l=[1,1,1,1]
l
[1, 1, 1, 1]
l=[1,12.3,3+5j,"str",[1,2],(1,2),{1,2},{1:2},False,None]
l
[1, 12.3, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
"list operations"
'list operations'
[1,2]+[3,4]
[1, 2, 3, 4]
[1,2,3]*4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l= ['python', 'java', 'c', 'flask', 'fasstapi', 'mysql', 'aws']
l
['python', 'java', 'c', 'flask', 'fasstapi', 'mysql', 'aws']
l[0]
'python'
l[-1]
'aws'
l[-2]
'mysql'
l[-4]
'flask'
l
['python', 'java', 'c', 'flask', 'fasstapi', 'mysql', 'aws']
l[:3]
['python', 'java', 'c']
l[-3:]
['fasstapi', 'mysql', 'aws']
l[2:5]
['c', 'flask', 'fasstapi']
l[1::2]
['java', 'flask', 'mysql']
l[::2]
['python', 'c', 'fasstapi', 'aws']
l[::-1]
['aws', 'mysql', 'fasstapi', 'flask', 'c', 'java', 'python']
l[-3:-6:-1]
['fasstapi', 'flask', 'c']
l
['python', 'java', 'c', 'flask', 'fasstapi', 'mysql', 'aws']
'c' in
SyntaxError: invalid syntax
'c' in l
True
'python' not in l
False
'html' not in l
True
'aws' in l
True
"list methods"
'list methods'
l
['python', 'java', 'c', 'flask', 'fasstapi', 'mysql', 'aws']
len(l)
7
sorted(l)
['aws', 'c', 'fasstapi', 'flask', 'java', 'mysql', 'python']
max(l)
'python'
min(l)
'aws'
l
['python', 'java', 'c', 'flask', 'fasstapi', 'mysql', 'aws']
id(l)
1435304026112
l=['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
id(l)
1435351633472
l[1]
'java'
l[1]='html'
l
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws']
id(l)
1435351633472
1[2]='c++'
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    1[2]='c++'
TypeError: 'int' object does not support item assignment
id(l)
1435351633472
l[2]='c++'
l
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
l[3]='css'
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws']
l.append['b']
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    l.append['b']
TypeError: 'builtin_function_or_method' object is not subscriptable
l.append('b')
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'b']
l.append('c')
l.append('d')
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'b', 'c', 'd']
l.insert([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    l.insert([1,2,3,4])
TypeError: insert expected 2 arguments, got 1
l.extend([1,2,3,4])
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'b', 'c', 'd', 1, 2, 3, 4]
l.insert(1,'flask')
l
['python', 'flask', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'b', 'c', 'd', 1, 2, 3, 4]
l.insert(2,'c')
l
['python', 'flask', 'c', 'html', 'c++', 'css', 'fastapi', 'mysql', 'aws', 'b', 'c', 'd', 1, 2, 3, 4]
id(l)
1435351633472
