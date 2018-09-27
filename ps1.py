class Node: 
    # Function to initialize the node object 
	def __init__(self, data): 
		self.data = data  # Assign data 
		self.top = 0  # Initialize next as null 
		self.down = 0  # Initialize next as null 
		self.left = 0  # Initialize next as null 
		self.right = 0  # Initialize next as null 
		self.plus = 0


x = input("Enter a name: ")
n = int(x.split(" ")[0])
m = int(x.split(" ")[1])

print(n)
print(m)
mat = [[0 for x in range(m)] for y in range(n)] 
newmat = [[0 for x in range(m)] for y in range(n)] 

for i in range(n):
	mat[i]=input().split(" ")
print(mat)
		
for i in range(n):
	for j in range(m):
		newmat[i][j]= Node(mat[i][j])
		print(newmat[i][j].data)
print(mat[0][0])

maxplus=[]


for i in range(n):
	for j in range(m):
		newmat[i][j]= Node(mat[i][j])
		if(newmat[i][j].data == 's'):
			top = i-1
			down = i+1
			left = j-1
			right = j+1

			while(top>=0 and newmat[top][j].data != 'd'):
				newmat[i][j].top=newmat[i][j].top+1
				top = top-1

			while(down<n and newmat[top][j].data != 'd'):
				newmat[i][j].down=newmat[i][j].down+1
				down = down+1

			while(left>=0 and newmat[i][left].data != 'd'):
				newmat[i][j].left=newmat[i][j].left+1
				left = left -1

			while(right<m and newmat[i][right].data != 'd'):
				newmat[i][j].right=newmat[i][j].right+1
				right = right+1

			#print(newmat[i][j].top)
			#print(newmat[i][j].down)
			#print(newmat[i][j].left)
			#print(newmat[i][j].right)
			
			newmat[i][j].plus = min(newmat[i][j].top,newmat[i][j].down,newmat[i][j].left,newmat[i][j].right)

			#minimum = min(newmat[i][j].top,newmat[i][j].down,newmat[i][j].left,newmat[i][j].right)

			#maximum = min(newmat[i][j].top,newmat[i][j].down,newmat[i][j].left,newmat[i][j].right)

			#if(minimum == 0 and maximum > 0):
				#newmat[i][j].plus = -1
			#print("****")
			#print(newmat[i][j].plus)
			maxplus.append(newmat[i][j].plus)

print(maxplus)			

def Range(list1): 
    largest = list1[0] 
    largest2 = list1[0] 
    for item in list1:        
        if item > largest:  
            largest = item 
        elif largest2!=largest and largest2 < item: 
                largest2 = item 
    print("Largest element is:", (largest*4)+1 , (largest2*4)+1) 
    print("Second Largest element is:", largest2) 
  
Range(maxplus) 








