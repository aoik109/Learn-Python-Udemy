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

############## PART 2 - SLICING ##################
## Slicing
# arr[1:3] -> select the elements from 1 up to 3 (not including)4
test_list = [1,2,3,4]
print(test_list[1:4]) # we want elements of index 1,2,3

## Direction of slicing
test_list2 = [1,2,3,4,5,6,7,8,9,10]
print(test_list2[1:3:1]) ##positive direction 1->3 by 1
print(test_list2[0:8:2]) ##picking every second value starting from index 0
print(test_list2[9:0:-2]) ##from index 9 (val = 10) to (not including) index 0
print(test_list2[-1:4:-1]) ##print 10->6

## leaving slicing values empty
default_slicing = test_list2[::] ## start = 0, end = len-1, by=1
print(default_slicing)

## EXERCISE
exercise_slice = test_list2[7:0:-2]
print(exercise_slice)

## tuple_slicing
test_tuple = (1,2,3,4,5,6,7,8,9,10)
print(test_tuple[0:5:3])