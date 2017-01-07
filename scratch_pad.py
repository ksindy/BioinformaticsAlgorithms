open_input = open('pattern_count_input.txt')
text = open_input.read().rstrip().replace(" ", "")
len_kmer = 7
max_mismatch = 3
k = 2
pattern = 'AGT'
import re

text = 'aaaaCAGaaaaaaaaG'
pattern = 'CAG'
pattern_found = [4,9]
bold = '<\b>'

# new_string = ''
# if pattern_found:
#     for i, base in enumerate(text):
#         new_string+=base
#         if i == pattern_found[0]:
#             new_string+=bold
#
#     print(new_string)


def mismatch (string1, string2):
    mismatches = 0
    for (nucleotide1, nucleotide2) in zip(string1, string2):
        if nucleotide1 != nucleotide2:
            mismatches += 1
    return(mismatches)

def approximate_patterns(text, pattern, max_mismatches):
    pattern_matches = ''
    pattern_start = 0
    pattern_end = 0
    for i, base in enumerate(text):
        query_pattern = text[i:i+len(pattern)]
        if mismatch(pattern, query_pattern) <= max_mismatches:
            pattern_matches += '<b>'
            pattern_start = i
            pattern_end = i + len(pattern)
        if i == pattern_end and pattern_start != 0:
            pattern_matches +='</b>'
            pattern_start = 0
            pattern_end = 0
        pattern_matches += base
    return(pattern_matches)

print(approximate_patterns(text,pattern,0))



# number = 7107
# len_pattern = 9
#
# from timeit import timeit
#
# def number_to_symbol(symbol):
#     dict_symbol = {0:'A', 1:'C', 2:'G', 3:'T'}
#     return dict_symbol[symbol]
#
# def remainder_symbol(div):
#     remainder = int(str(div).split('.')[1])
#     dict_remainder = {0:'A', 25:'C', 5:'G', 75:'T'}
#     last_symbol = dict_remainder[remainder]
#     return last_symbol
#
# def number_to_pattern(number, len_pattern):
#     sequence = ''
#     for len in range(len_pattern,0,-1):
#         if len == 0:
#             first_symbol = number_to_symbol(number)
#             sequence += first_symbol
#         else:
#             div = number/4
#             symbol = remainder_symbol(div)
#             sequence += symbol
#             len_pattern -= 1
#             number = int(str(div).split('.')[0])
#     return sequence[::-1]
# print(number_to_pattern(number, len_pattern))
# #number_to_pattern(number, len_pattern):8.712004325992893
#
#
# def numberToPattern (number, length):
#     letter_value = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
#     sequence = ''
#     for i in range(length):
#         ## take the remainder after dividing by 4, convert it to a base and prepend to sequence
#         sequence = letter_value[number % 4] + sequence
#         ## now do a floor division to get ready for the next base
#         number = number // 4
#     return sequence
# print(numberToPattern(number, len_pattern))
# #numberToPattern(number, len_pattern):0.7155352020054124
#
#
# print ("number_to_pattern(number, len_pattern):{}".format(timeit(
#                                     "number_to_pattern(number, len_pattern)",
#                                     "from __main__ import number_to_pattern;"
#                                     "number = 7187;"
#                                     "len_pattern = 9;"
#                                     , number =100000)))
#
# print ("numberToPattern(number, len_pattern):{}".format(timeit(
#                                     "numberToPattern(number, len_pattern)",
#                                     "from __main__ import numberToPattern;"
#                                     "number = 7187;"
#                                     "len_pattern = 9;"
#                                     , number =100000)))
# import itertools
# from timeit import timeit
# def symbol_to_number(symbol):
#     dict_symbol = {'A':0, 'C':1, 'G':2, 'T':3}
#     return dict_symbol[symbol]
#
# def pattern_to_number(pattern):
#     if not pattern:
#         return 0
#     symbol = pattern[-1]
#     prefix = pattern[0:-1]
#     return 4*pattern_to_number(prefix) + symbol_to_number(symbol)
#
# print(pattern_to_number(pattern))
# # pattern_to_number (pattern):1.215484529006062
#
# def pattern_to_number_two (pattern):
#     s = pattern
#     m = { "A" : "00", "C" : "01", "G" : "10", "T" : "11" }
#     return int("".join([m[c] for c in s]), 2)
# print(pattern_to_number_two(pattern))
# #pattern_to_number_two(pattern):0.5483961829959298
#
# def patternToNumber (pattern):
#     letter_value = {'A':0, 'C':1, 'G':2, 'T':3}
#     total = 0
#     for i in range(len(pattern)):
#         ## grab the letters from the rear ([-(i+1)]) for increasing i's and
#         ## multiply it's value by the position it's in
#         total += letter_value[pattern[-(i+1)]] * len(letter_value)**(i)
#     return total
# #patternToNumber(pattern):1.1557979640056146
#
# def patternToNumber2(dna):
#     crumb = dict(zip('ACGT', '0123'))
#     return int("".join(crumb[i] for i in dna), 4)
# #patternToNumber2(pattern):0.9234875129986904
#
# print ("pattern_to_number (pattern):{}".format(timeit(
#                                     "pattern_to_number (pattern)",
#                                     "from __main__ import pattern_to_number;"
#                                     "pattern = 'ATTCTGGA';"
#                                     , number =100000)))
#
# print ("pattern_to_number_two(pattern):{}".format(timeit(
#                                     "pattern_to_number_two(pattern)",
#                                     "from __main__ import pattern_to_number_two;"
#                                     "pattern = 'ATTCTGGA';"
#                                     , number =100000)))
#
# print ("patternToNumber(pattern):{}".format(timeit(
#                                     "patternToNumber(pattern)",
#                                     "from __main__ import patternToNumber;"
#                                     "pattern = 'ATTCTGGA';"
#                                     , number =100000)))
#
# print ("patternToNumber2(pattern):{}".format(timeit(
#                                     "patternToNumber2(pattern)",
#                                     "from __main__ import patternToNumber2;"
#                                     "pattern = 'ATTCTGGA';"
#                                     , number =100000)))

    # for i in range(len(pattern)):
    #     symbol = pattern[i+len(pattern)-1:i+len(pattern)]
    #     prefix = pattern[i:i+len(pattern)-1]
    #     print (prefix)

    # for i, nucleotide in enumerate(pattern):
    #     print(i, nucleotide)
    #     symbol = nucleotide
    #     print (symbol)



# def computing_frequencies(text, k):
#     for i in range(4**k+1):
#         i = 0
#     for i in enumerate(text):
#         pattern = text[i:i+k]
# computing_frequencies(text, k)

#
# def mismatch (string1, string2):
#     mismatches = 0
#     for (nucleotide1, nucleotide2) in zip(string1, string2):
#         if nucleotide1 != nucleotide2:
#             mismatches += 1
#     return(mismatches)
#
# def reverse_complement_four(text):
#     text = text[::-1].upper().replace(' ','')
#     reverse_complement_text = text.translate(str.maketrans('ACGT','TGCA'))
#     return reverse_complement_text
#
# def frequent_kmers(text, len_kmer):
#     frequent_kmer = []
#     dict_combinations = {}
#     for product in itertools.product(['A','T','C','G'], repeat=len_kmer):
#         dict_combinations["".join(product)] = 1
#     for i in range(len(text)-len_kmer+1):
#         pattern = text[i:i+len_kmer]
#         rc_pattern = reverse_complement_four(pattern)
#         for k, v in dict_combinations.items():
#             if mismatch(pattern, k) <= max_mismatch:
#                 dict_combinations[k] += 1
#             if mismatch(rc_pattern, k) <= max_mismatch:
#                 dict_combinations[k] += 1
#     for key, value in dict_combinations.items():
#         max_value = dict_combinations.get(max(dict_combinations, key=dict_combinations.get))
#         if value == max_value:
#             frequent_kmer.append(key)
#     return frequent_kmer
# print (frequent_kmers(text, len_kmer))


