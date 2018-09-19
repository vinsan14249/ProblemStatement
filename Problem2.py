#!/usr/bin/python                                       # for linux support

import re                                                    #   module for regular expression

while True:
    pwd = input('\nInput comma separated passwords :\n')     #  Taking comma separated inputs from user 
    entered_passwords = [i for i in pwd.split(',')]
    print("You entered",len(entered_passwords),"passwords")
    strong_passwords = []

    for i in entered_passwords:
        if(len(i) <13):
             if re.match(r'^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$&]).*$', i): # matching regex
                 strong_passwords.append(i)
    if (len(strong_passwords) > 0):
            print("\n Out of ",len(entered_passwords),"entered passwords their are",str(len(strong_passwords)),"strong passwords are :")
            for i in strong_passwords:
                print(i,end= "      ")
    else:
        print('\nSorry the password you entered was not between 6 and 12 characters long')
        print('Please try again')




'''
Regex Explained : ('^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$&]).*$')

- At least 1 small case letter      -   (?=.*[a-z])
- At least 1 upper case letter      -   (?=.*[A-Z])
- At least 1 number                 -   (?=.*\d)
- One character from @#$&.          -   (?=.*[@#$&])
- 6 ≤ length                        -   (?=.{6,})


Input/Outputs:

Input comma separated passwords :
Vi@12,fsnLbl@2kl00wd1,Ll@2k1,Ask_8@,123@aPp*10,Apple@1234,app@al,123455,asdfgh,123456789@ab,123456789@abc,@123456789M,123@appL
You entered 13 passwords

 Out of  13 entered passwords their are 5 strong passwords are :
Ll@2k1      Ask_8@      123@aPp*10      Apple@1234      123@appL
'''        