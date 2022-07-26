
# Fibonacci Sequence
# Small Python project to find the value based on the posistion within the Fibonacci sequence
# Loops 

import sys

while True: 
    while True: 
        print ('Enter the Nth Fibonacci number you wish to calculate to:')

        response = input('> ').upper()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        if response == 'QUIT':
            sys.exit()

        print('Please enter a number greater than 0, or QUIT')

    if nth == 1:
        print ('0')
        continue
    if nth == 2:
        print ('1')
        continue
    if nth > 2:
        x = [0,1]
        for i in range(0, nth-2):
            x.append(x[i] + x[i+1])
        print ('Digit ' + str(nth) + ' in the Fibonacci Sequence is: ' + str(x[nth-1]))
        continue
    
            

