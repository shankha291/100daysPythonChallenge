import random
print("Welcome to the Hangman game")
stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    '''
]
lives=5
word_list = [
    "python",
    "java",
    "javascript",
    "c",
    "cpp",
    "csharp",
    "php",
    "typescript",
    "ruby"
]

chosen_word=random.choice(word_list)
placeholder=""
word_len=len(chosen_word)
for i in range(word_len):
    placeholder+="_"
print(placeholder)  
game_over=False
list1=[]
while not game_over: 
    guess=input("You have to guess a popular programming language!!Guess a letter:").lower()
    string1 = ""   
    for letter in chosen_word:
        if(letter==guess):
            string1+=letter
            list1.append(guess)
        elif letter in list1:
            string1+=letter
        else:
            string1+="_"
    print(string1)
    if guess not in chosen_word:
        lives-=1
        if(lives==0):
            game_over=True
            
    if "_" not in string1:
        game_over=True
    print(stages[lives])
    if game_over==True:
        print("OOPs!!Play again")