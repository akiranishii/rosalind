import this
from collections import Counter
# Variables and Some Arithmetic
a = 3
b = 5
print(a**2 + b**2)

# Strings and lists
wordonestart = 4
wordoneend = 12
wordtwostart = 178
wordtwoend = 185

txtstr = "qKS1PhasianusJNtTV4wgxWdk6zjm4wO7SXXnTMEIZH34I5kUDn6RxzXsnMkhV3UvuYNiCROl2AIWJza2zHCNXtZ6YTILoyKUPGjXo0Knqj3kbrb197CKjvstd6YUvbRxb31YK0ReMCpMzmK4AUNniPGqeWPEMfif4tuYxlykwAtZFX5XIaltaicuss5Vafk."

print(f'{txtstr[wordonestart:wordoneend + 1]} {txtstr[wordtwostart:wordtwoend + 1]}')

# Conditions and Loops
start = 4366
end = 8860
result = 0
for x in range(start, end + 1):
    if x % 2 != 0:
        result += x
print(result)

# List comprehension method
result = sum([x for x in range(start, end + 1) if x % 2 != 0])
print(result)

# Working with Files
outputFile = []
with open('input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]

with open('output.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))

# Dictionaries

textstring = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# wordcount = {}
# for word in textstring.split(" "):
#     if word in wordcount:
#         wordcount[word] += 1
#     else:
#         wordcount[word] = 1

wordcount = Counter(textstring.split(" "))

for key, val in wordcount.items():
    print(key, val)
