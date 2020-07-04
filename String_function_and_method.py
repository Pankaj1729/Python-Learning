#String function and methods
# 1. len() functon : It is used to find the length of string
name = input("Enter your name : ")
print( "length of name is " + str(len(name)))
#example : name = "PaNkAj AgRaWal"
#output : 14

# 2. lower() method : it is used to convert all letters in lowercase
print("name in lower case letters : " + name.lower())
#example : name = "PaNkAj AgRaWal"
#output : pankaj agrawal

# 3. upper() method : it is used to convert all letters in uppercase
print("name in upper case letters : " + name.upper())
#example : name = "PaNkAj AgRaWal"
#output : PANKAJ AGRAWAL

# 4. title() method : it is used to covert text 1st letter in upper case and other letters in lowercase
print("name in titled form : " + name.title())
#example : name = "PaNkAj AgRaWal"
#output : Pankaj Agrawal

# 5. count() method : it is used to count the occurance of particular letter in a text(sensitive case means 'a' is differ 'A')
print("Occurance of \'a\' in name is " + str(name.count("a")))
print("Occurance of \'A\' in name is " + str(name.count("A")))

# 6. strip() method : it is used to remove space from left and right side both
dot = "****"
print(dot + name + dot)
print("name after remove space from both side is " + dot + name.strip() + dot)

# 6.1. lstrip() method : it is used to remove space from left side
print("name after remove space from left side is " + dot + name.lstrip() + dot)

#6.2. rstrip() method : it is used to remove space from right side
print("name after remove space from right side is " + dot + name.rstrip() + dot)

# 7. replace() method : it is used to replace a particular character or special character with other character or special character
# Note : it is not change the original string but it create new string
print("after replacing the chracter from name new name is " + name.replace("a","S"))# it treplace all 'a' with 'S'
print("after replacing first 'a' with 'S' is " + name.replace('a','S',1))

# 8. find() method : it is used to find the position of particular chracter or text from string
print("position of 'is' in string is " + str(name.find('is')))
pos = name.find('is')
print("position of is after 1st occurance of is " + str(name.find( 'is', pos+1)))

# 9. center() method : it is used to centerised the text or print between any special character
#and parameter pass here is more than length of word   
print("centerized name is " + name.center(22,"$"))
