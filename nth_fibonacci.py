#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# 0,1,1,2,3,5,8

def reason(n = 7):
    if n == 1:
        return "[0]"
    elif n == 2:
        return "[0, 1]"
    
    prime_list = [0, 1]
    for i in range(n+1):
        if i > 2:
            sum = prime_list[i - 3] + prime_list[i - 2]
            prime_list.append(sum)
    return prime_list

def main():
    answer = input("Enter nth value: ")
    
    print reason(answer)
    

if __name__ == "__main__":
    main()
