#spam = int(input())
#don't use above as it crashes for string input like line 23
spam = input()
#if spam == 1:
#doesn't work without '' because input() returns string
if spam == '1':
  print('Hello')
elif spam == '2':
  print('Howdy')
else:
  print('Greetings!')
  
Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
   
 1
Hello
   
 2
Howdy
   
 4
Greetings!
   
 asdf
Greetings!
