#!/usr/bin/python

import random

from words import *
from Tkinter import *


class ComplimentGenerator:
    def __init__(self):
        self.set_up_main_window()
        self.create_components()
        self.add_gui_components_to_window()

        self.master.mainloop()

    def set_up_main_window(self):
        self.master = Tk()
        self.master.title ("Compliment Generator")
        self.master.resizable(width=False, height=False)

    def create_components(self):
        self.name_label = Label(self.master, text="Name (optional): ")
        self.name_text_entry = Entry(self.master, justify="center")

        self.female_is_checked = IntVar()
        self.female_checkbox = Checkbutton(self.master, text="Female", variable=self.female_is_checked, command=self.self_female)
        self.female_checkbox.select()

        self.male_checkbox = Checkbutton(self.master, text="Male", command=self.self_male)

        self.compliment_button = Button(self.master, text="Compliment", width="10", command=self.print_compliment)
        self.compliment_label = Label(self.master, text="", width=50)

    def self_female(self):
        self.male_checkbox.deselect()
        self.female_checkbox.select()

    def self_male(self):
        self.female_checkbox.deselect()
        self.male_checkbox.select()

    def add_gui_components_to_window(self):
        self.name_label.grid(row=1, column=1, columnspan=2)
        self.name_text_entry.grid(row=2, column=1, columnspan=2)

        self.female_checkbox.grid(row=3, column=1)
        self.male_checkbox.grid(row=3, column=2)

        self.compliment_button.grid(row=4, column=1, columnspan=2)
        self.compliment_label.grid(row=5, column=1, columnspan=2)

    def print_compliment(self):
        if self.female_is_checked.get():
            noun_one = random.choice(feminine_nouns_one)
            noun_two = random.choice(feminine_nouns_two)
        else:
            noun_one = random.choice(masculine_nouns_one)
            noun_two = random.choice(masculine_nouns_two)

        if len(self.name_text_entry.get()) != 0:
            noun_one = self.name_text_entry.get()

        compliment_text = "({}), you are a(n) ({}) ({}) ({}).".format(
            noun_one,
            random.choice(adverbs),
            random.choice(adjectives),
            noun_two
        )

        self.compliment_label.config(text=compliment_text)


ComplimentGenerator()
