#!/usr/bin/python
from Words import *
from random import randint
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
        self.female_checkbox = Checkbutton(self.master, text="Female", variable=self.female_is_checked)
        self.female_checkbox.select()

        self.male_checkbox = Checkbutton(self.master, text="Male")

        self.female_checkbox.config(command=self.male_checkbox.deselect)
        self.male_checkbox.config(command=self.female_checkbox.deselect)

        self.compliment_button = Button(self.master, text="Compliment", width="10", command=self.print_compliment)
        self.compliment_label = Label(self.master, text="", width=50)

    def add_gui_components_to_window(self):
        self.name_label.grid(row=1, column=1, columnspan=2)
        self.name_text_entry.grid(row=2, column=1, columnspan=2)

        self.female_checkbox.grid(row=3, column=1)
        self.male_checkbox.grid(row=3, column=2)

        self.compliment_button.grid(row=4, column=1, columnspan=2)
        self.compliment_label.grid(row=5, column=1, columnspan=2)

    def print_compliment(self):
        feminine_nouns_one_rand_int = randint(0, len(feminine_nouns_one) - 1)
        feminine_nouns_two_rand_int = randint(0, len(feminine_nouns_two) - 1)

        masculine_nouns_one_rand_int = randint(0, len(masculine_nouns_one) - 1)
        masculine_nouns_two_rand_int = randint(0, len(feminine_nouns_two) - 1)

        adverbs_rand_int = randint(0, len(adverbs) - 1)
        adjective_rand_int = randint(0, len(adjectives) - 1)

        if self.female_is_checked.get():
            noun_one = feminine_nouns_one[feminine_nouns_one_rand_int]
            noun_two = feminine_nouns_two[feminine_nouns_two_rand_int]
        else:
            noun_one = masculine_nouns_one[masculine_nouns_one_rand_int]
            noun_two = feminine_nouns_two[masculine_nouns_two_rand_int]

        if len(self.name_text_entry.get()) != 0:
            noun_one = self.name_text_entry.get()

        compliment_text = "({}), you are a(n) ({}) ({}) ({}).".format(
            noun_one,
            adverbs[adverbs_rand_int],
            adjectives[adjective_rand_int],
            noun_two
        )

        self.compliment_label.config(text=compliment_text)


ComplimentGenerator()
