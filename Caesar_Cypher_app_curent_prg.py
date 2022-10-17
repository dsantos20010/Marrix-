import string
from tkinter import END

alphabets = string.ascii_lowercase + string.ascii_lowercase

#loop while user did not chose to EXIT


what_to_do = input(
    'enter encrypt to ENCRYPT, decrypt to DECRYPT, exit to EXIT the program \n').lower()

sentence=''
#end_program = (what_to_do == 'EXIT')

while not what_to_do == 'EXIT':
   
    # if we already data
    #check if we ant to use existing data
    if(len(sentence)):
        
        use_existing = input('use existing data: Y or N?')
        
       
        
        if(use_existing.find('N')!= -1):
            #get text
            sentence = list(input('enter your text: \n').lower())
            #get key
            shift_number = int(input('enter your shift number from 1 to 25: \n'))
        
   
           
    else:
        #get text
        sentence = list(input('enter your text: \n').lower())
        #get key
        shift_number = int(input('enter your shift number from 1 to 25: \n'))
        # search through the enter text
    if what_to_do == 'encrypt':
        #user wants to encrypt
      

        for i in range(len(sentence)):
            # get the position of each character within the sentence
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        # convert the list back to a string
        print(''.join(map(str, sentence)))
        #end_program = Trueen
        
       # decrypt_existing = list(input('Decrypt existing text? Y/N \n').lower())
        
        #if(decrypt_existing == 'N'):
         #   sentence = list(input('enter your text: \n').lower())
        #    shift_number = int(input('enter your shift number from 1 to 25: \n'))
        
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                sentence[i] = alphabets[new_letter]
            # convert the list back to a string
        print(''.join(map(str, sentence)))
        #end_program = True
    else:
        decide = input(
            'invalid entry, try again Y for YES, N for NO: \n').lower()
        if decide == 'y':
            sentence = list(input('enter your text: \n').lower())
            what_to_do = input(
                'enter encrypt to ENCRYPT, decrypt to DECRYPT, exit to EXIT the program \n').lower()
            shift_number = int(input('enter your shift number from 1 to 25: \n'))
        #else: 
           # end_program = True
    
    what_to_do = input(
    'enter encrypt to ENCRYPT, decrypt to DECRYPT, exit to EXIT the program \n').lower()
    
    
list("Program exiting")