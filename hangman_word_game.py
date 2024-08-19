## Hangman Word Game
import os
def clear ():
    os.system('cls')

oneWrong = """
1 wrong!

|
|
|
|
|
|
|
"""
twoWrong = """
The stage is set for hanging.

|=============
|
|
|
|
|
|
"""
threeWrong = """
The rope is set.

|=============
|      |
|
|
|
|
|
"""
fourWrong = """
Everything is set now.

|=============
|      |
|      |
|     ===
|
|
|  ||`````||
"""
fiveWrong = """
You are set now. You still have time.

|=============
|      |
|    (^_^)
|     ---
|    <`|`>
|     |`|
|  ||`````||
"""
sixWrong = """
The rope is tightened. Your last chance to stay alive.

|=============
|      |
|    (^_^)
|     ===
|    <`|`>
|     |`|
|  ||`````||
"""
sevenWrong = """
You're dead! Rest in peace.

|=============
|      |
|    (^_^)
|     ===
|    <`|`>
|     |`|
|
"""
punishment = [oneWrong, twoWrong, threeWrong, fourWrong, fiveWrong, sixWrong, sevenWrong]

wordPicked = (input ("Enter the word: ")).lower()
wordPickedArray = list (wordPicked)
wordPickedArrayCopy = wordPickedArray.copy()
wordPickedArrayHidden =[]
for i in range (0, len(wordPickedArray)):
    wordPickedArrayHidden.append("_")
             
print("Alright. Now let the player play it.")

wrong = 0
chancesLeft = 7
letterFound = False
alreadyGuessed = False

for i in range (0, ((len(wordPickedArray))+chancesLeft)):
    letterPicked = input ("Guess a letter: ").lower()
    for j in range (0, len(wordPickedArray)):
        if (letterPicked == wordPickedArrayHidden[j]):
            alreadyGuessed = True
        if (letterPicked == wordPickedArray[j]):
            letterFound = True
            wordPickedArray[j] = "-"
            wordPickedArrayHidden[j] = letterPicked

    if (alreadyGuessed):
        clear()
        print (wordPickedArrayHidden)
        print ("You have already guesed it.")
        alreadyGuessed = False
        continue

    if (letterFound):
        clear()
        print("Good guess!")
        print (wordPickedArrayHidden)
        print("\n")
        letterFound = False
    else:
        wrong+=1
        chancesLeft-=1
        clear()
        print("Wrong!")
        print(wordPickedArrayHidden)
        print(punishment[wrong-1])
        print(f"{(chancesLeft)} chance(s) left.\n")

    if (wordPickedArrayCopy == wordPickedArrayHidden):
        print("Good job! You won!\n")
        break

    if (chancesLeft == 0):
        break

print(f"Given word: {wordPicked.upper()}")