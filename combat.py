import random
import math
import time
#Other files.py
import stats

def block(attacker,defender,DMG): #Block
            if random.random() <defender.BLK:
                print(f"{defender.ID} goes on guard. ",end="")
                print(f"{attacker.ID} attacks {defender.ID} for {DMG*0.5} damage.")
                defender.C_HP = max(0,defender.C_HP-(attacker.ATK*0.5))
            else:
                print(f"{attacker.ID} attacked {defender.ID} for {DMG} damage.")
                defender.C_HP = max(0,defender.C_HP-attacker.ATK)

def attack(attacker,defender): #A attacks B
    DMG=attacker.ATK
    CRIT=attacker.ATK*1.5
    EVADE=dodge(defender)
    if random.random() <attacker.ACC:
        if random.random() <EVADE:
            if random.random() <attacker.CRT:
                block(attacker,defender,CRIT)
            else:
                block(attacker,defender,DMG)
        else:
            print(f"{defender.ID} dodges.",end=" ")
    else:
        print(f"{attacker.ID} misses.",end=" ")
    print(f"{defender.ID} {defender.C_HP}/{defender.M_HP}",end="\r")

def battle(enemy): #Assumes the player enters combat
    print(f"You run into a {enemy.ID}")
    if enemy.SPD>=stats.player.SPD:
        attack(enemy,stats.player)
        if stats.player.C_HP==0:
            print("You have died.")
    while enemy.C_HP>0 and stats.player.C_HP>0:
        attack(stats.player,enemy)
        time.sleep(0.5)
        if enemy.C_HP==0:
            print(f"You slay the {enemy.ID}")
            break
        attack(enemy,stats.player)
        time.sleep(0.5)
        if stats.player.C_HP==0:
            print("You have died.")
            break
    enemy.C_HP=enemy.M_HP
    if stats.player.C_HP>0:
        stats.player.GOLD=stats.player.GOLD+enemy.GOLD
        print(f"You gained {enemy.GOLD} gold! Total Gold: {stats.player.GOLD}")
