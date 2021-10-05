# Working List¶
# Make a list that includes four careers, such as 'programmer' and 'truck driver'.
# Use the list.index() function to find the index of one career in your list.
# Use the in function to show that this career is in your list.
# Use the append() function to add a new career to your list.
# Use the insert() function to add a new career at the beginning of the list.
# Use a loop to show all the careers in your list.
careers = ['programmer','truck driver','soccer player','golfer']
print(careers.index('programmer'))
print('programmer' in careers)
careers.append('dog walker')
careers.insert(0,'snail walker')
for i in careers:
    print(i)
    