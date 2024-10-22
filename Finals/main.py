import random

#Hangman Art - Marcus D
escii_art = {0: ("   ",
                 "   ",    
                 "   ",),
             1: (" o ",
                 "   ",    
                 "   ",),
             2: (" o ",
                 " |  ",    
                 "   ",),
             3: (" o ",
                 "/| ",    
                 "   ",),
             4: (" o ",
                 "/|\\",    
                 "   ",),   
             5: (" o ",
                 "/|\\",    
                 "/ ",),      
             6: (" o ",
                 "/|\\",    
                 "/ \\",)}



#Wordlist that computer chooses a word randomly- Sebastian M || 
wordBank=["womp","hawktuah","hello","sigma"]
selected_Word ="placeholder"
rand = random.randint(1,4)

if rand == 1:
    selected_Word = "womp"
elif rand ==2:
    selected_Word = "hawktuah" #"selected_Word" is the var for the randomly generated word that is to be guessed
elif rand ==3:
    woselected_Wordrd = "hello"
elif rand ==4:
    selected_Word = "sigma"

#Show man based of amount of wrong guesses - Marcus D
print("*************")
def hang_man(wrong_guesses):
  for line in escii_art:
    print(line)
print("*************")

#Generate word - Sebastian


#Show line for each letter in the random word "_" - William M 


#Checks if the letter exists in the word - William M

#Win/lose statement - Ryker R 
winOrLose = "Win" 

if winOrLose == "Win": 
    print ("YOU WIN!")
else: print("You Lose!")
#Show the answer whether you win or lose - Ryker R

print(selected_Word)








