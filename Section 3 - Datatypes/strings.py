### Strings

#### quotes for strings
test_var = 'Test 1'
test_var2 = "Test 2"
print(test_var)
print(test_var2)

#### quotes inside of strings
test_var3 = 'He said "This was great"' # using the other type of quotation marks
test_var4 = '\"\'' # escape character in front of characters to treat as strings

#### escape characters
test_var5 = 'Line 1: some text \nLine 2: some more text' # multiple lines within one string
test_var5b = '\tTab this line' # add a tab within a string
print(test_var5)
print(test_var5b)

#### multiple lines
'''A comment'''
test_var6 = '''A string
on multiple 
lines'''
print(test_var6)

####math and strings
test_var7 = 'hello' + ' World'
print(test_var7)
test_var8 = 'copy' * 10 # repeats copy 10 times
print(test_var8)

####how to get variables values into strings
name = 'Gojo'
age = 28
greeting_string = 'Hello {one}, you are {two} years old'.format(one=name, two=age) # format method; not many people use this
greeting_string_better = f'Hello {name}, you are {age} years old' # f-string
print(greeting_string)
print(greeting_string_better)

#### Exercise
X = 'Gojo'
Y = 'teaching'
exercise_string = f'Hello, my name is {X} \nand my hobby is {Y}'
print(exercise_string)