import random
import Words from hangman_words

#Wordlist that computer chooses a word randomly- Sebastian M || 
 

#Hangman Art - Marcus D
ascii_art = {0: ("   ",
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


#wordbank and selected word - sebastian
wordBank=["monitor","functions","fan","sdcard","software","hardware","programming","python","expressions","loops"]
selected_Word ="placeholder" # this is going to be answer 

##Show man based of amount of wrong guesses - Marcus D
print("*************")
def hang_man(wrong_guesses):
  for line in ascii_art:
    print(line)
print("*************")

#List of variables - Marcus D
def main():
   selected_Word = random.choice(wordBank)
   hint = ["_"] * selected_Word 
   wrong_guesses = 0
   guessed_letters = set()
   Running = True

   while Running == True:
      hang_man(wrong_guesses)
      lines(hint)
      guess = input("Enter a letter:").lower()

      if guess in selected_Word:
         
         
    


#Show line for each letter in the random word "_" - William M 
        Length = len(
  selected_Word
        )
        print("_ " * Length)
    


#Checks if the letter exists in the word - William M

#What is it? I finished and am trying to help here but how do you even check for letters? What do you mean and where?
#im still trying to figure out the other one, are we just using a set word bank?
#will the final one use a set wordbank? Yea we can just find one off the internet, but I'll ask if we can, if not, we can use a small list
#'requirements are: 
#A variable
#2 Functions
#A conditional -- did yall see what the teacher did? look at the board we need to make a variable for letters.
#I GOT IT WE NEED TO MAKE THE USERINPUT INTO A VAARI AND CHECK IF ITS IN Selectedword
    print ("YOU WIN!")
else: print("You Lose!")
#Show the answer whether you win or lose - Ryker R

print(selected_Word)








