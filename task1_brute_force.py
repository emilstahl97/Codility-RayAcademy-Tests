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

    s_counter = Counter(S)

    print(f's_counter: {s_counter}')

    # check how many times each word in L can be built using letters from S

    max_copies = 0

    for word in L:
        copies = float('inf') # just set big word to compare against
        word_counter = Counter(word)
        print(f'Name {word}:')
        print(f'Frequency: {word_counter}')

        # iterate L and check how many we can build using S 

        for letter, count in word_counter.items():
            print(f'Letter {letter} occurs {count} times in {word}')
            if letter not in s_counter:
                print(f'Letter {letter} not found in S')
                # we cannot build this word, no need to check rest
                copies = 0
                break
        
            # check how many times each letter of the word occurs in S, floor it.
            # number of copies we can make is limited by the letter with fewest copies
            copies = min(copies, s_counter[letter] // count)
            print(f'Copies of word: {copies}')

        # set the word that has maximum copies

        print('set max copis for word: ' + word)
        max_copies = max(max_copies, copies)

    return max_copies


# Example inputs from the problem statement
example1_S = "BILLOBILLOLOBBI"
example1_L = ["BILL", "BOB", "test"]
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