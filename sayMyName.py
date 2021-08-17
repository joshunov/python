'''
## Proof of work, session 1
Write a program called `sayMyName.py` that prints out your name N times, where N is the first digit of your SID. 
For example, if your SID is 432422232 and your name is Kimi Nonawa, then you would print:
```
Kimi Nonawa
Kimi Nonawa
Kimi Nonawa
... (repeat 432 times total)
Kimi Nonawa 
```
'''


my_name = "Josh Novick"
SID = '510****83'
N = int(SID[0:2])
for i in range(N):
    print(my_name)
