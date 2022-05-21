hello = 'Hello World!'
print(list(hello)) # Convert string to list
print(hello[0]) # Get first character
print(hello[-1]) # Get last character
print(hello[0:5]) # Get characters from 0 to 5

if hello.startswith('Hello'): # Check if string start with Hello
    print('Yes, the string starts with "Hello"')
else:
    print('No, it does not start with "Hello"')

if hello.isdigit(): # Check if string is digit
    print('Yes, the string is all digits')
else:
    print('No, it does not all digits')

if hello.isalpha(): # Check if string is alphabet
    print('Yes, the string is all letters')
else:
    print('No, it does not all letters')

if hello.endswith('World'): # Check ending of string
    print('Yes, the string ends with "World"')
else:
    print('No, it does not end with "World"')

print(hello.upper()) # Convert string to upper case
print(hello.lower()) # Convert string to lower case

upper_hello = hello.upper()
print(upper_hello.isupper()) # Check if string is upper case
