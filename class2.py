#ls1 = []
#print(type(ls1))
#ls2 = list()
#adding the values
#ls1.append(12)
#ls1.append(2.2)
#print("ls1",ls1)
#now adding two lists
#ls2.append(23)
#ls2.append("This is list 2")
#print("ls2",ls2)
#ls1.extend(ls2)
#print("ls1 extended",ls2)
#Now slicing list 
#ls3=[11,1.1,"3 list", 1.2,3,"abhi",233]
#print(ls3[3]) #indexing positive which have not and minu value 
#negative indexing work from rhs
#ls3=[11,1.1,"3 list", 1.2,3,"abhi",233]
#print(ls3[-1])
#Slicing
ls3=[11,1.1,"3 list", 1.2,3,"abhi",233]
#print(ls3[3:5])# it take 3 index position and 5th to print
#default starting start from the 0th index
#print("default indea",ls3[:5])
#step value
#print("Step value",ls3[2:3:1])
#reverse
#print("reverse",ls3[::-1])#revering the list
#negative index
#print("negative index",ls3[4:-2])
#manupulating the data or inserting the in existing list
#ls3.insert(2,"hello")#replaces 2nd index with "hello"
#print(ls3)
#pop function to remove from the list
#ls3.pop(-3)#removing the 3rd index from rhs
#print(ls3)
#remove function
#ls3.remove(1.1)
#print(ls3)
#tuple = orders, immutable, alows duplicate,hetrogeneous
#creating
#t1=()
#print(type(t1))
#t1=(1,2,3,4,"hi")
#typecasting tuples to add in the tuples
#print(list(t1))
#t2=list(t1)#here it has duplicate values of t1
#print(t2)
#set = unorderd,mutale,no duplication
#set creation
#1={12,13,14,11}
#print(s1)#it prints in orderd list
#s2={12,25,67,89}
#print(s2)
# set ops
#odd ={1,3,5,7,9}
#even={2,4,6,8}
#prime={1,3,5,7}
#u =odd.union(even)#combies all
#print(u)
#i=odd.inersection(prime)
#print(i)
#stings = orderd,immutable,text rep
#st1= "hye"
#st2="hello"
#x=st1+st2
#print("concatinate",x)
#print("split",x.split("o"))#here it skips the value 
#print(st1.upper())# makes evrything in upper letter