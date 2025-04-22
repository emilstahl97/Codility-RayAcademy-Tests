'''
You are given a string S, which consists entirely of decimal digits (0–9). Using digits from S, create a palindromic number with the largest possible decimal value. You should use at least one digit and you can reorder the digits. 
A palindromic number remains the same when its digits are reversed; for instance, "7", "44" or "83238". Any palindromic number you create should not, however, have any leading zeros, such as in "0990" or "010".

For example, decimal palindromic numbers that can be created from "8199" are: "1", "8", "9", "99", "919" and "989". Among them, "989" has the largest value.

Write a python function:

def solution(S):

that, given a string S of N digits, returns the string representing the palindromic number with the largest value.

Examples:
Given "39878", your function should return "898".

Given "00900", your function should return "9".

Given "0000", your function should return "0".

Given "54321", your function should return "5".

Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];

String S is made only of digits (0–9).
                                 
'''

from collections import Counter

def solution(S: str):
    print('S: ' + S)

    # 1: count frequency of digits in  

    s_freq_counter = {}

    for number in S:
        if number in s_freq_counter:
            s_freq_counter[number] += 1
        else:
            s_freq_counter[number] = 1

   
    # 2: special case, all zeros 

    if set(S) == {'0'}:
        return "0"

   
    #3: find largest digit to put in middle

    # largest number
    middle = ""

    for number in range(9, 0, -1):
        str_number = str(number)

        if str_number in s_freq_counter and s_freq_counter[str_number] % 2 == 1:
            middle = str_number
            print(middle)

            s_freq_counter[str_number] -= 1
            break


    # 4 build first half of palindrome, put largest digits first to maximize, then just reverse for other half
    half = []
    for number in range(9, 0, -1):
        str_number = str(number)

        #if number == 0 and not half:
        #   continue

        if str_number in s_freq_counter:
            pairs = s_freq_counter[str_number] // 2
            half.extend([str_number] * pairs)
            print(half)

   
    
    # 5 no pairs, no middle, just return max digit
    if not half and not middle:
        for number in range(9, 0, -1):
            str_number = str(number)
            if str_number in s_freq_counter:
                return str_number
        


    # just build palindrome

    print(half)
    palindrome = half + [middle] + half[::-1]

    return ''.join(map(str, palindrome))


s = "4382872"
  
palindrome = solution(s)

print(palindrome)