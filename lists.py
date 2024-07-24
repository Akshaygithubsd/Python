hello=["nvnv",56,"vnnv"]
print(hello)
hello[0]="Akshay"
print(hello)#unlike strings lists are mutable
print(hello[0:2])
hello.append("insert")#inserts at end
print(hello)
aks=[0,5,6,5,5]
aks.sort()
print(aks)
aks.reverse()
print(aks)
aks.insert(2,565)#means at index 2
print(aks)
aks.pop(0)#del at index 0
print(aks)
aks.remove(0)#means remove 0 from list
print(aks)#<class 'tuple'>

#tuple 

a=(5,6,6,6,5)
print(type(a))
#tuple is immutable
print(a)
b=a.count(6)
d=a.index(6)#give index of 6
print(d)
