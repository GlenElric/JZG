import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
background = "light grey"
timeleft = 60
highest_score = 0  # New variable to store the highest score

def startGame(event):
    if timeleft == 60:
        countdown()
    nextColour()

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        highscore()

def nextColour():
    global score, highest_score
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))
    else:
        scoreLabel.config(text="Time is up! Your score is " + str(score))
        highscore()  # Call the highscore function

def highscore():
    global score, highest_score
    if score > highest_score:
        highest_score = score
        highscoreLabel.config(text="New highscore: " + str(highest_score))  # Update the label text
    else:
        highscoreLabel.config(text="Highscore: " + str(highest_score))  # Update the label text

def restartGame():
    global score, timeleft
    score = 0
    timeleft = 60
    scoreLabel.config(text="Press enter to start")
    timeLabel.config(text="Time left: " + str(timeleft))
    label.config(text="")
    e.delete(0, tkinter.END)
    highscoreLabel.config(text="Highscore: " + str(highest_score))

root = tkinter.Tk()
root.title("Color Game")
root.geometry("800x600")

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                            font=('Times New Roman', 24), padx=10, pady=10, justify='center')
instructions.pack(anchor='center')

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Times New Roman', 24), padx=10, pady=10)
scoreLabel.pack(anchor='center')

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Times New Roman', 24), padx=10, pady=10)
timeLabel.pack(anchor='center')

label = tkinter.Label(root, font=('Times New Roman', 40), padx=10, pady=10)
label.pack(anchor='center')

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

# Add a label for displaying the highest score
highscoreLabel = tkinter.Label(root, text="Highscore: " + str(highest_score), font=('Times New Roman', 24), padx=10, pady=10)
highscoreLabel.pack(anchor='center')

# Add a restart button
restartButton = tkinter.Button(root, text="Restart", command=restartGame)
restartButton.pack(anchor='center')

root.mainloop()
