# Exercises
# Mountain Heights
# Wikipedia has a list of the tallest mountains in the world, with each mountain's elevation. Pick five mountains from this list.
# Create a dictionary with the mountain names as keys, and the elevations as values.
# Print out just the mountains' names, by looping through the keys of your dictionary.
# Print out just the mountains' elevations, by looping through the values of your dictionary.
# Print out a series of statements telling how tall each mountain is: "Everest is 8848 meters tall."
# Revise your output, if necessary.
# Make sure there is an introductory sentence describing the output for each loop you write.
# Make sure there is a blank line between each group of statements.
mtn_elevation = {'Everest': '8848','K2': '8611','Manaslu': '8163','Annapurna': '8091','Cho Oyu': '8188'}

for key in mtn_elevation.keys():
    print(key)

for value in mtn_elevation.values():
    print(value)

for key in mtn_elevation.keys():
    print("%s is %s meters tall." % (key, mtn_elevation[key]))
