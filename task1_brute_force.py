'''
There is a company that sells large letters made out of wood and metal (similar to the ones spelling "HOLLYWOOD"). The company is going out of business, and the owners want to sell off their remaining stock. They have listed all the remaining letters in a catalogue in a string S (in no particular order), and have advertised their "Everything must go" offer online.

Attracted by the reduced prices, Alice has decided to order some letters from the company. She wants to build as many signs with the name of her new blog as possible and place them around the city. She hasn't decided on the name of her blog yet, and is considering K different possibilities. Right now she is wondering about the maximum number of signs she can build if she chooses one of the names from her list.

Knowing the list of possible names of Alice's blog L and the company catalogue state S, find the maximum number of copies of a name from L that Alice can build.

Write a Python function:

def solution(S, L)

that, given the string S and the list L consisting of K strings, returns the maximum number of copies of a string from L that can be built only using letters from S.

Examples:
Given S = "BILLOBILLOLOBBI", L = ["BILL", "BOB"], the function should return 3. The sign "BILL" can be built three times using the letters from S and the sign "BOB" can be built only twice.

Given S = "CAT", L = ["ILOVEMYDOG", "CATS"], the function should return 0. None of the proposed names can be built using the letters from S.

Given S = "ABCDXYZ", L = ["ABCD", "XYZ"], the function should return 1. Both signs "ABCD" and "XYZ" can be built only once using the letters from S.

Assume that:
The length of string S is within the range [1..100];

K is an integer within the range [1..10];

The lengths of the strings in L are within the range [1..100];

String S is made only of uppercase letters (A-Z);

Strings in L consist only of uppercase letters (A-Z).

Notes:
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

Do you have any questions?
'''


from collections import Counter

def solution(S, L):
    # Count frequency of each letter in S
    s_freq = Counter(S)
    print(f's_freq: {s_freq}')
    
    max_copies = 0
    
    # Check each string in L
    for name in L:
        # Count frequency of each letter in the current name
        name_freq = Counter(name)
        print(f'Name: {name}, Name_freq: {name_freq}')
        
        # Calculate how many copies of the name can be made
        copies = float('inf')  # Start with infinity, find min across letters
        for char, count in name_freq.items():
            if char not in s_freq:
                copies = 0  # Cannot make any copies if a required letter is missing
                break
            # Number of copies is limited by the availability of each letter
            copies = min(copies, s_freq[char] // count)
        
        # Update max_copies if this name can be made more times
        max_copies = max(max_copies, copies)
    
    return max_copies



# Example inputs from the problem statement
example1_S = "BILLOBILLOLOBBI"
example1_L = ["BILL", "BOB"]
print(f'Example 1: S = {example1_S}, L = {example1_L}')
print(f"Example 1: {solution(example1_S, example1_L)}")  # Expected output: 3

'''
example2_S = "CAT"
example2_L = ["ILOVEMYDOG", "CATS"]
print(f"Example 2: {solution(example2_S, example2_L)}")  # Expected output: 0

example3_S = "ABCDXYZ"
example3_L = ["ABCD", "XYZ"]
print(f"Example 3: {solution(example3_S, example3_L)}")  # Expected output: 1

# Additional test cases
test1_S = "AAAAABBBBBCCCCC"
test1_L = ["ABC", "ABCABC", "ABCABCABC"]
print(f"Test 1: {solution(test1_S, test1_L)}")  # Should return 5 (can make 5 copies of "ABC")

test2_S = "XYZXYZXYZ"
test2_L = ["XYZ", "XY", "Z"]
print(f"Test 2: {solution(test2_S, test2_L)}")  # Should return 9 (can make 9 copies of "Z")

test3_S = "ABCDEFG"
test3_L = ["XYZ"]
print(f"Test 3: {solution(test3_S, test3_L)}")  # Should return 0 (no copies can be made)

test4_S = "AABBCC"
test4_L = ["ABC", "AABC", "AABCC"]
print(f"Test 4: {solution(test4_S, test4_L)}")  # Should return 2 (can make 2 copies of "ABC")

'''