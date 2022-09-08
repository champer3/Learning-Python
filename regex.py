import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
pat
.at
0at

'''
sentence = 'Start a sentence and then bring it to an end Start'
group = '''
a
aa
bababab
bbb
ab
bab
bbbba
'''

# pattern = re.compile(r'^Start$')
# pattern = re.compile(r'(a.*a | b.*b | a | b)')
# pattern = re.compile(r'((a.*a)|(b.*b)|a|b)$')
pattern = re.compile(r'^[ab]$')

matches = pattern.finditer(group)

for match in matches:
    print(match)
