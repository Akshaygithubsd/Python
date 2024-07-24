a='vjnf' # single quote string 
b="vvkjksv" #double quote string
c='''vdkjsnksk
vbkjfk'''# multiline string 
# string is immutable 

hel=a[0]
print(hel)
print(a[0:3])# starts from 0 excluding 3
print(len(a))
print(a[-3:-1])# start count from last char -1 till first
print(a[:3])# means from 0 to 3
print(a[1:])# means from 1 to length os string



#slicing with skip value

# word="akshay"
# print(word[1:5:2])
# means fetch form 1 and then fetch 2nd from that char


#functions 


# print(word.endswith("shay"))#returns boolean
# print(word.startswith("shay"))
# print(word.capitalize())# only first char
# print(word.find("shay"))
# print(word.replace("shay","bhbbd"))

# name=str(input())
# print(f"good {name}")# f string 

#detecting double spacing in string
he="hello i'm  Akshay"
print(he.find("  "))
