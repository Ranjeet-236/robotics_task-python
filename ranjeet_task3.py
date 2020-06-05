from array import *
#to use array function


def A():
	
 print("                  ● PM-CM stick's Red zone\n")
 arr=array('i',[])
 rpt=array('i',[])
 #create two blank array
 h= -1
 z=int(input("Enter the number of sticks : "))
 for j in range(z):
	 n=int(input("enter the length of next stick : "))
	 arr.append(n)
	 #value of n stores in "arr"array
 for i in arr:
	 arr.remove(i)
	 #remove the element i from "arr" array
	 for p in arr:
		 if p==i:
			 rpt.append(p)
			 arr.remove(i)
			 
 k=len(rpt)
 #find the number of element in 'rpt' array
 if k>=2:
	 d=max(rpt)
	 #stores max value from rpt
	 rpt.remove(d)
	 e=max(rpt)
	 g=d*e
	 print("")
	 print("area is :" , g)
	
 else:
	 print("area is :" ,h)

                #first task end

def B():
 print("        ● length calculator(longest alternating sub array)\n")
 arr=[]
 p=[]
 #create two blank list
 n=int(input("Enter size of array : "))
 #take nput from user
 for i in range(n):
	 x=int(input("Enter the next element : "))
	 #take nput from user
	 arr.append(x)
 a=len(arr)
 b=a-2
 for i in range(b):
	 if arr[i] > 0:
		 if arr[i+1] < 0:
			 if arr[i+2] > 0:
				 p.append(3)
				 #add 3 to list p
			 else:
				 p.append(2)
				 #add 2 to list p
		 else:
			 p.append(1)
	 else:
		 if arr[i+1] > 0:
			 if arr[i+2] < 0:
				 p.append(3)
			 else:
				 p.append(2)
		 else:
			 p.append(1)
			 #add 1 to list p

 if arr[b] >0:
	 if arr[b+1]<0:
		 if arr[0] >0:
			 p.append(3)
		 else:
			 p.append(2)
	 else:
		 p.append(1)
		
 if arr[b] <0:
	 if arr[b+1] >0:
		 if arr[0]<0:
			 p.append(3)
		 else:
			 p.append(2)
	 else:
		 p.append(1)
	

 if arr[b+1] >0:
	 if arr[0]<0:
		 if arr[1] >0:
			 p.append(3)
		 else:
			 p.append(2)
	 else:
		 p.append(1)
		
 if arr[b+1] <0:
	 if arr[0] >0:
		 if arr[1]<0:
			 p.append(3)
		 else:
			 p.append(2)
	 else:
		 p.append(1)

 print("output: " ,p)
 #show the output in screen
 
                  #second task end
 
def C():
	
	print("               ● VSSUT point calculator\n")
	print('X= '+"The extra points needs to qualify for play off")
	print('Y= '+"The number of remaining match\n")
	a=int(input("Enter the value of X : "))
	b=int(input("Enter the value of Y : "))
	#take 2 input from user
	print("\n")
	c=2*b
	d=a-b
	k=0
	
	if c>=a:
		if d<=0:
			print("Number of matches required to qualify for play off is :" , k)
		else:
			print("Number of matches required to qualify for play off is : ", d)
	else:
		print("invalid input of Y\n")
		print("It is guaranteed that VSSUT will qualify for playoffs if win all their remaining Y matches.")

                     #third task end

def D():
	
 print("                  ● RS's movie plan\n")
 length=array('i',[])
 rating=array('i',[])
 con=array('i' ,[])
 #create 3 blank array
 a=int(input("Enter the number of movies : "))
 for i in range(a):
	 x=int(input("Enter the length of next movie : "))
	 y=int(input("Enter the rating of next movie : "))
	 #take input from user
	 length.append(x)
	 rating.append(y)
	 #add valur of x and y to array length ad rating respectively
	 z=x*y
	 con.append(z)
 p=max(con)
 k=1
 for i in con:
	 if i==p:
		 break
	 k=k+1
 print("")
 print("OUTPUT: " + "movie number" ,k)
 #print the result

                 #fourth task end

def E():
	
 print("● minimum cost need to convert a array to single element array\n\n")
 file=array('i',[])
 a=int(input("enter the size of array :"))
 for i in range(a):
	 x=int(input("enter the next number :"))
	 file.append(x)
 b=min(file)
 #store minimum value from file in b
 d=b*(a-1)
 print("")
 print('size of array is :',a)
 print("The array is :",file)
 print("OUTPUT :",d)
 #show the result in screen

                     # END
                     
                     

print("1. PM-CM stick's Red zone")
print("2. maximun length of alternating sub array")
print("3. VSSUT point calculator")
print("4. RS's movie plan")
print("5. minimum cost finder (convert a array to single element array)\n\n")
v=int(input('enter the serial number of task you want to perform : '))
print("\n\n")

if v==1:
	A()
elif v==2:
	 B()
elif v==3:
	 C()
elif v==4:
	 D()
elif v==5:
	 E()
else:
	print("* invalid serial no input ")
 
	
print("hi i am rnjeet")



	


