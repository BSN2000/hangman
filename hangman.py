'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
from collections import Counter

somewords='''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

somewords=somewords.split(" ")

word = random.choice(somewords)

if __name__=='__main__':
    print("welcome to hangman game")
    flag = 0
    chances = len(word)+3
    letterguessed = ''
    correct = 0
    k=0
    print("Guess The Word,HINT:Its a fruit")
    for i in range(len(word)):
        print("_",end = " ")
    print()
    try:
        while(chances!=0) and flag==0 :
            chances -= 1
            print()
            
            
            try:
                guess = str(input("enter a guess letter "))
            except:
                print("enter only one letter!")
                continue

            #valiadtion of the entered letter ie, is letter or not
            if not guess.isalpha():
                print("enter a letter")
                continue
            elif len(guess)>1:
                print("enter only one letter")
                continue
            elif guess in letterguessed:
                print("the letter is already guessed")
                continue

            #if the guessed letter is correct

            if guess in word:
                k = word.count(guess)
            for _ in range(k):
                letterguessed += guess

            #printing the guessed letter

            for ch in word:
                if ch in letterguessed and (Counter(letterguessed)!=Counter(word)):
                    print(ch,end=" ")
                    correct+=1
                #if user guess all letter letters correctly with left chances
                elif(Counter(letterguessed)==Counter(word)):
                    print("the word is ",end = " ")
                    print(word)
                    flag=1
                    print("you won")
                    break#breaking the for loop
                    break#breaking the while loop
                else:
                    print("_",end=" ")

        #if user exhaust all moves
        if chances<=0 and (Counter(letterguessed)!=Counter(word)):
            print()
            print("sorry you have exhausted all your chances")
            print("the word was",word)
    except KeyboardInterrupt:
        print()
        print("try again")
        exit()