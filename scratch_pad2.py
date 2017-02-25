import re
import sys

# line = sys.stdin.readlines()
# while line:
#     print (line)
#     line = sys.stdin.readline()


# for text in sys.stdin.readlines():
#     print(input(text))


# import sys
#
x, y = [int(s) for s in sys.stdin.readline().split(" ")]
input('1 0')
print(x + y)


#print (text)
# text, pattern = [str(seq) for seq in sys.stdin.readlines()]
# print(text)
#
#  def pattern_find_three(text,pattern):
#     results = []
#     regex_pattern = re.compile('(?={0})'.format(pattern))
#     matches = regex_pattern.finditer(text)
#     for match in matches:
#         results.append((match.start()+1))
#     string = ' '.join(str(i) for i in results)
#     return string
#
# print(pattern_find_three(text, pattern))