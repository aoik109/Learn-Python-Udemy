### List and tuples
##### simple data containers

##### List [] - mutable
my_list = [1,2,3,4.5,'word']
my_list.reverse() # reverses the list
my_list.append(10)
print(my_list)
#my_list.clear() # clears the list
print(len(my_list))

##### Tuple () - immutable; a little bit faster
my_tuple = (1,2,3,4.5, 'Word', [7,8,9])
#my_tuple.append(10) # does NOT work because cannot change a tuple
#my_tuple.reverse() # does NOT work
print(my_tuple)

##### How to pick elements from a list or tuple -> Indexing or Slicing
###### each value in the list/tuple is assigned an index 0-(len-1)
##### Indexing -> lists, tuples, and strings
print(my_list[0]) # -> 'word'
print(my_tuple[5]) # -> [7,8,9]
print(my_tuple[5][0]) # 7 because [7,8,9][0]
print(my_tuple[-1]) # [7,8,9] going in the opposite direction!!!!

##### Exercise
exercise_list = ['first entry', [123,456,[0,'Hello :)']], 'bye']
print(exercise_list[1][2][1])

second_list = exercise_list[1]
second_list[0] = 890
print(exercise_list)