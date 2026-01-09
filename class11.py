#  List is a mutable collection of items in Python
#  list is mutable nature 
# my_list = [10, 20, 30, 40, 50]

# We can store anithing in list
# my_list = [10, "Hello", 45.67, True, None]

# we can have duplicate values in list
# my_list = [10, 20, 30, 20, 10, 40]

# We can access list items by index
# print(my_list[0])  # 10

# List is mutable that means we can change its items
# my_list[1] = 25
# print(my_list)  # [10, 25, 30, 40, 50]




# # ========== List Slicing and Indexing ==========
# my_list = [10, 20, 30, 40, 50]

# print(my_list[0])  # 10
# print(my_list[2])  # 30
# print(my_list[-1]) # 50





# Deep, reference and Shallow copy in list
# Deep, reference and Shallow copy in list

# reference copy
# a = [10,20,30,40,50]

# b = a

# b[0] = 100

# print(a)
# print(b)

# shallow copy
# a = [10,20,30,40,50]

# b = a.copy()

# b[0] = 100

# print(a)
# print(b)


# import copy
# # deep copy
# a = [[10,20],
#      [30,40]]

# b1 = a.copy()  # shallow copy
# b2 = copy.deepcopy(a)  # deep copy

# b1[0] [0] = 1000
# b2[1] [1] = 4000

# print(a)
# print(b1)
# print(b2) 



# # ========== List treversing ==========
# # treversing a list using for loop
# # ========== mothod 1: ==========

# my_list = [10, 20, 30, 40]

# for i in range(len(my_list)):
#     print(my_list[i] )





# # ========== list methods : ==========
# append(), 
# insert(), 
# extend(), 
# remove(), 
# pop(), 
# clear(), 
# index(), 
# count(), 
# sort(), 
# reverse()

my_list = [10, 20, 30, 40 , 10 , 10 ,  20]

print(my_list.count(10))  # count occurrences of 10 in the list


# my_list.append(50) # append 50 at the end
# my_list.clear() # remove all items from the list
# my_list.insert(1, 25) # insert 25 at index 1
# my_list.remove(30) # remove 30 from the list
# my_list.pop() # remove last item from the list
# print(my_list.count(10)) # count 10 in the list
# my_list.sort() # sort the list
# my_list.reverse() # reverse the list
# my_list.extend([50, 60, 70]) # extend the list by adding multiple items
# print(my_list) 

