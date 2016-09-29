open_input = open('pattern_count_input.txt')
text = open_input.read().rstrip().replace(" ", "")
pattern = "CGGCGGGAGAT"

from timeit import timeit

def pattern_search_one(text, pattern):
    count = 0
    for i, nucleotide in enumerate(text):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return (count)
#pattern_search_one:47.08834998100065
#3

def pattern_search_two(text, pattern):
    return (text.count(pattern))
#pattern_search_two:0.8119574589945842
#3

def pattern_search_three(text, pattern):
    match = []
    if pattern in text:
        match.append("yes")
    if not match:
        return ("No pattern found in text.")
    else:
        return ("Pattern found in text.")
#pattern_search_three:0.704544401000021
#Pattern found in text.

def pattern_search_four(text, patern):
    match = text.find(pattern)
    if match > -1:
        return ("Pattern found in text.")
    else:
        return ("Pattern not found in text.")
#pattern_search_four:0.900490316998912
#Pattern found in text.


# print ("pattern_search_one:{}".format(timeit(
#                                     "pattern_search_one(text, pattern)",
#                                     "from __main__ import pattern_search_one;"
#                                     "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
#                                     "pattern='TTCCGG' ")))
# print (pattern_search_one(text, pattern))

# print ("pattern_search_two:{}".format(timeit(
#                                     "pattern_search_two(text, pattern)",
#                                     "from __main__ import pattern_search_two;"
#                                     "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
#                                     "pattern='TTCCGG' ")))
# print (pattern_search_two(text, pattern))

# print ("pattern_search_three:{}".format(timeit(
#                                     "pattern_search_three(text, pattern)",
#                                     "from __main__ import pattern_search_three;"
#                                     "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
#                                     "pattern='TTCCGG' ")))
# print (pattern_search_three(text, pattern))

# print ("pattern_search_four:{}".format(timeit(
#                                     "pattern_search_four(text, pattern)",
#                                     "from __main__ import pattern_search_four;"
#                                     "text='TGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGG';"
#                                     "pattern='TTCCGG' ")))
# print (pattern_search_four(text, pattern))