#!/usr/bin/env python2
#encoding: UTF-8

def fizz_buzz(n):
    """ return fizz when divisible by 3
    return buzz when divisible by 5
    return fizzbuz when divisible by both 3 and 5
    """
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'