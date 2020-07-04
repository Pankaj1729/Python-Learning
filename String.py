print("enter your name")
name = input("My name is ")
# 1.sting indexing
#Syntax : variable_name[index]
#example: "Deepak"
#name[0]or[-6] = D
#name[1]or[-5] = e
#name[2]or[-4] = e
#name[3]or[-3] = p
#name[4]or[-2] = a
#name[5]or[-1] = k
print("name[0] is ",name[0] )
print("name[-4] is ",name[-4] )
# 2.String slicing
#Syntax : variable_name[starting_index:end_index*]
#*Note: element print from starting_index to (end_index-1)
#example: "Deepak"
#print(name[2:4])
#output: ep
#print(name[:]) or print(name[0:])
#output: Deepak
#print(name[:5])
#output: Deepa
print("name[0:] is ",name[0:])
print("name[2:4] is ",name[2:4] )
print("name[:] is ",name[:] )
print("name[:5] is " ,name[:5])
print("name[:-6] is ",name[:-6] )
print("name[:-1] is ",name[:-1] )
print("name[-1:] is ",name[-1:] )
print("name[-6:] is ",name[-6:] )
print("name[:0] is ",name[:0] )
# 3.Step_argument_slicing
#Syntax : variable_name[start_index:end_index:step]
#Note:element print start_index to (end_index-1) step wise
#example: "Deepak"
#print(name[0:5:2])
#output: Dea
print("name[0:5:2] is ",name[0:5:2])
print(" for reverseing the string use name[-1::-1] or name[::-1]")
print("Reverse string is ",name[::-1])
print("Actual string is ",name[0::1])

