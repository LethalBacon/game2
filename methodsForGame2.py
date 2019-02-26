# Ethan Hughes
# 2.22.19
import random
import time
import string
import os
import pygame, sys
from pygame.locals import *

def add_stats(num, play): # abstraction vv
    add_strength = int(input('Strength added: '))
    while add_strength > num:
        add_strength = int(input('Strength added: '))
    add_health = int(input('Health added: '))
    while add_health + add_strength != num:
        add_health = int(input('Health added: '))
    play.damage += add_strength
    play.health += add_health
    print(play)

class Gladiator:                # Only available class, everyone will be a Gladiator
    def __init__ (self, name, strength, health):
        self.name = name
        self.damage = strength
        self.health = health
        self.move = 'stun'
        self.level = 1

    def attack(self, other_guy):            # attack process
        other_guy.health -= self.damage
        print('{} has attacked {}!'.format(self.name, other_guy.name))

    def stun(self, other_guy):              # special move, happens when you type 3 during battle
        print('{} has stunned {}'.format(self.name, other_guy.name))
        other_guy.damage = 0
        print(other_guy)

    def __str__(self):                      # this is what is returned when print(player) happens
        return'{} {}: {} health, {} damage'.format(self.level, self.name, self.health, self.damage)

class bug:                                  # only enemy class
    def __init__(self, rond):
        self.damage = random.randint(1,7 + rond)        # the enemy damage will go up according to the round number, and will be random
        self.name = 'bug'
        self.health = 8 + rond - self.damage            # the enemy health is just based on damage, the bug stats start by being = 15, scaling up by rond(3) each defeat

    def attack(self, other_guy):            # enemy attack process, they have a 50/50 chance to land an attack
        if random.randint(0,1) == 0:
            other_guy.health -= self.damage
            print('{} has attacked you player!'.format(self.name))
            print(other_guy)
        else:
            print('{} attack has failed!'.format(self.name))

    def __str__(self):
        return'*A {} appears with {} health, and can deal {} damage!*'.format(self.name, self.health, self.damage)


