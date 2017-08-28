#!/usr/bin/python
from Words import *
from random import randint
from Tkinter import *

# Set up main window settings
master = Tk()
master.title ("Compliment Generator")
master.resizable (width = False, height = False)
width  = 450
height = 105
master.minsize (width, height)
master.maxsize (width, height)

# Create label
nameLabel = Label(master, text = "Name (optional): ")
nameLabel.pack()

# Create name entry box
nameTextEntry = Entry(master, justify = 'center')
nameTextEntry.pack()

# Create label
complimentLabel = Label(master, text = "")

def PrintCompliment():
    nounsRandInt     = randint(0, len(nouns) - 1)
    adverbsRandInt   = randint(0, len(adverbs) - 1)
    adjectiveRandInt = randint(0, len(adjectives) - 1)
    nounsTwoRandInt  = randint(0, len(nounsTwo) - 1)

    if len(nameTextEntry.get()) == 0:
        compliment = "(" + nouns[nounsRandInt]

    else:
        compliment = "(" + nameTextEntry.get()

    compliment += "), you are a(n) (" + adverbs[adverbsRandInt] \
    + ") (" + adjectives[adjectiveRandInt] \
    + ") (" + nounsTwo[nounsTwoRandInt] + ")."

    complimentLabel.config(text = compliment)

# Create button
buttonThing = Button(master, text="Compliment", width="10", command=PrintCompliment)
buttonThing.pack()

complimentLabel.pack()

master.mainloop()
