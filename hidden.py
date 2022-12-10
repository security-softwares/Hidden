import os
a=input('enter any audio file')
oz=os.path.isfile(a)
if oz==0:
print("not exist")
exit()
f=open(a,'ab')
m=input("enter message to hide or txt file ")
enc=input("encryption yes/no (default:no)")

try :
o=open(m,'r')
o.read()
except:

m=m




if enc=='' or enc.isspace==True:
enc='no'
ev=eval(f"b' {m.split()}'")
f.write(ev)
if enc.lower()=='yes' or enc.lower()=='y':
byte=int(input('enter encryption bytes (digit)'))


li=[]
for i in m:
ored=int(ord(i)*int(byte))
li.append(ored)

el=eval(f"b' {li}'")

f.write(el)
