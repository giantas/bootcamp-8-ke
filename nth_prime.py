#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def is_prime(nth):
    
    first_value = 2
    prime_list = [first_value]
    
    if nth < 1:
        return "value cannot be less than 1"
        
    
    elif nth == 1:
        return prime_list
    else:
        while len(prime_list) < nth:
            first_value += 1
            if first_value % 2 == 0:
                pass
            else:
                for n in range(1,first_value):
                    if first_value % n == 0:
                        pass
                    else:
                        if first_value not in prime_list:
                            prime_list.append(first_value)

        return prime_list
    

def main():
    nth_value = input("Enter nth value: ")
    
    print "Result: ",is_prime(nth_value)
    

if __name__ == "__main__":
    main()
