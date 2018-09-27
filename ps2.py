list1 = ['a','b','c','d','e','f','g','h','i']
list2 = ['j','k','l','m','n','o','p','q','r']
list3 = ['s','t','u','v','w','x','y','z','_']

x = input("Enter rotations: ")
k1 = int(x.split(" ")[0])
k2 = int(x.split(" ")[1])
k3 = int(x.split(" ")[2])

strr = input("Input String: ")

list4=[]
list5=[]
list6=[]

for ch in strr:
	print(ch)
	if ch in list1:
		list4.append(ch)
	elif ch in list2:
		list5.append(ch)
	elif ch in list3:
		list6.append(ch)


def rotate(listt, n):
	for i in range(len(listt)):	
		listt[]

rotate(list4,k1)
rotate(list5,k2)
rotate(list6,k3)


