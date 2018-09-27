#Initialize th three lists
list1 = ['a','b','c','d','e','f','g','h','i']
list2 = ['j','k','l','m','n','o','p','q','r']
list3 = ['s','t','u','v','w','x','y','z','_']

#Input the rotation value
x = input("Enter rotations: ")
k1 = int(x.split(" ")[0])
k2 = int(x.split(" ")[1])
k3 = int(x.split(" ")[2])

#Input the string
strr = input("Input String: ")

list4=[]
list5=[]
list6=[]

#Divide the string into 3 parts
for ch in strr:
	if ch in list1:
		list4.append(ch)
	elif ch in list2:
		list5.append(ch)
	elif ch in list3:
		list6.append(ch)

#Function to rotate listt by n
def rotate(listt, n):
	rlistt=[]
	for i in range(len(listt)):
		rlistt.append(0)
	for i in range(len(listt)):	
		rlistt[i] = listt[((i-n)%len(listt))]
	return rlistt

#Call rotate for all the three lists
rlist4=rotate(list4,k1)
rlist5=rotate(list5,k2)
rlist6=rotate(list6,k3)

i=0
j=0
k=0

#Create new String and print
output=[]
for ch in strr:
	if ch in list1:
		output.append(rlist4[i])
		i=i+1
	elif ch in list2:
		output.append(rlist5[j])
		j=j+1
	elif ch in list3:
		output.append(rlist6[k])
		k=k+1

for ch in output:
	print(ch,end="")
print()
