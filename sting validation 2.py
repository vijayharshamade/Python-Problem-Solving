s=input()
is_firstletter_lower = s[0].islower()
#print(is_firstletter_lower)
no_of_letters = 1 
are_letters = True

for i in s:
    if i.isalpha():
        continue
    else:
        are_letters = False 
    
for i in s:
    if i.isupper():
        no_of_letters+=1 

#print(no_of_letters)

if (is_firstletter_lower and are_letters):
    print(True,no_of_letters,end="")
else:
    print(False)