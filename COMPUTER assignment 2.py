#QUESTION 1:
string="Python is a case sensitive language"
#part (a):
print("part(a)")
print("length of the string=",len(string))
#part (b):
print("part(b)")
print("reversed string is =",string[-1:-(len(string)+1):-1])
#part (c):
print("part(c)")
new_string=string[10:26]
print("new string stored =",new_string)
#part (d):
print("part(d)")
string=string.replace("a case sensitive ","object oriented ")
print("replaced string=",string)
#part(e):
print("part(e)")
print("index of substring 'a' =",string.index("a"))
#part(f):
print("part(f)")
print("string after removing white spaces = ",string.replace(" ",""))

#QUESTION 2:
name="HARMAN"
SID="21104097"
DEPTname="ELECTRICAL"
CGPA="9.9"
print("Hey,"+name+" Here!\nMY SID is "+SID+"\n"+"I am from"+DEPTname+" and my CGPA is "+CGPA)

#QUESTION 3:
a=56
b=10
#part (a):
print(a&b)
#part (b):
print(a|b)
#part (c):
print(a^b)
#part (d):
leftshifted_a=a<<2
leftshifted_b=b<<2
a=56
b=10
#part (e):
rightshifted_a=a>>2
rightshifted_b=b>>4

#QUESTION 4:
import math
print("ENTER 3 NUMBERS:")
n1=int(input("ENTER 1ST NUMBER"))
n2=int(input("ENTER 2ND NUMBER"))
n3=int(input("ENTER 3RD NUMBER"))
print("MAXIMUM NUMBER = ",max(n1,n2,n3))

#QUESTION 5:
string=input("ENTER STRING")
i=string.find("name")
if i==-1:
    print("NO")
else:
    print("YES")

#QUESTION 6:
print("ENTER sidelengths:")
s1=int(input("ENTER side1"))
s2=int(input("ENTER side2"))
s3=int(input("ENTER side3"))
if((s1>(s2+s3))or (s2>(s1+s3))or(s3>(s1+s2))):
    print("NO,TRIANGLE IS NOT POSSIBLE")
else:
    print("YES,TRIANGLE CAN BE FORMED")

