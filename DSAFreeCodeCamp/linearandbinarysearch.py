"""
1. State the problem clearly. Identify the input & output formats
2. Come up with some example inputs and outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem in english
4. Implement the solution and test using outputs. Fix bugs
5. Analayze the algorithm's complexity and identify inefficiencies 
6. Overcome inefficiencies with correct technique 
7. Repeat steps 3-6
"""

"""
Question 1: Alice has some cards with numbers written on them. She arranges
the cards in decreasing oreder, and lays them out face down in a sequence on a 
table. She challenges Bob to pick out the card containing a given number by
turning over as few cards as possible. Write a function to help Bob locate the card.

[13, 11, 10, 7, 4, 3, 1, 0]

"""
# ===============================
# STEP 1: State problem & format
# ===============================
"""
Problem:
    We need to write a program to find the position of a given number in a list of
    numbers arranged in decreasing order. We also need to minimize the number of 
    times we access elements from the list.

"""
# ===============================
# STEP 2: Example input and output
# ===============================
"""
Input:
    1) cards: A list of numbers sorted in decreasing order. E.g.[13, 11, 10, 7, 4, 3, 1, 0]
    2) query: A number, whose position in the array is to be determined E.g. 7

Output:
    3) postions: The position of 'query' in the list 'cards' E.g. '3' in the above case (counting from 0)
"""

def locate_card(cards, query):
    pass

"""
Tips:
    * Name the function and think carefully about the psuedocode (signature)
    * Discuss the problem with the interviewer if you're unsure how to frame it in abstract terms
    * Use descriptive variable names
"""

# === TEST CASE ===
# test = {
#     'input': {
#         'cards': [13, 11, 10, 7, 4, 3, 1, 0],
#         'query': 7
#     },
#     'output': 3
# }

# locate_card(**test['input']) == test['output']

# Edge cases

"""
1. 'query' occurs in middle of list 'cards'
2. 'query' is the first element in 'cards'
3. 'query' is the last element in 'cards'
4. list 'cards' contains just one element, which is 'query'
5. list 'cards' does not contain 'query'
6. list 'cards' is empty
7. list 'cards' contains repeating numbers
8. 'query' occurs more than once in 'cards'
9 ???
"""
 
# ===============================
# STEP 3: Solution for the problem in English
# ===============================

"""
Brute Force
1. Create a variable 'position' with the value 0
2. Check wether the number at the index 'position' in card equals 'query'
3. If it does, 'position' is the answer and can be returned from the function
4. If not, increment the value of 'position' by 1, and repeat steps 2 to 5 till we reach 
the last position
5. if the number wasn't found, return -1
"""

def locate_card(cards, query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1

# https://www.youtube.com/watch?v=pkYVOmU3MgA
# 32:33