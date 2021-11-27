''' Implement a Python function, 
that first creates a dictionary where the dictionary keys are numbers 1 through x (1, 2, 3, ..., x) 
and the values are the keys squared (1, 4, 9, ..., x**2). 
The function should then use this dictionary in order 
to finally return a string containing "1**2=1, 2**2=4, 3**2=9, ..., x**2=??.'''

#function defination

def dictionary_key_values():

    #dict_creation
    dict_num = {1: 1**2, 2: 2**2, 3: 3**2, 4: 4**2, 5: 5**2} 
    output = [] 
    
    # looping through key, value in dictionary items
    for k, v in dict_num.items():
        element =  str(k)+'**2='+ str(v) 
        output.append(element)
    
    return  ', '.join(output) 

if __name__ == '__main__':
    output = dictionary_key_values()
    print(output)