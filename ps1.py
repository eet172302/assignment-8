#Node that stores 5 things, value, top, down, left and right
class Node:  
	def __init__(self, data): 
		self.data = data  
		self.top = 0
		self.down = 0  
		self.left = 0 
		self.right = 0 
		self.plus = 0

#Take input
x = input("Enter dimensions: ")
n = int(x.split(" ")[0])
m = int(x.split(" ")[1])

#Initialize mtrix
mat = [[0 for x in range(m)] for y in range(n)] 
newmat = [[0 for x in range(m)] for y in range(n)] 

#Take input in matrix
for i in range(n):
	mat[i]=input().split(" ")
		
for i in range(n):
	for j in range(m):
		newmat[i][j]= Node(mat[i][j])
maxplus=[]

#Parse through the matrix to find no. of 's' in top, left, down, right
for i in range(n):
	for j in range(m):
		if(newmat[i][j].data == 'S'):
			top = i-1
			down = i+1
			left = j-1
			right = j+1

			while(top>=0 and newmat[top][j].data != 'D'):
				newmat[i][j].top=newmat[i][j].top+1
				top = top-1

			while(down<n and newmat[down][j].data != 'D'):
				newmat[i][j].down=newmat[i][j].down+1
				down = down+1

			while(left>=0 and newmat[i][left].data != 'D'):
				newmat[i][j].left=newmat[i][j].left+1
				left = left -1

			while(right<m and newmat[i][right].data != 'D'):
				newmat[i][j].right=newmat[i][j].right+1
				right = right+1

			#Find min of top, down, left and right
			#this will give length of plus on that element
			newmat[i][j].plus = min(newmat[i][j].top,newmat[i][j].down,newmat[i][j].left,newmat[i][j].right)

			maxplus.append(newmat[i][j].plus)

#Function to get 2 maximum elements
def Large(list1): 
    largest = list1[0] 
    largest2 = list1[0] 
    for item in list1:        
        if item > largest:  
            largest = item 
        elif largest2!=largest and largest2 < item: 
                largest2 = item 
    print((largest*4)+1 , (largest2*4)+1) 

Large(maxplus) 

