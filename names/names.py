import time

from bst import BSTNode


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
bst_1 = BSTNode(names_1)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
bst_2 = BSTNode(names_2)
f.close()

# bst_1.in_order_print()

duplicates = bst_1.find_duplicates(bst_2) #first_list.get_duplicates(second_list)  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements # this is O(n^2)
# The only way to make this a log n or even o(1) (hash map) is to be able to divide a list kinda sort of like a binary tree
# for name_1 in names_1:
#     for name_2 in names_2:
# # 


# so only return the duplicates

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
