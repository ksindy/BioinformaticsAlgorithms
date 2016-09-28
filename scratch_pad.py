
open_input = open('pattern_count_input.txt')
text = open_input.read().rstrip().replace(" ", "")
pattern = "CGGCGGGAGAT"

from timeit import timeit
import re


def pattern_find_one(text, pattern):
    list = []
    for i, nucleotide in enumerate(text):
        if text[i:i+len(pattern)] == pattern:
            list.append(i)
    return (list)
# pattern_find_one:41.1288166979939
# [215, 257, 361]


def pattern_find_two(text,pattern):
    matches = re.finditer('(?={0})'.format(pattern),text)
    positions = [str(match.start()) for match in matches]
    result = ' '.join(positions)
    return(result)
#pattern_find_two:15.497524202990462
#215 257 361


def pattern_find_three(text,pattern):
    results = []
    regex_pattern = re.compile('(?={0})'.format(pattern))
    matches = regex_pattern.finditer(text)
    for match in matches:
        results.append(match.start())
    return(results)
# pattern_find_three:11.731942209997214
# [215, 257, 361]


print ("pattern_find_one:{}".format(timeit(
                                    "pattern_find_one(text, pattern)",
                                    "from __main__ import pattern_find_one;"
                                    "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
                                    "pattern='TTCCGG' ")))

print ("pattern_find_two:{}".format(timeit(
                                    "pattern_find_two(text, pattern)",
                                    "from __main__ import pattern_find_two;"
                                    "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
                                    "pattern='TTCCGG' ")))

print ("pattern_find_three:{}".format(timeit(
                                    "pattern_find_three(text, pattern)",
                                    "from __main__ import pattern_find_three;"
                                    "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
                                    "pattern='TTCCGG' ")))
