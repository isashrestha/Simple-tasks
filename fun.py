def vowel_count(word):
    vowels = 0
    for i in word:
        if(i == "a" or i =="e" or i == "i" or i == "o" or i == "u"):
            vowels = vowels + 1;
    return vowels

word = "watermelon"
print(vowel_count(word))




     
        
    
    
    