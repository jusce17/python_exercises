# coding: utf-8
'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

'''
def not_string(word):
    
    if len(word) >= 3 and word[:3] == "not":
        print(word)
    else:
        print("not "+ word) 
        


