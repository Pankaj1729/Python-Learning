#method used in list1
list1=[1,2,3,"pankaj",'kumar',2.0,3.6]
print("first list1 is :",list1)
#method used for inserting new elements in list1

#insert method

#1. insert at any position 
list1.insert(5,"agrawal")
print("list1 after insert element at 5th position :",list1)

#2.concatenation of list1
list2=[7,8,3,8,5]
list13=[8,2,3,8,6]
print(list2,list13,"concatenated list1 are :",list2+list13)

#3.append method
list2.append(list13)
print("after append method list2 is :",list2)
print(list2[5])
#4.extend method
list13.extend(list1)
print("after extending list13 with list1 is :",list13) 



#method used for deleting an element from list1

#1.pop method: it is used to pop the item from list1 and also return the poped value
number=list1.pop()
print("After poping element from last list1 is :",list1)
print("poped value is :",number)
#1.1 pop element from specific position
list1.pop(2)
print("element pop from 2nd index now list1 is :",list1)

#2.delete or del method
del list1[1]
print("delete element from 1st index now list1 is :",list1)

#3.remove method : this method is used to remove any specific element from list1
list1.remove("kumar")
print("list1 after remove \'kumar\' from list1 :",list1)

#4.count method: used to count number of word in list1
print(list1.count("pankaj"))

#5.sort method :used to sort the list1
list14=[7,8,3,8,5,8,2,3,8,6]
list14.sort()
print(list14)

#6.sorted function: it is also used to sort the list1
list15=[9,7,6,1,0,8,7,7,0,6]
print(sorted(list15))

#7.clear method:it is used to clear the whole list1
list2.clear()
print(list2)

#8.copy method
list15.sort()
list14.extend(list15)
list15=list14.copy()
list15.sort()
print(list15)

#9.join method: used to convert list1 to string
print("".join(str(list15)))

#10. crete list1 using range
list6=list(range(1,11))
print(list6)

#11.index method
print(list6.index(2))

#12. min function
list9=[1,90,390,890]
print(min(list9))

#13. max function
print(max(list9))
