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


def solution(S: str):

    # 1: count frequency of digits in S 

    freq = {}

    for digit in S:
        if digit in freq:
            # increase count
            freq[digit] = freq[digit] + 1
        else:
            freq[digit] = 1
    
    # 2: special case, all zeros 

    if set(S) == {'0'}:
        return "0"

    #3: find largest digit to put in middle

    middle = ""

    for digit in range(9, -1, -1): # decrement from 9
        digit_str = str(digit)
        # if odd freq, only one
        if digit_str in freq and freq[digit_str] % 2 == 1: 
            middle = digit_str
            freq[digit_str] -= 1 # mark used
            break



    # 4 build first half of palindrome, put largest digits first to maximize, then just reverse for other half

    half = []
    for digit in range(9, -1, -1):
        digit_str = str(digit)
        # skip zeros if at start
        if digit == 0 and not half:
            continue
        
        if digit_str in freq:
            # see number of pairs
            pairs = freq[digit_str] // 2
            half.extend([digit_str] * pairs) # add digits to half

    
    # 5 no pairs, no middle, just return max digit
    if not half and not middle:
        for digit in range(9, -1, -1):
            if str(digit) in freq:
                return str(digit)   


    # just build palindrome
    palindrome = "".join(half) + middle + "".join(half[::-1])

    return palindrome

  


