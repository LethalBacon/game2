# Ethan Hughes
# 2.22.19
import random
import time
import string
import os
from pygame.locals import *
from methodsForGame2 import add_stats, Gladiator, bug

print('You have 10 points to spend, spend on strength and health, Player')
strength = int(input('strength: '))
while(strength < 0 or strength > 10):           # while the strength is above 10 or under 0, just re ask the question
    strength = int(input('strength: '))

if(strength != 10):
    health = int(input('health: '))
    while(health < 0 or health > 10 or health + strength != 10):        # while the strength + health is not equal to 10, re ask, or if healh is above 10 or under 0
        print('Your total status points must add up to 10')
        health = int(input('health: '))
else:
    print('All stregth, sounds good!')          # if someone wants to be all strength then they need health, a bit of a secret, helps this player out a bit
    health = 2

player = Gladiator('Player 1', strength, health)                  # this is the process of adding the player to the class
print(player)
print('You may now add 5 more stats')
add_stats(5, player)                                    # first use of add_stats, bring the player total up to 15, or if all strength 17

num_enemies = random.randint(5,10)              # random amount of enemies selected
rond = 0
print('For round 1 you will have {} enemies'.format(num_enemies))
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')        # clears the terminal so that the battle happens on a new screen
cooldown = False                                # initalizing the cooldown variable for the special move
print('Welcome to the battle Player!')
print('You can only do your special once per round!')
print('If you do run from the fight, you will not level up!')
while num_enemies != 0 and player.health > 0 :          # while the player is alive, or there are more bugs to fight keep this loop going
    bug1 = bug(rond)                                        # creates a random bug
    past_health = bug1.health
    print('You have {} bugs left!\n'.format(num_enemies))
    print(bug1)
    print(player)

    while bug1.health > 0 and player.health > 0:
        if random.randint(0,1) == 1:                    # 50/50 chance between you staring and bug starting
            print('Your atttack!')
            num_of_action = int(input('You can either 1. attack (damage vs bug health), 2. run 3. {}  ||  choose the corresponding number\n'.format(player.move)))
            while num_of_action > 3 or num_of_action <1:
                num_of_action = int(input('Please enter a valid number: '))  # if you enter an invaild number the program wont end luckily
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
            add_stats(past_health, player)
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