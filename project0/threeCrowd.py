# Three is a Crowd¶
# Make a list of names that includes at least four people.
# Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
# Modify your list so that there are only two people in it. Use one of the methods for removing people from the list, don't just redefine the list.
# Run your if test again. There should be no output this time, because there are less than three people in the list.
# Bonus: Store your if test in a function called something like crowd_test.
names = ['Jim','James','Jimbo','Jimothy']

def crowd_test(names):
    if len(names) > 3:
        print("this is too crowded")

crowd_test(names)
names.pop(1)
names.pop(2)
crowd_test(names)

