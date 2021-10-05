# Multiples of Ten
# Make a list of the first ten multiples of ten (10, 20, 30... 90, 100).
# There are a number of ways to do this, but try to do it using a list comprehension.
# Print out your list.

multiplesOfTen = []
for number in range(1,11):
    multiplesOfTen.append(number*10)
for number in multiplesOfTen:
    print(number)

## or:
# multTen = [number*10 for number in range(1,11)]
#
# for i in multTen:
#     print(i)
