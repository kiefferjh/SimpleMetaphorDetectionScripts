#Assignment 8

from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer

#Need a way to save to file
def saveToIntersectionFile(lineSet):
    lineString = ''.join(lineSet)
    with open('intersectionPride.txt', 'a') as file:
        file.write(lineString)

#Let's create a way to lemmatize the words we will be using, this is a function we will refer back to many times
def lemmatization(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word)

# I think we will also need a way to get rid of punctuation because when we compare words, certain words might have punctuation in them
def removePunctuation(text): #We will call this function on the whole pride and prejudice text because it returns a string and doesn't work well reading in a list
    text = re.sub(r'[^\w\s]','',text)
    return text

#We shall open our two lists of words:
#Love List
with open("loveRelatedWords.txt", 'r') as file:
    loveWords = file.read().split("\n")

#Journey List
with open("journeyRelatedWords.txt", 'r') as file2:
    journeyWords = file2.read().split("\n")

    #Let's test and see if everything looks right
#print(loveWords)
#print(journeyWords)

#We must get the sentences from pride and prejudice.
with open("pride.txt", 'r', encoding = 'utf8') as file3:
    prideWords = file3.read() #I'm not splitting it here because I want to use NLTK to tokenize it into sentences
    prideSents = sent_tokenize(prideWords)



#Now that we've opened all our files and got all our lists of word and sentences, we can go through and perform some checks
#we have a list of sentences now, but we will want to make sure each word does not have punctuation
for each_word in prideSents:
    each_word = removePunctuation(each_word) #Now the word won't have annoying punctuation
    #now we must check if the sentence has at least one word from each list
    # a fast way to do this is with a SET operation!





    if (prideSet.intersection(loveSet) and prideSet.intersection(journeySet)):
        saveToIntersectionFile(prideSet)
