"""
Given a string, e.g "elephant"
Write a program (function) to find the first unique character in this string

"elephant" -> 'l'
"maggie" -> "m"
"""

def findUniqueChar(word):
    for c in word:
        if word.count(c) == 1:
            return c

#print(findUniqueChar("elephant")) 