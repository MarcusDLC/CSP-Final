
import random
 
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


#Wordbank - Sebastian
wordBank = ["monitor","functions","fan","sdcard","software","hardware","programming","python","expressions","loops"]

##Show man based of amount of wrong guesses - Marcus D
def hang_man(wrong_guesses):
  for line in ascii_art[wrong_guesses]:
    print(line)

#Show line for each letter in the random word "_" - William M 
def lines(hint):
   print(" ".join(hint))

#Answer line for end of the game - Group
def solution(selected_Word):
   print(" ".join(selected_Word))

#List of variables and starting game mechanism - Marcus D
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
      guess = input("Enter a letter: ").lower()

#Makes sure the input is a single letter - Marcus D.
      if len(guess) != 1 or not guess.isalpha():
         print("Input is invalid.")
         continue

#Makes sure the guess doesn't count in the set of guessed letters.
      
      if guess in guessed_letters:
        print(f"{guess} was already guessed. Try another input")
        continue
      
      guessed_letters.add(guess)
      
#Checks if the letter exists in the word - William M 
      if guess in selected_Word: 
            for i in range(len(selected_Word)):
                if selected_Word[i] == guess: 
                    hint[i]= guess
      else:
        wrong_guesses +=1
#Win/Lose statement for whether you win or lose the game - Ryker R
      if "_" not in hint:
           hang_man(wrong_guesses)
           solution(selected_Word)
           print("YOU WIN!")
           Running = False

      elif wrong_guesses >= 6:
           hang_man(wrong_guesses)
           solution(selected_Word)
           print("You lose. :(")
           Running = False 

if __name__ == "__main__":
    main()