#War Metaphor Script
#Kieffer Higgins
# Make it more efficient later!
#Imports
import os
import re
from sys import argv
#Let... argv[1] = BBC Climate Change List, argv[2] = War List, argv[3] = Intersection List
#argv[4] = bbcIntersection #argv[5] = warintersection

#///////////////////////////////////////////////////////////////////
#functions for later use:
#Saves a set that was made from a line of an article to file specified in argv[3]
def saveToIntersectionFile(line, fileName, outputFile, intersection ):
    #we had passed in a set but we can just save the line
    #lineString = ''.join(lineSet)
    intersectionString = ''.join(intersection)
    with open(outputFile, 'a', encoding = 'utf8') as file:
        try:
            file.write('Intersection: ' + intersectionString + '\t Found in ' + fileName + "\t" + line + '\n')
        except:
            print("Could not save line " + line + "To Intersection File")
#Gets BBC List from file
def getBBCList():
    with open(argv[1], 'r') as file:
        bbcList = file.read().split("\n")
        return bbcList
#Gets War List From File
def getWarList():
    with open(argv[2], 'r') as file:
        warList = file.read().split("\n")
        return warList
#After searching for spaced words in our files we then change the spaced words in the bbc list to an underscore format
def fixBBCList():
    newList = []
    with open(argv[1], 'r') as file:
        bbcList = file.read().split("\n")
        for item in bbcList:
            if " " in item:

                newItem =item.replace(" ", "_")

                newList.append(newItem)
            else:
                newList.append(item)
        #print(newList)
    return newList

#/////////////////////////////////////////////////////////////////////////////

# MAIN AREA
print("Starting Engines...")
#Let us get our BBC List and War List
bbcList = getBBCList()
warList = getWarList()


#Get all the files in genre folder (this script will be run in each folder)
files = [file for file in os.listdir() if file.endswith(".txt")]

# /////////////// REPLACE SPACES WITH UNDERSCORES //////////////////////////
        #!!!! There is an issue with this function where it still thinks it has to rename a new thing...but..it works for one run.
#For each file in files
for file in files:
    #This is a flag used for later
    deleteFlag = 0
    #Try to do the following
    #try:
        #Open the file
    with open(file, 'r', encoding = 'utf8') as openedFile:
        #We read in the file
        readFile = openedFile.read()
        #If there's a word in the file that is also in the BBC list and it contains a space...
        #if (word in openedFile for word in bbcList) and " " in word:


        #For each word in the BBC List (not the War List as it does not have any words containing a space)
        for word in bbcList:
            #We check if that word is also in our read in file and if there is a space in the word
            #We could just check for the words with spaces in them...there might be a way more efficient way to do all of this
            if (word in readFile) and " " in word:
                #If the word is in the file and has a space in it,
                    #We need to replace the space in that word in that file.

                oldWord = word
                newWord = oldWord.replace(" ", "_")

                #Then we replace our old word with our new fixed up word
                newFileContent = readFile.replace(oldWord, newWord)


                #Let us create a new name for the files which we have replaced the spaces in
                newFileName =  "[SPACE REPLACED]" + file
                #Now let's open a new file and write to it
                with open(newFileName, 'w', encoding = 'utf8') as theFileToWriteto:
                    #We write the changed underscore / space content to file
                    theFileToWriteto.write(newFileContent)
                #Now we must delete the old file
                #Let's change this flag so we can use it later
                deleteFlag = 1
        #If we have marked a file for deletion
        if deleteFlag == 1:
                #Close it and kill it.
                openedFile.close()
                os.remove(file)




    #If we can't do any of the above just move on and don't crash the program
    #except:
        #but make a note of it
      # print("Failed to open a file or replace something")
       #continue
#Replace the spaces in the words in our BBCLIST
bbcList = fixBBCList()

# ////////////////////////////////////////////////////////////

# //////////////////// CHECKING FOR INTERSECTION ///////////////////
#Make BBC list and War List into sets
bbcSet = set(bbcList)
warSet = set(warList)
#For each sentence in each genre

# We need to reestablish our file list since it has changed
files = [file for file in os.listdir() if file.endswith(".txt")]
#For each file in our list of files
for file in files:
    #try:
        #We open each file in our list of files
        with open(file, 'r', encoding = 'utf8') as openedFile:
            #Assigning the read in contents to "text file"
            textFile = openedFile.read()
            #For each line (as determined by \n char) in textFile,
            for line in textFile.split('\n'):
                #Make the sentence / line a list
                lineList = line.split()
                #then make sentence / line a set
                lineSet = set(lineList)
                #We now perform checks as to whether or not there is an intersection of sets:

                #If a set of a line has an intersection with BBC SET:
                if (lineSet.intersection(bbcSet)):
                    #Create a list of the intersecting values
                    bbcIntersectionList = list(lineSet.intersection(bbcSet))
                    #Save this line, filename and intersection to specified file (argv4)
                    saveToIntersectionFile(line, file, argv[4], bbcIntersectionList)
                #If a set of a line has an intersection with WAR SET:
                if(lineSet.intersection(warSet)):
                    #Create a list of the intersecting values
                    warIntersectionList = list(lineSet.intersection(warSet))
                    #Save this line, filename and intersection to specified file (argv5)
                    saveToIntersectionFile(line,file, argv[5], warIntersectionList)


                #If intersections are had with both: (IMPORTANT PART)
                if (lineSet.intersection(bbcSet) and lineSet.intersection(warSet)):

                    #Create a list of the intersecting words with bbcSet
                    bbcListIntersection = list(lineSet.intersection(bbcSet))
                    #Create a list of the intersecting worods with warSet
                    warListIntersection = list(lineSet.intersection(warSet))
                    #Create a new empty list
                    intersection = []
                    #Add the two lists to intersection:
                    intersection.append("[") #For ease of readability
                    intersection.extend(bbcListIntersection)
                    intersection.append("\t") #For ease of readability
                    intersection.extend(warListIntersection)
                    intersection.append("]") #For ease of readability

                    #Save this line, filename and intersection to specified file (argv3)
                    saveToIntersectionFile(line, file, argv[3], intersection)
print("Morality Deconstructed")

    #except:
        #print("Probably couldn't open a file or map a character")
        #continue
