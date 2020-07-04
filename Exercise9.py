name = input("enter your name : ")
n=len(name)
i=0
#j=0
#k=0
#while i<n:
 #   k=name.count(name[i])
  #  if k>1:
   #     while j<(i-1):
    #        if name[j]==name[i-1]:
     #           j+=1
      #          i+=1
    #else:
     #   print(f"{name[i]} in name is {k} times")
   # i +=1
temp=""
while i<n:
    if name[i] not in temp:
         print(f"{name[i]} in name is {name.count(name[i])} times")
         temp += name[i]
    i +=1
