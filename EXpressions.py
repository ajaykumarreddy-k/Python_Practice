import re
#code for regular expressions to extract email addresses from a string
'''text = "Emails:test@example.com,hello.world@company.org"
# Regular expression to match email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# Find all email addresses in the text
emails = re.findall(email_pattern, text)
# Print the list of email addresses
print("Extracted emails:", emails)'''
# matching the two strings in regular expressions
'''     
text1 = "Hello Python"
texxt2 = "programming Hello World"
pattern = r"Hello" 
match1 = re.match(pattern, text1)
print(f"Match1{text1}: {match1.group() if match1 else "None"}")
match2 = re.match(pattern, texxt2)
print(f"Match2{texxt2}: {match2.group() if match2 else "None"}")
# Using re.search to find the first occurrence of "Hello" in the string
'''
