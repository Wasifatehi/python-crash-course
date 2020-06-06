# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:08:23 2020

@author: barbora

Use a loop to see how hard it might be to win the kind of lottery modelled in
9_14. Make a list or tuple called my_ticket. Write a loop that keeps pulling 
numbers until your ticket wins. Print a message reporting how many times the 
loop had to run to give you a winning ticket.

"""

# Import choice from random module
from random import choice

# Create lists to hold my tickets and all tickets
raffle_available = [1, 5, 23, 6, 2, 7, 4, 9, 43, 54, 'e', 'g', 'c', 'd', 'm']
my_tickets = [23, 'm']

# Pull tickets until one of my tickets wins
flag = True
counter = 0
all_chosen = []
while flag:
    counter += 1
    chosen = choice(raffle_available)
    # Delete chosen value from list of all available values
    raffle_available.remove(chosen)
    all_chosen.append(chosen)
    if chosen in my_tickets:
        print("I have won!")
        print(f"It took me {counter} attempts.")
        flag = False
    
print(all_chosen)