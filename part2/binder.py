import os
import sys
from subprocess import call
import os
from subprocess import Popen, PIPE

# The file name
FILE_NAME = "codearray.h";

###########################################################
# Returns the hexidecimal dump of a particular binary file
# @execPath - the executable path
# @return - returns the hexidecimal string representing
# the bytes of the program. The string has format:
# byte1,byte2,byte3....byten,
# For example, 0x19,0x12,0x45,0xda,
##########################################################
def getHexDump(execPath):

	# The return value
	retVal = None

	process = Popen(["/usr/bin/hexdump", "-v", "-e", '"0x" 1/1 "%02X" ","', execPath], stdout=PIPE)
	(output, err) = process.communicate()
	exit_code = process.wait()
	if exit_code == 0:
		retVal = output

	return retVal


###################################################################
# Generates the header file containing an array of executable codes
# @param execList - the list of executables
# @param fileName - the header file to which to write data
###################################################################

def generateHeaderFile(execList, fileName):

	# The header file
	headerFile = None

	# The program array
	progNames = sys.argv

	# Open the header file
	headerFile = open(fileName, "w")

	# The program index
	progCount = 0

	# The lengths of programs
	progLens = []

	# Write the array name to the header file
	headerFile.write("#include <string>\n\nusing namespace std;\n\nunsigned char* codeArray[" + str(len(execList)) + "] =\n{");

	firstValue = True
	for progName in execList:
		if progCount != 0:
			headerFile.write(",\n")
		value = getHexDump(progName)
		if value == None:
			print("Error getting Hex dump for " + progName)

		numBytes = value.count(',')

		progLens.append(numBytes)
		progCount += 1

		headerFile.write("new unsigned char[" + str(numBytes) + "]{")
		if value[-1] == ',':
			value = value[:-1]
		value = value.replace(",", ", ")
		headerFile.write(value)
		headerFile.write("}")
	headerFile.write("\n};")

	# Write for programLengths
	headerFile.write("\n\nunsigned programLengths[" + str(len(execList)) + "] = {")
	for i in range(len(execList)):
		if i != 0:
			headerFile.write(", ")
		headerFile.write(str(progLens[i]))
	headerFile.write("};")


	# Write the number of programs.
	headerFile.write("\n\n#define NUM_BINARIES " +  str(len(progNames) - 1))

	# Close the header file
	headerFile.close()


############################################################
# Compiles the combined binaries
# @param binderCppFileName - the name of the C++ binder file
# @param execName - the executable file name
############################################################
def compileFile(binderCppFileName, execName):

	print("Compiling...")

	process = Popen(["g++", binderCppFileName, "-o", execName,
	"-std=gnu++11"], stdout=PIPE)
	(output, err) = process.communicate()
	print(output)
	exit_code = process.wait()
	if exit_code == 0:
		print("Compilation succeeded")
	else:
		print("Compilation failed")

generateHeaderFile(sys.argv[1:], FILE_NAME)
compileFile("binderbackend.cpp", "bound")
