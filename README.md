# Hangman-Game
A terminal based hangman game

Hangman Game System

A simple Python console application to play the classic game of Hangman. This script is all about bringing a dramatic, immersive feel to the terminal using timed text and custom visuals.

The Working

This Python file controls the entire Hangman experience, making sure it feels like a high-stakes, dramatic game right in your console.

The working process flows like this:

Dramatic Start: The game kicks off with a special typewrittereffect function that prints text slowly, simulating a voice. This builds the suspense and introduces the rules.

Word Prep: A word is picked at random from our generous list of 100+ words using the random_word_generator.

The Game Engine (game_system): This is where the magic happens. It handles the core guessing loop.

Letter Tracking: I used a neat trick here: a dictionary maps all the letters in the secret word. If a word has multiple of the same letter (like 'e'), the code handles it by temporarily renaming the keys (e.g., 'e' and 'e2') so every single letter position is tracked correctly.

Guessing: The user guesses a letter. If it's right, the dashes turn into the letter. If it's wrong...

The Hangman Appears: ...The wrong_guess count increases, and the hangman(n) function draws another body part on the screen, adding to the tension.

Win or Lose: If the player correctly fills in all the dashes, they win! If the count hits 6, the gallows are complete, a sound effect plays, the word is revealed, and the world is lost (until they try again).

Replay: After every game, the user can easily start a new round with a simple Y/N input.

Core Functions - The Building Blocks

Function Name

What it Does

hangman(n)

Takes the number of wrong guesses and prints the associated stick figure parts for that moment in time.

dash_for_words_initial(word)

Just prints the starting set of _ dashes before the guessing starts.

game_system(word)

The brain of the game, managing the loop, dictionary tracking, input, and win/loss checks.

random_word_generator(words)

Grabs one random word from the massive word list to start the challenge.

typewrittereffect(s, t)

Prints strings slowly to give that cinematic, announcing feel.

Future Possible Improvements

Later, we can make this project even better. The sound part is a bit tricky since winsound is only for Windows. We could definitely make it cross-platform for anyone to enjoy the full audio experience.

Also, it's just a command line app right now. It could be super cool to turn this into a proper GUI game using something like Pygame or Tkinter. That way, we get real graphics instead of just stick figures! Adding difficulty levels or maybe a high-score tracker would also be fun.
