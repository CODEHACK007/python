... 
>>> spam = input()
1111
>>> spam
'1111'
>>> bacon = 20
>>> bacon + 1
21
>>> 'spam' + 'spamspam'
'spamspamspam'
>>> 'spam' * 3
'spamspamspam'
>>> 'I have eaten ' + 99 + ' burritos.'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> 'I have eaten ' + '99' + ' burritos.'
'I have eaten 99 burritos.'
>>> 'I have eaten ' + str(99) + ' burritos.'
'I have eaten 99 burritos.'
>>> 
