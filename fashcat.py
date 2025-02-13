#!/usr/bin/env python3

import sys
from typing import TextIO

word_list: list[str] = ['women and underrepresented', 'diversity and inclusion', 'increase the diversity',
                        'culturally responsive', 'enhance the diversity', 'fostering inclusivity',
                        'fostering inclusivity', 'cultural differences', 'indigenous community', 'community diversity',
                        'diverse backgrounds', 'diverse communities', 'enhancing diversity', 'promoting diversity',
                        'underrepresentation', 'increase diversity', 'race and ethnicity', 'sense of belonging',
                        'sexual preferences', 'cultural heritage', 'diverse community', 'equal opportunity',
                        'hispanic minority', 'racial inequality', 'under appreciated', 'under represented',
                        'black and latinx', 'community equity', 'diversity equity', 'gender diversity',
                        'gender diversity', 'racial diversity', 'underrepresented', 'implicit biases', 'biases towards',
                        'discrimination', 'discriminatory', 'diverse groups', 'racial justice', 'social justice',
                        'biased toward', 'discriminated', 'diverse group', 'implicit bias', 'inclusiveness',
                        'institutional', 'multicultural', 'sociocultural', 'socioeconomic', 'disabilities',
                        'diversifying', 'historically', 'inequalities', 'marginalized', 'polarization', 'under served',
                        'diversified', 'hate speech', 'hate speech', 'inclusivity', 'inequitable', 'marginalize',
                        'stereotypes', 'underserved', 'undervalued', 'disability', 'inequality', 'inequities',
                        'minorities', 'privileges', 'activists', 'advocates', 'diversify', 'diversity', 'equitable',
                        'ethnicity', 'inclusion', 'inclusive', 'political', 'prejudice', 'activism', 'advocacy',
                        'advocate', 'barriers', 'equality', 'excluded', 'excluded', 'minority', 'racially', 'systemic',
                        'barrier', 'females', 'genders', 'females', 'genders', 'biased', 'biases', 'latinx', 'equity',
                        'female', 'gender', 'female', 'gender', 'racial', 'racism', 'status', 'trauma', 'victim',
                        'bipoc', 'black', 'women', 'lgbt', 'dei']

def process_line(line: str):
    lowercase_line = line.lower()
    for word in word_list:
        pos:int = lowercase_line.find(word)
        while pos >= 0:
            redact:str = '█' * len(word)
            line = line[:pos] + redact + line[pos+len(word):]
            lowercase_line = lowercase_line[:pos] + redact + lowercase_line[pos + len(word):]
            pos = lowercase_line.find(word)
    print(line)


def process_stream(stream:TextIO):
    for line in stream:
        process_line(line.strip())

if len(sys.argv) > 1:
    process_stream(open(sys.argv[1], 'r'))
else:
    process_stream(sys.stdin)
