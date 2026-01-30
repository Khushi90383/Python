#1st way of reversing String
original_string="Hello world"
reversed_string=original_string[::-1]
print(reversed_string)

# 2nd Way of reversing String
original_string="Hello World"
reversed_string="".join(reversed(original_string))
print(reversed_string)


