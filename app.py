from random import choice

def draw_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |      
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |      
        """
    ]
    
    print(stages[6-tries])






word_list = ["apple", "banana", "cherry", "grape", "orange", "pear", "kiwi", "pineapple", "strawberry", "blueberry"]
word = choice(word_list)
blank = []
try_= 6

for i in word: # to fill the blank
    blank+='-'


# print(word)

while  try_:
    if '-' in blank:
        draw_hangman(try_)
        u =  input("enter :  ")
        
        for i in range(len(word)):
            if u[0] == word[i]:
                blank[i] = u[0]
        
        if not(u[0] in word):
                try_-= 1
                
        print(blank)
    
    else:
        print("you won")
        break
    
if try_ == 0:
    draw_hangman(try_)
    print("Game Over")
    
