import random
import time
import winsound



def hangman(n:int):
    '''this function recives the body part number and print the body parts till that body part numgber'''
    print()
    bodyparts = ['  0\n',"/","   \\\n","  |\n","/","   \\"]
    for i in range(n):
        print(bodyparts[i],end="")
    print()

def dash_for_words_initial(word:str):
    '''this prints _ for each letter of word only initially afterwards dashes are handles by other functions'''
    wordlen = len(word)
    for l in range(wordlen):
        print("_",end="")
    print()

def game_system(word:str):
    ''' this control all the system of the game'''
    dash_for_words_initial(word)
    dict={}
    for letter in word:
        if letter.lower() in dict:
            dict[letter.lower()][1] +=1
            letter = letter.lower() + str(dict[letter.lower()][1]) 
            dict[letter.lower()] = ['_',0]
        else:
            dict[letter.lower()] = ['_',0]
     
    wrong_guess = 0 
    while True:
        letter_guess = input("\nGuess the letter of the word: ")
        print()
        letter_guessed = 0
        for key in dict:
            if letter_guess.lower() in key.lower():
                dict[key][0] = letter_guess
                letter_guessed += 1
        if letter_guessed == 0:
                wrong_guess += 1
       
        for letter in dict:
                print(dict[letter][0], end="")
        if wrong_guess == 6:
            print()
            winsound.PlaySound("R:/CodeWorkspace/My Python/Projects/sounds/thunder.wav",winsound.SND_ASYNC)
            hangman(wrong_guess)
            typewrittereffect("The word was: "+word,0.07)
            return False
        
        word_guessed = ''
        for letter in dict:
            word_guessed = word_guessed + dict[letter][0].lower()
        if word_guessed.lower() == word:
            return True
        
        print()    
        hangman(wrong_guess)

def random_word_generator(words:list):
     '''returns a random word out of the list of the words'''
     random_index = random.randint(0,len(words)-1)
     return words[random_index]     

def typewrittereffect(s:str, t:float):
    print()
   
    for letters in s:
        
        print(letters, flush = True,end='')
        time.sleep(t)
    print()

        


words = ["about", "above", "across", "after", "again", "almost", "along", "always", "another", "answer",
    "apple", "around", "artist", "auntie", "balance", "banana", "because", "before", "behind", "believe",
    "below", "between", "black", "blanket", "board", "bottle", "bridge", "brinjal", "brother", "building",
    "butter", "camera", "careful", "centre", "chair", "class", "cloud", "coffee", "college", "computer",
    "country", "cricket", "culture", "curry", "dance", "dinner", "doubt", "driver", "during", "early",
    "earth", "eight", "eleven", "enough", "evening", "family", "father", "friend", "garden", "glasses",
    "global", "ground", "happy", "holiday", "honest", "hospital", "important", "india", "jacket", "jungle",
    "kitchen", "language", "learn", "letter", "lights", "listen", "little", "market", "matter", "medicine",
    "memory", "million", "morning", "mother", "music", "native", "natural", "nephew", "nothing", "number",
    "office", "orange", "people", "picture", "please", "police", "project", "question", "really", "respect",
    "school", "science", "sister", "simple", "station", "student", "teacher", "telephone", "thousand", "today"]  

'''Below is the Starting screen of the game'''
typewrittereffect("<Imagine the written text as the voice of a woman announcer>",0.06)

welcome_message = "Welcome to the Game of Hangman"
typewrittereffect(welcome_message,0.07)

rules ='''Here are the rules of the game:
RULES:1. You will be provided with a random word
2. You have to guess the word by guessing each letter of the word. Simple right!
3. Just there is a Catch! Every wrong guess forms one part of the:'''
typewrittereffect(rules, 0.07)

typewrittereffect("HANGMAN!",0.3)
winsound.PlaySound("R:/CodeWorkspace/My Python/Projects/sounds/thunder.wav",winsound.SND_ASYNC)
hangman(6)

time.sleep(2)
rules_continue ="""4. Don't let that ever happen!
5. The safety of the world is now in your hands. SAVE US!"""
typewrittereffect(rules_continue,0.07)

typewrittereffect("Let's get Started with the Game :)\n",0.07)
game_over = False
while game_over == False:
    word = random_word_generator(words)  
    game = game_system(word)
    if game == True:
        print()
        typewrittereffect("OH Gosh! That was a intense game. YOU SAVED US!",0.07)
        typewrittereffect("There are many more HANGMAN! coming up around the world. Wanna try beat them!",0.07)
        
    elif game == False:
        print()
        typewrittereffect("YOU FAILED US!",0.1)
        typewrittereffect("TRY AGAIN?",0.07)
    
    
    while True:
        tryagain = input("Y/N: ")
        if tryagain.lower() == 'y':
            typewrittereffect("Here is your new challenge:", 0.05)
            break
        elif tryagain.lower() =='n':
            typewrittereffect("No problem.Thanks for your service ;)",0.08)
            game_over = True
            break
        else:
            typewrittereffect("Please enter a valid input :(",0.08)
        






     

