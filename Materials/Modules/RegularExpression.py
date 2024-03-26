import re
patterns = ['term1', 'term2']
text = 'This is a string with term2, but not the other term'

# 1
# for pattern in patterns:
#     print(f"Searching for {pattern} in {text}\n")
    
#     #check for match
#     if re.search(pattern, text):
#         print("\nMatch was found\n")
#     else:
#         print("\nNo Match was found\n")

# 2
split_term = "@"
phrase = "What is your email? Ex: MallcleJoin@gmail.com"
re.split(split_term,phrase)
