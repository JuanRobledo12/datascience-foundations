"""
Given a string that contains several characters in duplicate and continuous,
except one character, find the unique character within the string.

Input:
AABCCDDEEFF

Output:
B

Input:
AAB

Output:
B
"""

# Tiempo: O(N)
# Espacio: O(1)
def unique_char(word_string):
    i = 0
    for letter in word_string:
        if i == 0:
            prev_letter = letter
            i += 1 # Este lo puse abajo del continue la cague bien duro jajajaj
            continue     
        else:
            curr_letter = letter
        if curr_letter == prev_letter:
            # print("These characters are continuous")
            i = 0
        else:
            return prev_letter

    return letter

print(unique_char('AABCCDDEEFF'))
print(unique_char('AAB'))
print(unique_char('AACCBZZ'))
