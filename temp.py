keyword=["include","int","main","getch","stdio.h","printf"]
operator=["+","-","/","*","%","&","="]
delimiter=[";",",","\n","<",">","#","(",")","{","}"]
key=[]
op=[]
delim=[]
ide=[]
r=[]
string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
import re
with open("a.txt","r+") as file:
        for line in file:
            r=re.split(r"[ #{}()<>=;+]",line)
            for letter in r:
                if letter in keyword:
                    key.append(letter)
                else:
                    for letter in line:
                        if letter in operator:
                            op.append(letter)
                        else:
                            for letter in line:
                                if letter in delimiter:
                                    delim.append(letter)
                                for letter in r:
                                    if letter in string:
                                        ide.append(letter)
                
print('keywords:',set(key))
print('operator:',set(op))
print('delimiter:',set(delim))        
print('identifier:',set(ide))         
"""
output:
keywords: {'stdio.h', 'printf', 'include', 'int', 'getch', 'main'}
operator: {'%', '=', '+'}
delimiter: {'}', ',', '{', '>', ')', '#', '<', '\n', '(', ';'}
identifier: {'', 'a', 'c', 'b'}
"""
