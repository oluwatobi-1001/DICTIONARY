# 📖 Patience's Dictionary

A simple command-line dictionary written in Python. It shows you a list of words, and you type any word from the list to get its meaning.

Built as part of my 100 Days of Coding journey.

## Features

- Stores more than 90 words and their meanings in a Python dictionary
- Shows the full list of available words when the program starts
- Looks up a word and prints its meaning
- Works with any letter case: apple, Apple and APPLE all give the same result
- Keeps asking for new words until you decide to stop
- Tells you politely when a word is not in the dictionary

## How it works

1. The program prints a welcome message and lists every word it knows.
2. It asks you to enter a word.
3. If the word is in the dictionary, it prints the meaning and asks for another word.
4. If the word is not in the dictionary, it says sorry and asks if you want to look up another word: type 1 for yes or 0 for no.
5. Typing 0 (or anything other than 1) ends the program with "Goodbye!".

flowchart TD
    A[Start: welcome message and list of words] --> B[Enter a word]
    B --> C{Is the word in the dictionary?}
    C -->|Yes| D[Print the meaning]
    D --> B
    C -->|No| E[Sorry, that word is not in the dictionary]
    E --> F{Look up another word? 1 or 0}
    F -->|1| B
    F -->|0 or anything else| G[Goodbye!]
## Requirements

- Python 3
- No extra libraries needed

## How to run

1. Save the code as dictionary.py.
2. Open a terminal in the folder that contains the file.
3. Run:

python dictionary.py
## Example session

Welcome to Patience's Dictionary!


Here are some words you can look up:
- apple
- brave
- candle
...

Enter a word to find its meaning: Apple
Meaning: A round fruit that is usually red, green, or yellow.

Enter a word to find its meaning: banana
Sorry, that word is not in the dictionary.
Do you want to look up another word? (1/0), 1 for yes, 0 for no: 0
Goodbye!
## Words included

<details>
<summary>Click to see all the words</summary>

apple, brave, candle, dance, eagle, family, garden, happy, island, journey, knowledge, language, mountain, nature, ocean, peace, question, river, school, teacher, umbrella, victory, window, youth, zealous, ability, beautiful, courage, delight, education, freedom, generous, honest, imagination, justice, kindness, liberty, miracle, necessary, opportunity, patience, quality, respect, success, talent, understanding, valuable, wisdom, adventure, brilliant, creative, determination, energy, excellent, friendship, gratitude, happiness, inspiration, joyful, leadership, motivation, noble, optimistic, powerful, responsible, strength, trust, unique, volunteer, wonderful, achievement, balance, communication, discipline, focus, growth, hope, innovation, knowledgeable, learning, mindful, progress, resourceful, smart, thoughtful, unity, vision, ambition, confidence, empathy, curious, perseverance

</details>

## What I practised

- Dictionaries: storing words and meanings as key-value pairs
- for loops to print every word in the dictionary
- while True loops to keep the program running
- input() and print() to talk to the user
- .lower() so lookups ignore capital letters
- in to check if a word exists in the dictionary
- if, elif and else for decisions
- break to leave a loop and continue to go back to the start of it

## Author

Oluwatobi Patience Oyelude

