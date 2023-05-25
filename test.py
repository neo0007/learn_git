#! /usr/bin/python

import sys

def main():
 
    digit1 = int(sys.argv[1])
    digit2 = int(sys.argv[2])
    digit3 = int(sys.argv[3])

# Print out the input
    print ("Here is our input:")
    print ("Input 1 is: " + str(digit1))
    print ("Input 2 is: " + str(digit2))
    print ("Input 3 is: " + str(digit3))


# Do some math
    num = digit1 * (digit2 + digit3)
    num_new = digit1 * digit2 * digit3
# Now print out the results
# print is an output
    print("Results: ")
    print( num )
    print('This is the second output expression, with num=' + str(num))
    print( 'argv[1] * argv[2] * argv[3] =' + str(num_new))

if __name__ == '__main__':
    main()
