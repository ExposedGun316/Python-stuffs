original = input('Enter a word:')

if len(original) > 0 and original.isalpha(): #Making sure user selected word and make sure it is a word and not a number
    print (original)
else:
    print ('empty') #If input is a number or nothing inputed, don't continue with code

#begun, the translating has    
pyg = 'ay'
word = original.lower() #Changes word to lowercase
first = word[0]
new_word = word + first + pyg #Adds all above elements together
new_word = new_word[1:len(new_word)]#Slices word
print (new_word) #Prints the Pig Latin word
