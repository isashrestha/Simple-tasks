#author = Isha Shrestha
#To count the number of vowel in given character.

word = input ("Enter a word = ") #taking user input

vowels = 0
consonants = 0
word = word.lower() #using lower() method
for i in word: #looping through a string
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" ):
        vowels = vowels+1;
    else:
        consonants = consonants+1;
    
print("Total number of vowels= ", vowels) # print total number of vowels
print("Total number of consonants= ", consonants)


    

    
    
    
    
    
