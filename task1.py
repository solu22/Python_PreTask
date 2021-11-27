'''Implement a Python function which returns a list of all of the numbers which are divisible by 7,
 but not divisible by 5, between 2000 and 3200 '''

import task2

def numberRange():
    divi_seven = [] # store output number
    
    # go through the given number range
    for number in range(2000, 3201):
        if number % 7 == 0 and number % 5 != 0:
             divi_seven.append(number)

    return divi_seven

if __name__ == '__main__':
    number = numberRange()
    print('List of numbers  divisible by 7 but not 5: \n{}'.format(number))


    
    
    



