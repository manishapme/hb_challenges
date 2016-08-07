"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

    >>> dec2bin(1000000)
    '11110100001001000000'

"""


def dec2bin(num):
    """Convert a decimal number to binary representation."""
    
    if type(num) != int:
        print 'Function only works with integers'
        return

    binary_str = ""
    base = 2
    #start at one to ensure our loop will run at least once for num ==0
    num_loops = 1

    # get length of final binary string. will be minimum of 1 character.
    while (base ** num_loops) <= num:
        num_loops +=1

    # getting the range in reverse order allows us to build the string from left to right
    # stepping backwards in increments of 1 and stopping at 0
    for i in range(num_loops - 1, -1, -1):
        x = base ** (i)
        if num >= x:
            binary_str += '1'
            num -= x
        else:
            binary_str += '0'

    return binary_str



dec2bin(15)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
