from stages import stages


def start_game(word: str) -> bool:
    letters = tuple(word)
    triesLeft = len(stages) - 1
    currentTry = 0

    for letterIndex, letter in enumerate(letters):
        while triesLeft > 0:
            print("\n" + stages[currentTry])

            tryInput = ''
            while not tryInput:
                tryInput = input("Enter the letter: ")

            tryLetter = tryInput[0]

            if tryLetter == letter:
                if (letterIndex < len(letters) - 1):
                    print(u"\U0001f389" + " Good. Next letter?")
                break
            else:
                currentTry += 1
                triesLeft -= 1
                print(u"\U0001f480" + " Wrong. Try once more.")

    print(f"\nWord to guess was: {word}")

    return triesLeft > 0


word = ''
while not word:
    word = input(u"\U0001f680" + " What word shall we guess? ")

print("\n" * 100)

if start_game(word):
    print(u"\U0001f389" + " YOU WON. CONGRATULATIONS!")
else:
    print(stages[-1])
    print(u"\U0001f480" + " GAME OVER. YOU LOST!")
