Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s = "python"
>>> s
'python'
>>> p=""
>>> p
''
>>> s
'python'
>>> t = 'programming'
>>> t
'programming'
>>> s+t
'pythonprogramming'
>>> t*2
'programmingprogramming'
>>> s*7
'pythonpythonpythonpythonpythonpythonpython'
>>> '0'*10
'0000000000'
>>> s = 'python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> s[7]
'j'
>>> s[-1]
'i'
>>> s[5]
'n'
>>> s[-5]
's'
>>> s[12]
'f'
>>> s[-3]
'a'
>>> s
'python java flask mysql fastapi'
>>> s[0:6:1]
'python'
s[0:4:5]
'p'
s[:5]
'pytho'
s[:6]
'python'
s[7:11]
'java'
s[9:13]
'va f'
s[13:17]
'lask'
s[12:17]
'flask'
s[19:23]
'ysql'
s[18:23]
'mysql'
s[-2:3]
''
s[-4:4]
''
s[::-11]
'iya'
s[24:]
'fastapi'
s[-7:]
'fastapi'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s
'python java flask mysql fastapi'
'python' in s
True
'flask' not in s
False
'java' not in s
False
'java' in s
True
'c++' not in s
True
'c' in s
False
s
'python java flask mysql fastapi'
len(s)
31
ord('s')
115
ord('a')
97
ord('A')
65
ord('+')
43
ord('*')
42
ord('@')
64
chr(12)
'\x0c'
chr(10)
'\n'
max(s)
'y'
s
'python java flask mysql fastapi'
min(s)
' '
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
"case sensitive"
'case sensitive'
s
'python java flask mysql fastapi'
s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower()
'python java flask mysql fastapi'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capitalize()
'Python java flask mysql fastapi'
s='python'
s
'python'
s.center(40, '_')
'_________________python_________________'
s.center(40, '@')
'@@@@@@@@@@@@@@@@@python@@@@@@@@@@@@@@@@@'
s.ljust(40.'*')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.ljust(40,'*')
'python**********************************'
s.rjust(40,'*')
'**********************************python'
'l'.zfill(5)
'0000l'
'123'.zfill(5)
'00123'
'12345667'.zfill(5)
'12345667'
"finding methos"
'finding methos'
s
'python'
s = 'python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s.find('y')
1
s.rfind('f')
24
s.index('p')
0
s.index('a')
8
s.rindex('m')
18
"finding methods"
'finding methods'
s.count('n')
1
s.ounnt('a')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.ounnt('a')
AttributeError: 'str' object has no attribute 'ounnt'. Did you mean: 'count'?
s.cound('a')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.cound('a')
AttributeError: 'str' object has no attribute 'cound'. Did you mean: 'count'?
s.count('a')
5
s = '      codeg  nan     '
s
'      codeg  nan     '
s.strip()
'codeg  nan'
s.lstrip()
'codeg  nan     '
s.rstrip()
'      codeg  nan'
s = 'python java flask mysql fastapi'
s
SyntaxError: multiple statements found while compiling a single statement
s
'      codeg  nan     '
s = 'python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s.replace('a','*')
'python j*v* fl*sk mysql f*st*pi'
s.maketrans
<built-in method maketrans of type object at 0x00007FFB70B2C0C0>
s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
s.translate(s.maketrans('apkqs','12345'))
'2ython j1v1 fl153 my54l f15t12i'
s.translate(s.maketrans('aeiou','*****'))
'pyth*n j*v* fl*sk mysql f*st*p*'
