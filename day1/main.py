import re

def replace_spelled_digits(line):
    replacements = {
        'one' : 'on1e', 
        'two' : 'tw2o', 
        'three' : 'thr3e',
        'four': 'fo4ur', 
        'five':'fi5ve',
        'six': 'si6x',
        'seven': 'sev7en',
        'eight' : 'ei8ght',
        'nine':'ni9ne'
        }
    for word, digit in replacements.items():
        line = line.replace(word, digit)
    return line

values = []

with open("day1.txt") as file:
    for line in file:
        values.append(line.rstrip())

total_sum = 0

for line in values:
    # r3pl4c3 w1th numb3r
    line = replace_spelled_digits(line)
    
    # 3xtr4ct d1g1t
    digits_only = re.sub('\D', '', line)
    
    if digits_only:
        total_sum += int(digits_only[0] + digits_only[-1])

print("Sum:", total_sum)
