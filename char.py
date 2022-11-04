# author = Isha Shrestha
# Program to check given character is a vowel or consonant

character = input ("Enter a character = ")
#taking user input
ch=character.lower() #using lower() method 
if ch.isdigit():
    print("invalid character")    
elif (character == "a" or character == "e" or character == "i" or  character == "o" or character == "u" ):
    print(character, "is Vowel")
else:
    print(character, "is Consonant")

    