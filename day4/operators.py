Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"ARITHMETIC OPERATOR"
'ARITHMETIC OPERATOR'
a=10
b=20
a
10
b
20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a//b
0
a**b
100000000000000000000
"comparison operatior"
'comparison operatior'
a
10
b
20
a==b
False
a<b
True
a<-b
False
a>-b
True
a<=b
True
a>=b
False
""LOGICAL OPERATORS"
SyntaxError: unterminated string literal (detected at line 1)
A
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
10
b
20
a%2 == 0 and a>10
False
b
20
b%2 == 0 and b>10
True
b%2 == 0 or b>10
True
b%2==0
True
not b%2==0
False
"MEMBERSHIP OPERATORS"
'MEMBERSHIP OPERATORS'
#st list tuple set dict
s = 'python'
'p' in s
True
't' in s
True
'y'
'y'
'y' in s
True
't' in s
True
'z' in s
False
'p'
'p'
'p' not in s
False
'r' not in s
True
l = [ "python", "c", "html", "ml"]
'l' in python
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    'l' in python
NameError: name 'python' is not defined
"python" in l
True
"ai" in l
False
"c" in l
True
"html" not in l
False
"c" not in l
False
s={1,2,3,4}
4 in s
True
5 in s
False
2 in s
True
7 in s
False
3 not in s
False
d={1:2, 2:4, 3:6, 4:8}
10 in d
False
1 in d
True
2 in d
True
5 not in d
True
6 not in d
True
"IDENTITY OPERATOR"
'IDENTITY OPERATOR'
l = [1,2,3,4]
m = [1,2,3,4]
id(l)
2278639675648
id(m)
2278639671616
>>> l == m
True
>>> l is m
False
>>> n = m
>>> n
[1, 2, 3, 4]

>>> id(n)
2278639671616
>>> id(m)
2278639671616
>>> n is m
True
>>> "ASSIGNMENT OPERATORS"
'ASSIGNMENT OPERATORS'
>>> a
10
>>> b
20
>>>  c
...  
SyntaxError: unexpected indent
>>> c = 10
>>> c
10
>>> c +=10
>>> c
20
>>> c -=10
>>> c
10
>>> c +=10
>>> c
20
>>> c = c+10
>>> c
30
