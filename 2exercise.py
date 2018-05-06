>>> (5 > 4) and (3 == 5)
False
>>> not (5 > 4)
False
>>> (5 > 4) or (3 == 5)
True
>>> not ((5 > 4) or (3 == 5))
False
>>> (True and True) and (True == False)
False
>>> (not False) or (not True)
True
>>> 

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
