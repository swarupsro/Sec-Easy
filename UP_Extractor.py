# this is written on python 2
fo=open("UD3.txt","r")
users=[]
for lines in fo.readlines():
    if 'name' and 'password' in lines:
        items=lines.split() #converts to list"""
        users.append(items[1]) #append the second item that is the username"""

print users
