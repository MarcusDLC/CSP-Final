
import random

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
wordBank = ["monitor","functions","fan","sdcard","software","hardware","programming","python","expressions","loops"]

##Show man based of amount of wrong guesses - Marcus D
print("*************")
def hang_man(wrong_guesses):
  for line in ascii_art:
    print(line)
print("*************")

#Show line for each letter in the random word "_" - William M 
def lines(hint):
   print(" ".join(hint))

#Answer line for end of the game - Group
def solution(selected_Word):
   print(" ".join(selected_Word))

#List of variables - Marcus D
def main():
   selected_Word = random.choice(wordBank)
   hint = ["_"] * len(selected_Word)
   wrong_guesses = 0
   guessed_letters = set()
   Running = True

#Starting game code, like the lines and user input - Marcus D
   while Running == True:
      hang_man(wrong_guesses)
      lines(hint)
      guess = input("Enter a letter:").lower()
#What is it? I finished and am trying to help here but how do you even check for letters? What do you mean and where?
#im still trying to figure out the other one, are we just using a set word bank?
#will the final one use a set wordbank? Yea we can just find one off the internet, but I'll ask if we can, if not, we can use a small list
#'requirements are: 
#A variable
#2 Functions
#A conditional -- did yall see what the teacher did? look at the board we need to make a variable for letters.
#I GOT IT WE NEED TO MAKE THE USERINPUT INTO A VAARI AND CHECK IF ITS IN Selectedword FAX 
#where is the userinput? IDK Line CHAT LET ME COOK NOW :fire:  :fire: marcus save our stuff
#Checks if the letter exists in the word - William M
      if guess in selected_Word:
        for i in range(len(selected_Word)):
            if selected_Word[i] == guess:
                hint[i]= guess
        else:
           wrong_guesses +=1
#what happened to my code down here
#Win/Lose statement for whether you win or lose the game - Ryker R
        if "_" not in hint:
           hang_man(wrong_guesses)
           solution(selected_Word)
           print("YOU WIN!")
           Running - False
        elif wrong_guesses >= len(hang_man) - 1:
           hang_man(wrong_guesses)
           solution(selected_Word)
           print("You lose. :(")
           Running = False
           





