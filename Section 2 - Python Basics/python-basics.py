######## Code executes from top to bottom
# print("    /")
# print("  /  /")
# print("/  /  /")

######## Math operators
#power
# print(10**2) # 10^2
# #floor divide -> truncating
# print(10//3) # 3
# #mod -> remainder
# print(7%2) # 2 2 2 1 = remainder 1

######### Variables
# a container for any type of data
# result = 10 + 5
# print(result)

# #snake case
# snake_case = "variable naming convention"

# # more math operators; adding the right side to the variable
# num1=1
# num1+=5
# num1-=5
# num1*=5
# num2/=5
# print(num1)

# test_variable_snake_case = 10
# test_variable_snake_case+=20
# print(test_variable_snake_case)

########### Functions
# special commands
# print(), len(), abs()
#function(arguments)
print("test")
print(len('allison'))
print(abs(-50))
print('one', 'two')

print(max(1,100,2,400,50,20))

###### Methods
# functions that are attached to objects
print('a word'.upper())

username = 'John Smithxx'.title() # first letter uppercase
username = 'John Smith'.title().strip('x') #removes the arguments from the front/end of string
print(username)


print(dir(username)) #prints all the methods of the object