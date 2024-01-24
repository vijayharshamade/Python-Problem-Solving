s = "This_IS_book"
is_alpha_and_underscore = True 

for i in s:
    if (i.isalpha() and i.isupper()) or i=="_":
        continue
    else:
        is_alpha_and_underscore = False
        
    
#print(is_alpha_and_underscore)

length_s = len(s.split("_"))
#print(length_s)

if is_alpha_and_underscore:
    print(is_alpha_and_underscore,length_s,end="")
else:
    print(False)