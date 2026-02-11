#IF ELSE ELIF
#Simple flow control

#If condition
x = True
if x:
    print('yes')        #This is called a scope (bit inside the if)
    print('again')      #This is called a scope (bit inside the if)
else:
    print('no')

#Condition evaluations (True - run | False - not run)
x = 100
y = 25
if y ==x: print('equal to')                 #Don't need to do tab indents. Can do one line
if y !=x: print('not equal to')             #Don't need to do tab indents. Can do one line
if y <x: print('less than')                 #Don't need to do tab indents. Can do one line
if y >x: print('greater than')              #Don't need to do tab indents. Can do one line
if y <=x: print('less than or equal to')    #Don't need to do tab indents. Can do one line
if y >=x: print('greater than or equal to') #Don't need to do tab indents. Can do one line

#Elif is the switch solution
x = 10
if x ==25:
    print('x = 25')
elif x ==50:
    print('x = 50')
elif x ==75:
    print('x = 75')
elif x ==100:
    print('x = 50')
else:
    print('Catch All Here')

#Nested statements
x = 82
if x >50:
    print('over 50')
    if x >60:
        print('over 60')
        if x > 70:
            print('over 70')
            if x > 80:
                print('over 80')
                if x > 90:
                    print('over 90')
                    if x > 100:
                        print('over 100')
