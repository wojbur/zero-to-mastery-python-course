import re

# At least 8 char long
# contains any letters, numbers, $%#@
# has to end with a number

email = 'andrei@yahoo.com'
password = 'heeeeeflsjjnfopisjf!@#$eeee1'

email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_regex = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
check1 = email_regex.search(email)
check2 = password_regex.search(password)

print(check1)
print(check2)
