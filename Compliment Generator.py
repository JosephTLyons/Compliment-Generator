#!/usr/bin/python
from random import randint
from Tkinter import *

# Set up main window settings
master = Tk()
master.title ("Compliment Generator")
master.resizable (width = False, height = False)
width  = 400
height = 120
master.minsize (width, height)
master.maxsize (width, height)

# Words
nouns      = "Baby", "Honey", "Love", "Sweety", "Pumpkin", "Boo-Boo", "Bae", "Girl", "Dearest", "Bbgrl", "Sugar"
adverbs    = "super", "extremely", "very", "especially", "really", "perfectly", "completely", "entirely", "incredibly"
adjectives = "sexy", "beautiful", "astonishing", "fabulous", "extraordinary", "gorgeous", "independent", "glowing", \
             "responsible", "passionate", "kind", "caring", "impressive", "marvelous", "stupendous", "confident", \
             "courageous", "perfect", "honest", "charismatic", "breathtaking", "classy", "affectionate", "compassionate", \
             "resourceful", "swag-tastic", "cooperative", "exuberant", "productive", "stellar", "divine", "adventurous", \
             "fearless", "gregarious", "rational" , "sincere" , "witty", "versatile", "sociable", "pro-active", "practical", \
             "optimistic", "loyal", "imaginative", "humorous", "fearless", "dynamic", "determined", "diligent", "courteous", "reasonable"
nounsTwo   = "duck", "girl", "woman", "princess", "queen", "daisy", "invdividual", "intellect", "tulip", "koala bear", \
             "sex symbol", "specimen", "mermaid", "watermelon", "goose", "being", "goddess", "savant", "companion", \
             "baby-maker", "heart-throb", "citizen", "genius", "baller", "badass", "marsupial", "unicorn"

# Create label
nameLabel = Label(master, text = "Name: ")
nameLabel.pack()

# Create name entry box
nameTextEntry = Entry(master, justify = 'center')
nameTextEntry.pack()

# Create label
complimentLabel = Label(master, text = "")

def PrintCompliment():
    compliment = nameTextEntry.get() + ", you are a(n) (" + adverbs[randint(0, len(adverbs) - 1)] \
                 + ") (" + adjectives[randint(0, len(adjectives) - 1)] + ") (" + nounsTwo[randint(0, len(nounsTwo) - 1)] + ")."

    complimentLabel.config(text = compliment)

# Create button
buttonThing = Button(master, text="Compliment", width="10", command=PrintCompliment)
buttonThing.pack()

complimentLabel.pack()

master.mainloop()
