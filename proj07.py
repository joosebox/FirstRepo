##################################################################
#  Section 5
#  Computer Project #7
#  Strings, lists, files and their various operators
##################################################################

import random

def scramble_word(word_str):
    """Takes a single word from the file and returns a scrambled word
       according to the following rules
       1) First and last letter are preserved in the original positions
       2) Seems like a waste to shuffle something of length 3 or less
       3) Punctuation postions are preserved"""
    if len(word_str) > 3:
        letters_list = list(word_str)
        if letters_list[-1] = '.':
            letters_to_shuffle = letters_list[1:-2]
            random.shuffle(letters_to_shuffle)
            shuffled_str = ''.join(letters_to_shuffle)
            word_scrambled = letters_list[0] + shuffled_str + letters_list[-2] + letters_list[-1]
        letters_to_shuffle = letters_list[1:-1]
        random.shuffle(letters_to_shuffle)
        shuffled_str = ''.join(letters_to_shuffle)
        word_scrambled = letters_list[0] + shuffled_str + letters_list[-1]
    if len(word_str) <= 3:
        word_scrambled = word_str
    return word_scrambled

def scramble_line(line_str):
    """Takes an entire line of text and returns a new line with each word
    scrambled using the scarmble_word function"""
    shuffled_list = ''
    word_list = line_str.split(' ')
    for word in word_list:
        shuffled_list += scramble_word(word) + ' '
    return(shuffled_list)

def open_read_file(file_name_str):
    """Continuously prompts until it can open a file"""
    while True:
            try:
                file_obj = open(file_name_str,"r")
                break
            # If file name is incorrect, reprompt
            except IOError:
                print("Bad file name, try again")
                file_name_str = input("Open what file: ")
    return file_obj

def main():
    file_write = input('Name of file to write: ')
    fileObjOut = open(file_write,"w")
    file_read = input('Name of file to read: ')
    file = open_read_file(file_read)
    for line in file: 
        scrambled_line_str = scramble_line(line)
        fileObjOut.write(scrambled_line_str)
        
    
main()
