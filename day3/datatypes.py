Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> b = 2.3
>>> type(b)
<class 'float'>
>>> c = 2+5j
>>> type(c)
<class 'complex'>
>>> s = "Codegen"
>>> type(s)
<class 'str'>
>>> l =[1,2,3,4]
>>> type(l)
<class 'list'>
>>> k = [1, 3.4, 5, "54", [2,3,4]]
>>> k
[1, 3.4, 5, '54', [2, 3, 4]]
>>> type (k)
<class 'list'>
>>> l = [1,1,1,1,1]
>>> l
[1, 1, 1, 1, 1]
>>> type(l)
<class 'list'>
>>> l.pop
<built-in method pop of list object at 0x00000273E6D73780>
>>> l.pop()
1
>>> l = [1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> id(l)
2696824477760
>>> l
[1, 2, 3, 4]
>>> t=(1,2,3)
>>> t=(1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t=(1, 2.3)
>>> t
(1, 2.3)
>>> type(t)
<class 'tuple'>
<class 'tuple'>
SyntaxError: invalid syntax
s ={34,123,2345,1235,136]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s ={34,123,2345,1235,136}
s
{34, 1235, 136, 2345, 123}
type(s)
<class 'set'>
d={l:"one",2:4, 3:[1,2,3],5:(1,34)}
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d={l:"one",2:4, 3:[1,2,3],5:(1,34)}
TypeError: unhashable type: 'list'
d={1:"one" ,2:4, 3:[1,2,3],5: (1,23)}
d
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
pro = {"pro_name":'laptop' ,"price":55000,"discount":10}
pro
{'pro_name': 'laptop', 'price': 55000, 'discount': 10}
type(d)
<class 'dict'>
status =True
type(status)
<class 'bool'>
s =False
type(s)
<class 'bool'>
s=None
type(s)
<class 'NoneType'>
