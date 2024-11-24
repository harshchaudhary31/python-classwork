filename = "example.txt"


file = open(filename, "w")

dataString = "Some Dummy text to be entered here \n with a new line \n after \t a tab "

fileContent = file.write(dataString)

file.close()
