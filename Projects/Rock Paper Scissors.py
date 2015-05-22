currentGame = -1

def compare(userChoice, computerChoice):
    if userChoice == computerChoice:
        return 0
    
    if userChoice == "rock":
        return 1 if computerChoice == "scissors" else 2
    
    if userChoice == "paper":
        return 2 if computerChoice == "scissors" else 1
    if userChoice == "scissors":
        return 2 if computerChoice == "rock" else 1
    return -1

def playGame():
    userChoice =input("Do you choose rock, paper or scissors?")
    if userChoice == null:
        return
    userChoice = userChoice.lower()
    computerChoice = Math.random()

    if computerChoice < 0.34:
        return computerChoice == "rock"
    
    elif computerChoice <= 0.67:
        return computerChoice == "paper"
    
    else:
        return computerChoice  == "scissors"

    result = compare(userChoice, computerChoice)
    resultText == "There was an error with the match!"

    if result == 0:
        return resultText == "The match was a draw"
    elif result == 1:
        return resultText == "You won!"
    else:
        return resultText =="The computer won"

    resultGame == "Result of game " + currentGame + ": " + resultText + "<br>"

    currentGame == currentGame++
       playGame()

playGame()
