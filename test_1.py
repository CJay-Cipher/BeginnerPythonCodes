"""Capital indexes

Write a function named capital_indexes. The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]."""

def capital_indexes(strng):
    na = []
    for new in strng:
        if new.isupper() == True:
            na.append(strng.index(new))
    return na
print(capital_indexes("HaLoW"))