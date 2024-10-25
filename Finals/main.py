
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
wordBank = ["apple","cheese","computer","teacher","idyllic","pear","milk","keyboard","pencil"
         ,"positive","rambutan","yogurt","mouse","notebook","exhilaration","kiwi","butter"
         ,"motherboard","chromebook","enthralled","banana","whey","ram","desk","vivacious"
         ,"octopus","supermarket","gloves","yellow","couch","rabbit","hospital","pants"
         ,"blue","chair","doe","school","shoes","red","painting","jellyfish","church"
         ,"shirt","green","table","guitar","grandma","badminton","skin","eyes","violin"
         ,"uncle","basketball","lungs","nose","glockenspiel","mother","baseball","heart"
         ,"mouth","gobbledegook","pneumonoultramicroscopicsilicovolcanoconiosis","squid"]

##Show man based of amount of wrong guesses - Marcus D
def hang_man(wrong_guesses):
  for line in ascii_art[wrong_guesses]:
    print(line)

#Mechanism of lines for the start of the game "_" - William M 
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

#Makes sure the input is a single letter - Group
      if len(guess) != 1 or not guess.isalpha():
         print("Input is invalid. Please try again")
         continue

#Makes sure the guess doesn't count in the set of guessed letters. - William M
      
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
#Main function call that tells the computer the program needs to wait for inputs and give specific details. Basically a single-player game mechanism - Marcus D
if __name__ == "__main__":
    main()