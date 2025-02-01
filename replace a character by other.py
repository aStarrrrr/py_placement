import re

sample = "Abhinand#$!Shaji$#"
final = re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=\w)', ' ', sample)

print(final)



# Explanation
#           (?<=\w): Ensures that the special character is preceded by a word character (A-Z, a-z, 0-9).
#           [$#!]+: Matches one or more occurrences of only the specified special characters ($, #, !).
#           (?=\w): Ensures that the special character is followed by a word character.