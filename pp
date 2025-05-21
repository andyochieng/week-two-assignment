# Create an empty list and perform all operations
my_list = []                     # Step 1
my_list.append(10)              # Step 2
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)           # Step 3
my_list.extend([50, 60, 70])    # Step 4
my_list.pop()                   # Step 5
my_list.sort()                  # Step 6
index_of_30 = my_list.index(30) # Step 7
print("Index of 30:", index_of_30)
