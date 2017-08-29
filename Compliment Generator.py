#!/usr/bin/python
from Words import *
from random import randint
from Tkinter import *

# Set up main window settings
master = Tk()
master.title ("Compliment Generator")
width  = 450
height = 150
master.minsize (width, height)
master.maxsize (width, height)

def femaleOption():
    maleCheckbox.deselect()

def maleOption():
    femaleCheckbox.deselect()

# Create label
nameLabel = Label(master, text = "Name (optional): ")
nameLabel.pack()

# Create name entry box
nameTextEntry = Entry(master, justify = 'center')
nameTextEntry.pack()

#Create female checkbox
femaleIsChecked = IntVar()
femaleCheckbox = Checkbutton(master, text = "Female", command = femaleOption, variable = femaleIsChecked)
femaleCheckbox.select()
femaleCheckbox.pack()

#Create male checkbox
maleCheckbox = Checkbutton(master, text = "male", command = maleOption)
maleCheckbox.pack()

# Create label
complimentLabel = Label(master, text = "")

def PrintCompliment():
    feminineNounsOneRandInt  = randint(0, len(feminineNounsOne) - 1)
    masculineNounsOneRandInt = randint(0, len(masculineNounsOne) - 1)
    adverbsRandInt           = randint(0, len(adverbs) - 1)
    adjectiveRandInt         = randint(0, len(adjectives) - 1)
    feminineNounsTwoRandInt  = randint(0, len(feminineNounsTwo) - 1)
    masculineNounsTwoRandInt = randint(0, len(masculineNounsTwo) - 1)

    complimentText = "("

    # If no name is specified, use a default noun
    if len(nameTextEntry.get()) == 0:
        if femaleIsChecked.get():
            complimentText += feminineNounsOne[feminineNounsOneRandInt]

        else:
            complimentText += masculineNounsOne[masculineNounsOneRandInt]

    else:
        complimentText = "(" + nameTextEntry.get()

    complimentText += "), you are a(n) (" + adverbs[adverbsRandInt] + ") (" + adjectives[adjectiveRandInt] + ") ("

    if femaleIsChecked.get():
        complimentText += feminineNounsTwo[feminineNounsTwoRandInt]

    else:
        complimentText += masculineNounsTwo[masculineNounsTwoRandInt]

    complimentText += ")."

    complimentLabel.config(text = complimentText)

# Create button
complimentButton = Button(master, text = "Compliment", width="10", command = PrintCompliment)
complimentButton.pack()

complimentLabel.pack()

master.mainloop()
