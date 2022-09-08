import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_urls = pattern.sub(r'\2\3', urls)
subbed_urls = pattern.sub(r'\2\3', urls)
# subbed_urls = pattern.finditer(urls)

# for match in subbed_urls:
#     print(match.group(2))
print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))
