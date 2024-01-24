strr = 'a))(cd))))()(0c'

#output a 1 , ) 7 , ( 3 , c 2 , d 1 , 0 1

#sort the above frequencies in desencing order
# output   ) 7 , ( 3 ,  c 2 , a 1 , d 1 , 0 1 

new_dict = {}
# Calculate frequencies
for char in strr:
    if char in new_dict:
        new_dict[char] += 1 
    else:
        new_dict[char] = 1 
        
print(new_dict)

# Print frequencies
for char, count in sorted(new_dict.items(), key=lambda x: x[1], reverse=True):
    print(f'{char} {count}', end=', '.strip(","))