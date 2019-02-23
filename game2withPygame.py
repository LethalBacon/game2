# Ethan Hughes
import random
import time
import string
import os
import pygame

def add_stats(num): # abstraction vv
    add_strength = input('Strength added: ')
    while add_strength > num:
        add_strength = input('Strength added: ')
    add_health = input('Health added: ')
    while add_health + add_strength != num:
        add_health = input('Health added: ')
    player.damage += add_strength
    player.health += add_health
    print(player)

class Gladiator:                # Only available class, everyone will be a Gladiator
    def __init__ (self, name):
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
    def __init__(self):
        self.damage = random.randint(1,7 + rond)        # the enemy damage will go up according to the round number, and will be random
        self.name = 'bug'
        self.health = 8 + rond - self.damage            # the enemy health is just based on damage, the bug stats start by being = 15, scaling up by rond(3) each defeat

    def attack(self, other_guy):            # enemy attack process, they have a 50/50 chance to land an attack
        if random.randint(0,1) == 0:
            other_guy.health -= self.damage
            print('{} has attacked you player!'.format(self.name))
            print(player)
        else:
            print('{} attack has failed!'.format(self.name))

    def __str__(self):
        return'*A {} appears with {} health, and can deal {} damage!*'.format(self.name, self.health, self.damage)

print('You have 10 points to spend, spend on strength and health, Player')
strength = input('strength: ')
while(strength < 0 or strength > 10):           # while the strength is above 10 or under 0, just re ask the question
    strength = input('strength: ')

if(strength != 10):
    health = input('health: ')
    while(health < 0 or health > 10 or health + strength != 10):        # while the strength + health is not equal to 10, re ask, or if healh is above 10 or under 0
        print('Your total status points must add up to 10')
        health = input('health: ')
else:
    print('All stregth, sounds good!')          # if someone wants to be all strength then they need health, a bit of a secret, helps this player out a bit
    health = 2

player = Gladiator('Player 1')                  # this is the process of adding the player to the class
print(player)
print('You may now add 5 more stats')
add_stats(5)                                    # first use of add_stats, bring the player total up to 15, or if all strength 17

num_enemies = random.randint(5,10)              # random amount of enemies selected
rond = 0
print('For round 1 you will have {} enemies'.format(num_enemies))
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')        # clears the terminal so that the battle happens on a new screen
cooldown = False                                # initalizing the cooldown variable for the special move
print('Welcome to the battle Player!')
print('You can only do your special once per round!')
print('If you do run from the fight, you will not level up!')

# Algorithim VV

while num_enemies != 0 and player.health > 0 :          # while the player is alive, or there are more bugs to fight keep this loop going
    bug1 = bug()                                        # creates a random bug
    past_health = bug1.health
    print('You have {} bugs left!\n'.format(num_enemies))
    print(bug1)
    print(player)

    while bug1.health > 0 and player.health > 0:
        if random.randint(0,1) == 1:                    # 50/50 chance between you staring and bug starting
            print('Your atttack!')
            num_of_action = input('You can either 1. attack (damage vs bug health), 2. run 3. {}  ||  choose the corresponding number\n'.format(player.move))
            while num_of_action > 3 or num_of_action <1:
                num_of_action = input('Please enter a valid number: ')  # if you enter an invaild number the program wont end luckily
            if num_of_action == 1 or num_of_action == 3:
                if num_of_action == 1:
                    player.attack(bug1)
                elif num_of_action == 3 and cooldown == False:          # cooldown has to be False in order to do your special attack
                    print('Player stuns the bug, putting its damage to 0!')
                    player.stun(bug1)
                    cooldown = True
                else:
                    print('You are still on cooldown, you cannot use your special move again this round')
                    print('Preforming regular attack')
                    player.attack(bug1)
                if bug1.health > 0:
                    print('bug now has {} health left!'.format(bug1.health))
                    print('bug will now try to attack you player!')
                    time.sleep(5)
                    bug1.attack(player)
                else:
                    print('You have squashed the bug!\n')

            else:
                print('Player attempts to run from the bug')    # random chance 50/50 to run away from the bug
                if random.randint(1,2) == 1:
                    print('Player succesfully espaces!')
                    break
                else:
                    print('Player did not escape, must fight the bug!')
                    bug1.attack(player)
        else:
            print('bug is attacking!')
            time.sleep(4)
            bug1.attack(player)


    if player.health > 0:
        if num_of_action != 2:      # if you beat the bug, and you didn't run you absorb half the health of the bug
            print('You now absorb the {} life force from the bug'.format(past_health))
            add_stats(past_health)
            rond += 3               # the bugs stats will now be equal to 18, 21, 24, 27, 30, etc.
        num_enemies -= 1
        alive = True

    else:
        print('You have died X)!')
        print('I would try again if I were you')
        alive = False

if alive == True:
    print(player)
    print('Nice job getting to level {}!'.format(player.level))
    print('Very nice job! I will add more later, thanks for playing though!')