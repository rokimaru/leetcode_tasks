"""
 * Написать функцию которая считает кол-во символов в строке, встречающихся более 1 раза
 * Вернуть кол-во этих символов
 *
"""

import collections


def count_repeated_symbols(s):
    count = 0
    dict = collections.Counter(s)
    for key in dict:
        if dict[key] > 1:
            count += 1
    return count


print(count_repeated_symbols("aaaabbc"))
print(count_repeated_symbols("abbc"))
print(count_repeated_symbols("abbbc"))
print(count_repeated_symbols("abbccc"))
print(count_repeated_symbols("aabac"))



