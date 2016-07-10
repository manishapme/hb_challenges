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

"""


def dec2bin(num):
    """Convert a decimal number to binary representation."""
    
    if type(num) != int:
        print 'Function only works with integers'
        return
    elif num == 0:
        return str(0)

    binary_str = ""
    base = 2
    r = num

    for i in range(7, -1, -1):
        x = base ** (i)
        if r == x:
            binary_str = binary_str +'1'
            print "r == x: " + binary_str + "r " + str(r)  + " x: " + str(x)
        elif (r == num) and (x > num):
            print "r == num: " + binary_str  + "r " + str(r)  + " x: " + str(x)
            pass

        elif r < x:
            binary_str = binary_str +'0'
            print "r < x " + binary_str  + "r " + str(r)  + " x: " + str(x)
        elif r > 0:
            binary_str = binary_str +'1'
            print "r > 0 " + binary_str  + "r " + str(r)  + " x: " + str(x)

        r = num % x


    return binary_str



dec2bin(15)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
