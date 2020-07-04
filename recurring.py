def recurring_character(s):
    for i in s:
        for j in range(1,len(s)):
                n=0
                if (i==s[j]):
                    n+=1
                    if(n==1):
                        return s[j]
str1=input("Enter a string ")
print(recurring_character(str1))
#ABCA
