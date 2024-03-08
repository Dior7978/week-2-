# Create an empty list
My_list = []

# Append the elements to the list
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)

# Insert the value 15 at the second position
My_list.insert(1, 15)  # Remember, Python is 0-indexed, so position 1 is the second position

# Extend my_list with another list
My_list.extend([50, 60, 70])

# Remove the last element from my_list
My_list.pop()  # By default, pop removes and returns the last item in the list

# Sort my_list in ascending order
My_list.sort()

#Find the index of 30
index = My_list.index(30)

# Find and print the index of the value 30 in my_list
print(My_list)
print(f'the index of 30 is:{index}')
