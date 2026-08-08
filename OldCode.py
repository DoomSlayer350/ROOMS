from random import randint
from random import choice
from time import sleep
import math
from functools import reduce
import sys
import platform
import os

"""

So from here on I commence the refactoring of my old text-based adventure game.

Here's the plan:

    - Don't change any functionality except saving to a json file instead of a csv file to gain more experience with using the json format.
    - Other than that, add clearer naming conventions
    - Split code into other files
    - Before I didn't really know how OOP worked, I think I didn't use any inheritance...
    - Ye that's it

if LibraryOfBooks took over a week and that was 400 lines of code
2500/400 = 6.25

This will take approximately 6 weeks...
and since I know I will get bored and will keep alternating between different projects, it might take a little longer than that...

"""

directions = ["N","E","S","W"]

rep_check = False

if "REPLIT_DB_URL" in os.environ:
    #print("Running in Replit")
    rep_check = True
else:
    #print("Not running in Replit")
    rep_check = False

def clear_shell():
    if rep_check == True:
        os_name = platform.system()
        if os_name == 'Windows':
            import os
            os.system('cls')  # For Windows
        else:
            import subprocess
            subprocess.call('clear', shell=True)  # For Unix/Linux
    else:
        print("\n" * 40)

def game_delay_print(string, buffer, delay):
    for letter in string:
        print("", end="", flush=True)
        if buffer == True:
            sleep(delay)
            print(letter, end="")
        else:
            sleep(delay)
            print(letter, end="")
    print()
class item:
    def __init__(self,name,equippable,equipped,spawnable,spawn_probability,item_type):
        self.name = name
        self.equippable = equippable
        self.equipped = equipped
        self.spawnable = spawnable
        self.spawn_probability = spawn_probability
        self.item_type = item_type
class armour:
    def __init__(self,body_type,defense_stats, durability, storage):
        self.body_type = body_type
        self.defense_stats = defense_stats
        self.durability = durability
        self.storage = storage
class weapon:
    def __init__(self,wielding_type,attack_damage, durability,weapon_type):
        self.wielding_type = wielding_type
        self.attack_damage = attack_damage
        self.durability = durability
        self.weapon_type = weapon_type
class ranged:
    def __init__(self, magazine):
        self.magazine = magazine
class melee:
    def __init__(self, length):
        self.length = length

class hostile:
    def __init__(self, stats, hostile_type, speed, spawn_chance):
        self.stats = stats
        self.hostile_type = hostile_type
        self.speed = speed
        self.spawn_chance = spawn_chance
    def hostile_attack(self):
        pass
    def damage_dealt(self, damage, player):
        #print(self.stats)
        #print(self.stats["Attack"])
        #print("Hp of en", self.stats["HP"])
        #print("Damage before defense", damage)
        en_HP = self.stats["HP"]
        prev_hp = en_HP
        damage = damage - ((self.stats["Defense"] ** 0.5) / randint(1,2))
        if abs(damage) != damage:
            damage = abs(damage) * 0.5
        en_HP -= damage
        en_HP = int(en_HP)
        if prev_hp < en_HP:
            en_HP = prev_hp
        print("\nYou dealt " + str(int(damage)) + " damage!\n")
        self.stats["HP"] = en_HP
        print("\nThe enemy is now on " + str(en_HP) + " Health!\n")
        energy = player.stats["Energy"]
        energy -= randint(1,35)
        if abs(energy) != energy:
            energy = 0
        player.stats["Energy"] = energy
        print("\nYou are now on " + str(player.stats["Energy"]) + " Energy.\n")
        sleep(4)
        #print("HP of en after damage -", self.stats["HP"])
    class goblins: # ok time for hellhounds and a gargoyle, this should be finished by today, then when you do the ending, that should be done on Saturday. We will have then successfully finished pyhton and I should make a portfolio and upload it there as well as all my other projects.
        def __init__(self, name):
            self.name = name
        def encounter(self, player, hostiles, rooms):
            curr_hostile = None
            for ind_room in rooms:
                if ind_room.player_loc == True:
                    curr_hostile = ind_room.hostiles
            game_delay_print("But... Hang on...", False, 0.3)
            game_delay_print("Something aint right here!", False, 0.15)
            game_delay_print("A green humanoid figure sat in the corner...", False, 0.1)
            game_delay_print("It bore the figure of a human but did not bear the conscience of man...", False, 0.1)
            unnoticed = randint(1,4) == 1
            if unnoticed == True:
                game_delay_print("The goblin fixated its gaze on something.", False, 0.15)
                game_delay_print("At the very least, you should be thankful you have gone in unnoticed.", False, 0.1)
                game_delay_print("Now choose wisely. Should you |[strike]| while it isn't looking or |[move]| and avoid a fight.", False, 0.15)
                player_input = input()
                while player_input != "move" and player_input != "strike":
                    player_input = input("Please select from the 2 above!")
                if player_input == "move":
                    player.move(rooms)
                    clear_shell()
                    return
                elif player_input == "strike":
                    damage = player.stats["Attack"] * 10
                    en_hp = curr_hostile.stats["HP"]
                    en_hp -= damage
                    curr_hostile.stats["HP"] = en_hp
            else:
                game_delay_print("It beamed its vicious eyes on you.", False, 0.25)
                game_delay_print("You assume battle stance...", False, 0.1)
                game_delay_print("A message popped up on your screen.", False, 0.05)
                game_delay_print("-\-\[Join Rock,Paper,Scissors. Y/N]/-/-", False, 0.05)
                game_delay_print("With utmost confidence, you say: ", False,0.05)
                game_delay_print("Yes", False,0.3)
                clear_shell()
            fight = True
            distance = randint(50,150)
            ammo_capac = 0
            ammo = 0
            for items in player.items:
                if items.equipped == True:
                    if isinstance(items.item_type, weapon):
                        if isinstance(items.item_type.weapon_type, ranged):
                            ammo_capac += items.item_type.weapon_type.magazine
            ammo = ammo_capac
            en_opt_dist = randint(1,100)
            damage = 0
            en_check = 0
            player.stats["HP"] = 100
            while fight == True:
                clear_shell()
                print("----" * 20)
                print("\n           Enemy HP: " + str(int(curr_hostile.stats["HP"])) + "\n")
                print("\n           Your HP: " + str(player.stats["HP"])+ "\n")
                    #print(player.stats)
                if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                    energy = player.stats["Max Energy"]
                    player.stats["Energy"] = energy
                print("\n           Your Energy: " + str(player.stats["Energy"])+ "\n")
                print("\n           Your Ammo: " + str(ammo)+ "\n")
                print("----" * 20 + "\n\n")
                input("Press ENTER to continue. - ")
                clear_shell()
                if curr_hostile.stats["HP"] <= 0:
                    for ind_room in rooms:
                        if ind_room.player_loc == True:
                            if type(ind_room.hostiles) == list:
                                ind_room.hostiles.pop()
                            else:
                                del ind_room.hostiles
                                ind_room.hostiles = []
                    print("You have slain the goblin, Max Energy is increased by 5.")
                    max_energy = player.stats["Max Energy"]
                    max_energy += 5
                    player.stats["Max Energy"] = max_energy
                    sleep(3)
                    clear_shell()
                    return False
                if player.stats["HP"] <= 0:
                    game_delay_print("You try to move but you just fall on the ground", False, 0.1)
                    game_delay_print("You are in a pool of your own blood", False, 0.15)
                    game_delay_print("As blood seeps out of you, so does your strength", False, 0.12)
                    game_delay_print("A message popped up on your screen...", False, 0.1)
                    sleep(0.5)
                    print("/\|[Player's Data will be overwritten]|/\\")
                    sleep(0.5)
                    game_delay_print("Your foe wasn't even that strong...", False, 0.2)
                    game_delay_print("I guess...", False, 0.21)
                    game_delay_print("This is...", False, 0.25)
                    game_delay_print("|[THE END]|", False, 0.3)
                    filepath = "ROOM_Data.csv"
                    with open(filepath, "w") as file:
                        None
                    filepath = "ROOMS_Map.csv"
                    with open(filepath, "w") as file:
                        None
                    return True
                defense_multiplier = 0
                en_defense_multiplier = 0
                damage = 0
                print("You are " + str(distance) + " units away from the target")
                game_delay_print("Should you |[fight]| or |[flee]|\n\n", False, 0.1)
                user_input_choice = input()
                while user_input_choice != "fight" and user_input_choice != "flee":
                    user_input_choice = input("Please select the 2 above! \n")
                if user_input_choice == "fight": # Add Rock paper scissors but with a slight twist, rock is attack, paper is block, and scissors is I guess shoot? anyways add a stat to player called stamina and make it so attack wastes stamina and also add a distance thing where attacking at a distance closest to your weapon length increases damage. This means you should add "step" where you waste stamina to get closer to or further away from the enemy. Thats all. no it aint, also add a reload function to reload your weapon and set its magazine back to 1: drawback is that it wastes a turn
                    user_input = input("Now choose... rock, paper, scissors, reload or step - ")
                    while user_input != "rock" and user_input != "paper" and user_input != "scissors" and user_input != "step" and user_input != "reload":
                        user_input = input("Choose the 4 above!\n")
                    if user_input == "rock" and player.stats["Energy"] == 0:
                        print("You flail around like a donut due to your lack of energy so nothing happens...")
                        sleep(4)
                    elif user_input == "rock":
                        melee_weapons = []
                        for ind_item in player.items:
                            if ind_item.equipped == True and isinstance(ind_item.item_type, weapon):
                                if isinstance(ind_item.item_type.weapon_type, melee):
                                    melee_weapons.append(ind_item)
                        length = 0
                        if len(melee_weapons) == 2:
                            if melee_weapons[0].item_type.weapon_type.length > melee_weapons[1].item_type.weapon_type.length:
                                length = melee_weapons[0].item_type.weapon_type.length
                            else:
                                length = melee_weapons[1].item_type.weapon_type.length
                        elif len(melee_weapons) == 1:
                            length = melee_weapons[0].item_type.weapon_type.length
                        else:
                            length = 1
                        multiplier = length / distance
                        multiplier += 1
                        damage = player.stats["Attack"] * multiplier
                        curr_hostile.damage_dealt(damage, player)
                    elif user_input == "paper":
                        while defense_multiplier == 0 and defense_multiplier > 1:
                            defense_multiplier = randint(1,10) / player.stats["Defense"]
                        energy = player.stats["Energy"]
                        energy += randint(0,20)
                        player.stats["Energy"] = energy
                        if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                            energy = player.stats["Max Energy"]
                            player.stats["Energy"] = energy
                    elif user_input == "scissors" and ammo == 0:
                        print("You stare at your gun baffled like a retard. You forgot to reload it you idiot!")
                        sleep(4)
                    elif user_input == "scissors":
                        multiplier = randint(1,5)
                        multiplier /= randint(1,10)
                        damage = player.stats["Attack"] * multiplier
                        print("------"+str(damage)+"------")
                        en_hp = curr_hostile.stats["HP"]
                        en_hp -= damage
                        en_hp = en_hp + (curr_hostile.stats["Defense"] / randint(1,10))
                        en_hp = int(en_hp)
                        curr_hostile.stats["HP"] = en_hp
                        print("The enemy is now on " + str(en_hp))
                        ammo -= 1
                        print("You are now on " + str(ammo) + " ammo.")
                        energy = player.stats["Energy"]
                        energy += randint(0,20)
                        player.stats["Energy"] = energy
                        if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                            energy = player.stats["Max Energy"]
                            player.stats["Energy"] = energy
                    elif user_input == "step":
                        step_input = input("Would you like to step |[forward]| or |[back]|")
                        while step_input != "forward" and step_input != "back":
                            step_input = input("Please input foward or back")
                        if step_input == "forward":
                            print("Distance Now --- " + str(distance))
                            distance -= randint(1,50)
                            if abs(distance) != distance or distance == 0:
                                distance = 1
                            print("Distance After --- " + str(distance))
                            energy = player.stats["Energy"]
                            energy -= randint(1,20)
                        elif step_input == "back":
                            distance += randint(1,50)
                            energy = player.stats["Energy"]
                            energy -= randint(1,20)
                    elif user_input == "reload":
                        ammo = ammo_capac
                    ai_choice = randint(0,2)
                    #print("Ai Choice: ------------- " + str(ai_choice))
                    if ai_choice == 0:
                        print("\nThe enemy strikes out\n.")
                        multiplier = en_opt_dist / distance
                        additive = abs(en_opt_dist - distance)
                        additive /= en_opt_dist
                        multiplier += additive
                        en_attack = curr_hostile.stats["Attack"]
                        damage = multiplier * en_attack
                        damage = int(damage)
                        if defense_multiplier != 0:
                            damage *= defense_multiplier
                        pl_hp = player.stats["HP"]
                        player.stats["HP"] = pl_hp - damage
                        print("\nThe enemy deals " + str(damage) + " damage.\n")
                        print("You are now on " + str(player.stats["HP"]) + " HP.")
                        sleep(4)
                    elif ai_choice == 1:
                        print("\nThe enemy blocks.\n")
                        while en_defense_multiplier == 0 and en_defense_multiplier > 1 or en_check == en_defense_multiplier:
                            if curr_hostile.stats["Defense"] > damage:
                                en_defense_multiplier = 1
                            else:
                                en_defense_multiplier = curr_hostile.stats["Defense"]/damage
                        if damage <= 0:
                            continue
                        else:
                            new_damage = damage * en_defense_multiplier
                            new_damage = abs(damage - new_damage)
                            en_hp = curr_hostile.stats["HP"]
                            prev_hp = en_hp
                            curr_hostile.stats["HP"] = en_hp + new_damage
                            if prev_hp < en_hp:
                                en_hp = prev_hp
                            en_check = en_defense_multiplier
                        print("\nThe enemy absorbed " + str(int(new_damage)) + " damage.\n")
                        print("\nThe enemy is now on " + str(int(en_hp + new_damage)) + " HP. \n")
                        sleep(4)
                    elif ai_choice == 2:
                        random_shoot_choices = ["\nThe goblin somehow pulled out a 50 cal and shot you?\n", "\nDamn, the goblin pulled out a magnum and fired a round at you!\n", "\nWha..? How does he have this many weapons. He pulled aout a machete and threw it at you?\n"]
                        multiplier = 1 / distance
                        additive = abs(1 - distance)
                        additive /= en_opt_dist
                        multiplier += additive
                        en_attack = curr_hostile.stats["Attack"]
                        damage = (multiplier + 0.1) * en_attack
                        damage = int(damage)
                        if defense_multiplier != 0:
                            damage *= defense_multiplier
                        pl_hp = player.stats["HP"]
                        player.stats["HP"] = pl_hp - damage
                        print(choice(random_shoot_choices))
                        print("\nThe enemy deals " + str(damage) + " damage.\n")
                        print("\nYou are now on " + str(player.stats["HP"]) + " HP.\n")
                        sleep(4)
                elif user_input_choice == "flee":
                    player.move(rooms)
                    return False
    class hellhounds:
        def __init__(self, name):
            self.name = name
        def encounter(self, player, hostiles, rooms):
            curr_hostile = None
            for ind_room in rooms:
                if ind_room.player_loc == True:
                    curr_hostile = ind_room.hostiles
            game_delay_print("But... Hang on...", False, 0.3)
            game_delay_print("Something aint right here!", False, 0.15)
            game_delay_print("A hellish creature was lying on the ground...", False, 0.1)
            game_delay_print("Its fur blacker than hellfire and the heat emnating from its body was unbearable.", False, 0.1)
            unnoticed = randint(1,4) == 1
            if unnoticed == True:
                game_delay_print("The hellhound fixated its gaze on something.", False, 0.15)
                game_delay_print("At the very least, you should be thankful you have gone in unnoticed.", False, 0.1)
                game_delay_print("Now choose wisely. Should you |[strike]| while it isn't looking or |[move]| and avoid a fight.", False, 0.15)
                player_input = input()
                while player_input != "move" and player_input != "strike":
                    player_input = input("Please select from the 2 above!")
                if player_input == "move":
                    player.move(rooms)
                    clear_shell()
                    return
                elif player_input == "strike":
                    damage = player.stats["Attack"] * 10
                    en_hp = curr_hostile.stats["HP"]
                    en_hp -= damage
                    curr_hostile.stats["HP"] = en_hp
            else:
                game_delay_print("It beamed its vicious eyes on you.", False, 0.25)
                game_delay_print("You assume battle stance...", False, 0.1)
                game_delay_print("A message popped up on your screen.", False, 0.05)
                game_delay_print("-\-\[Join Rock,Paper,Scissors. Y/N]/-/-", False, 0.05)
                game_delay_print("With utmost confidence, you say: ", False,0.05)
                game_delay_print("Yes", False,0.3)
            fight = True
            distance = randint(50,150)
            ammo_capac = 0
            ammo = 0
            for items in player.items:
                if items.equipped == True:
                    if isinstance(items.item_type, weapon):
                        if isinstance(items.item_type.weapon_type, ranged):
                            ammo_capac += items.item_type.weapon_type.magazine
            ammo = ammo_capac
            en_opt_dist = randint(1,100)
            damage = 0
            en_check = 0
            player.stats["HP"] = 100
            while fight == True:
                clear_shell()
                print("----" * 20)
                print("\n           Enemy HP: " + str(int(curr_hostile.stats["HP"])) + "\n")
                print("\n           Your HP: " + str(player.stats["HP"])+ "\n")
                    #print(player.stats)
                if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                    energy = player.stats["Max Energy"]
                    player.stats["Energy"] = energy
                print("\n           Your Energy: " + str(player.stats["Energy"])+ "\n")
                print("\n           Your Ammo: " + str(ammo)+ "\n")
                print("----" * 20 + "\n\n")
                input("Press ENTER to continue. - ")
                clear_shell()
                if curr_hostile.stats["HP"] <= 0:
                    for ind_room in rooms:
                        if ind_room.player_loc == True:
                            if type(ind_room.hostiles) == list:
                                ind_room.hostiles.pop()
                            else:
                                del ind_room.hostiles
                                ind_room.hostiles = []
                    print("You have slain the hellhound, Max Energy is increased by 10.")
                    max_energy = player.stats["Max Energy"]
                    max_energy += 5
                    player.stats["Max Energy"] = max_energy
                    sleep(3)
                    clear_shell()
                    return False
                if player.stats["HP"] <= 0:
                    game_delay_print("You try to move but you just fall on the ground", False, 0.1)
                    game_delay_print("You are in a pool of your own blood", False, 0.15)
                    game_delay_print("As blood seeps out of you, so does your strength", False, 0.12)
                    game_delay_print("A message popped up on your screen...", False, 0.1)
                    sleep(0.5)
                    print("/\|[Player's Data will be overwritten]|/\\")
                    sleep(0.5)
                    game_delay_print("Your foe wasn't even that strong...", False, 0.2)
                    game_delay_print("I guess...", False, 0.21)
                    game_delay_print("This is...", False, 0.25)
                    game_delay_print("|[THE END]|", False, 0.3)
                    filepath = "ROOM_Data.csv"
                    with open(filepath, "w") as file:
                        None
                    filepath = "ROOMS_Map.csv"
                    with open(filepath, "w") as file:
                        None
                    return True
                defense_multiplier = 0
                en_defense_multiplier = 0
                damage = 0
                print("You are " + str(distance) + " units away from the target")
                game_delay_print("Should you |[fight]| or |[flee]|\n\n", False, 0.1)
                user_input_choice = input()
                while user_input_choice != "fight" and user_input_choice != "flee":
                    user_input_choice = input("Please select the 2 above! \n")
                if user_input_choice == "fight": # Add Rock paper scissors but with a slight twist, rock is attack, paper is block, and scissors is I guess shoot? anyways add a stat to player called stamina and make it so attack wastes stamina and also add a distance thing where attacking at a distance closest to your weapon length increases damage. This means you should add "step" where you waste stamina to get closer to or further away from the enemy. Thats all. no it aint, also add a reload function to reload your weapon and set its magazine back to 1: drawback is that it wastes a turn
                    user_input = input("Now choose... rock, paper, scissors, reload or step - ")
                    while user_input != "rock" and user_input != "paper" and user_input != "scissors" and user_input != "step" and user_input != "reload":
                        user_input = input("Choose the 4 above!\n")
                    if user_input == "rock" and player.stats["Energy"] == 0:
                        print("You flail around like a donut due to your lack of energy so nothing happens...")
                        sleep(4)
                    elif user_input == "rock":
                        melee_weapons = []
                        for ind_item in player.items:
                            if ind_item.equipped == True and isinstance(ind_item.item_type, weapon):
                                if isinstance(ind_item.item_type.weapon_type, melee):
                                    melee_weapons.append(ind_item)
                        length = 0
                        if len(melee_weapons) == 2:
                            if melee_weapons[0].item_type.weapon_type.length > melee_weapons[1].item_type.weapon_type.length:
                                length = melee_weapons[0].item_type.weapon_type.length
                            else:
                                length = melee_weapons[1].item_type.weapon_type.length
                        elif len(melee_weapons) == 1:
                            length = melee_weapons[0].item_type.weapon_type.length
                        else:
                            length = 1
                        multiplier = length / distance
                        multiplier += 1
                        damage = player.stats["Attack"] * multiplier
                        curr_hostile.damage_dealt(damage, player)
                    elif user_input == "paper":
                        while defense_multiplier == 0 and defense_multiplier > 1:
                            defense_multiplier = randint(1,10) / player.stats["Defense"]
                        energy = player.stats["Energy"]
                        energy += randint(0,20)
                        player.stats["Energy"] = energy
                        if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                            energy = player.stats["Max Energy"]
                            player.stats["Energy"] = energy
                    elif user_input == "scissors" and ammo == 0:
                        print("You stare at your gun baffled like a retard. You forgot to reload it you idiot!")
                        sleep(4)
                    elif user_input == "scissors":
                        multiplier = randint(1,5)
                        multiplier /= randint(1,10)
                        damage = player.stats["Attack"] * multiplier
                        print("------"+str(damage)+"------")
                        en_hp = curr_hostile.stats["HP"]
                        en_hp -= damage
                        en_hp = en_hp + (curr_hostile.stats["Defense"] / randint(1,10))
                        en_hp = int(en_hp)
                        curr_hostile.stats["HP"] = en_hp
                        print("The enemy is now on " + str(en_hp))
                        ammo -= 1
                        print("You are now on " + str(ammo) + " ammo.")
                        energy = player.stats["Energy"]
                        energy += randint(0,20)
                        player.stats["Energy"] = energy
                        if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                            energy = player.stats["Max Energy"]
                            player.stats["Energy"] = energy
                    elif user_input == "step":
                        step_input = input("Would you like to step |[forward]| or |[back]|")
                        while step_input != "forward" and step_input != "back":
                            step_input = input("Please input foward or back")
                        if step_input == "forward":
                            print("Distance Now --- " + str(distance))
                            distance -= randint(1,50)
                            if abs(distance) != distance or distance == 0:
                                distance = 1
                            print("Distance After --- " + str(distance))
                            energy = player.stats["Energy"]
                            energy -= randint(1,20)
                        elif step_input == "back":
                            distance += randint(1,50)
                            energy = player.stats["Energy"]
                            energy -= randint(1,20)
                    elif user_input == "reload":
                        ammo = ammo_capac
                    ai_choice = randint(0,2)
                    #print("Ai Choice: ------------- " + str(ai_choice))
                    if ai_choice == 0:
                        print("\nThe enemy strikes out\n.")
                        multiplier = en_opt_dist / distance
                        additive = abs(en_opt_dist - distance)
                        additive /= en_opt_dist
                        multiplier += additive
                        en_attack = curr_hostile.stats["Attack"]
                        damage = multiplier * en_attack
                        damage = int(damage)
                        if defense_multiplier != 0:
                            damage *= defense_multiplier
                        pl_hp = player.stats["HP"]
                        player.stats["HP"] = pl_hp - damage
                        print("\nThe enemy deals " + str(damage) + " damage.\n")
                        print("You are now on " + str(player.stats["HP"]) + " HP.")
                        sleep(4)
                    elif ai_choice == 1:
                        print("\nThe enemy blocks.\n")
                        while en_defense_multiplier == 0 and en_defense_multiplier > 1 or en_check == en_defense_multiplier:
                            if curr_hostile.stats["Defense"] > damage:
                                en_defense_multiplier = 1
                            else:
                                en_defense_multiplier = curr_hostile.stats["Defense"]/damage
                        if damage <= 0:
                            continue
                        else:
                            new_damage = damage * en_defense_multiplier
                            new_damage = abs(damage - new_damage)
                            en_hp = curr_hostile.stats["HP"]
                            prev_hp = en_hp
                            curr_hostile.stats["HP"] = en_hp + new_damage
                            if prev_hp < en_hp:
                                en_hp = prev_hp
                            en_check = en_defense_multiplier
                        print("\nThe enemy absorbed " + str(int(new_damage)) + " damage.\n")
                        print("\nThe enemy is now on " + str(int(en_hp + new_damage)) + " HP. \n")
                        sleep(4)
                    elif ai_choice == 2:
                        random_shoot_choices = ["It held an LMG between its jaws and shot you...", "It used its paws to fire an arrow at you...", "The hellhound...p.peed on you...? Who made this game, oh wait... it was me."]
                        multiplier = 1 / distance
                        additive = abs(1 - distance)
                        additive /= en_opt_dist
                        multiplier += additive
                        en_attack = curr_hostile.stats["Attack"]
                        damage = (multiplier + 0.1) * en_attack
                        damage = int(damage)
                        if defense_multiplier != 0:
                            damage *= defense_multiplier
                        pl_hp = player.stats["HP"]
                        player.stats["HP"] = pl_hp - damage
                        print(choice(random_shoot_choices))
                        print("\nThe enemy deals " + str(damage) + " damage.\n")
                        print("\nYou are now on " + str(player.stats["HP"]) + " HP.\n")
                        sleep(4)
                elif user_input_choice == "flee":
                    player.move(rooms)
                    return False
    class gargoyles:
        def __init__(self, name):
            self.name = name
        def encounter(self, player, hostiles, rooms):
            curr_hostile = None
            for ind_room in rooms:
                if ind_room.player_loc == True:
                    curr_hostile = ind_room.hostiles
            game_delay_print("But... Hang on...", False, 0.3)
            game_delay_print("Something aint right here!", False, 0.15)
            game_delay_print("A creature was crouched in the corner...", False, 0.1)
            game_delay_print("Its wings shrouded its body, but it did not hide its gaze doped with rage", False, 0.1)
            unnoticed = randint(1,4) == 1
            if unnoticed == True:
                game_delay_print("The gargoyoe fixated its gaze on something.", False, 0.15)
                game_delay_print("At the very least, you should be thankful you have gone in unnoticed.", False, 0.1)
                game_delay_print("Now choose wisely. Should you |[strike]| while it isn't looking or |[move]| and avoid a fight.", False, 0.15)
                player_input = input()
                while player_input != "move" and player_input != "strike":
                    player_input = input("Please select from the 2 above!")
                if player_input == "move":
                    player.move(rooms)
                    clear_shell()
                    return
                elif player_input == "strike":
                    damage = player.stats["Attack"] * 10
                    en_hp = curr_hostile.stats["HP"]
                    en_hp -= damage
                    curr_hostile.stats["HP"] = en_hp
            else:
                game_delay_print("It beamed its vicious eyes on you.", False, 0.25)
                game_delay_print("You assume battle stance...", False, 0.1)
                game_delay_print("A message popped up on your screen.", False, 0.05)
                game_delay_print("-\-\[Join Rock,Paper,Scissors. Y/N]/-/-", False, 0.05)
                game_delay_print("With utmost confidence, you say: ", False,0.05)
                game_delay_print("Yes", False,0.3)
            fight = True
            distance = randint(50,150)
            ammo_capac = 0
            ammo = 0
            for items in player.items:
                if items.equipped == True:
                    if isinstance(items.item_type, weapon):
                        if isinstance(items.item_type.weapon_type, ranged):
                            ammo_capac += items.item_type.weapon_type.magazine
            ammo = ammo_capac
            en_opt_dist = randint(1,100)
            damage = 0
            en_check = 0
            player.stats["HP"] = 100
            while fight == True:
                clear_shell()
                print("----" * 20)
                print("\n           Enemy HP: " + str(int(curr_hostile.stats["HP"])) + "\n")
                print("\n           Your HP: " + str(player.stats["HP"])+ "\n")
                    #print(player.stats)
                if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                    energy = player.stats["Max Energy"]
                    player.stats["Energy"] = energy
                print("\n           Your Energy: " + str(player.stats["Energy"])+ "\n")
                print("\n           Your Ammo: " + str(ammo)+ "\n")
                print("----" * 20 + "\n\n")
                input("Press ENTER to continue. - ")
                clear_shell()
                if curr_hostile.stats["HP"] <= 0:
                    for ind_room in rooms:
                        if ind_room.player_loc == True:
                            if type(ind_room.hostiles) == list:
                                ind_room.hostiles.pop()
                            else:
                                del ind_room.hostiles
                                ind_room.hostiles = []
                    print("You have slain the gargoyle, Max Energy is increased by 15.")
                    max_energy = player.stats["Max Energy"]
                    max_energy += 5
                    player.stats["Max Energy"] = max_energy
                    sleep(3)
                    clear_shell()
                    return False
                if player.stats["HP"] <= 0:
                    game_delay_print("You try to move but you just fall on the ground", False, 0.1)
                    game_delay_print("You are in a pool of your own blood", False, 0.15)
                    game_delay_print("As blood seeps out of you, so does your strength", False, 0.12)
                    game_delay_print("A message popped up on your screen...", False, 0.1)
                    sleep(0.5)
                    print("/\|[Player's Data will be overwritten]|/\\")
                    sleep(0.5)
                    game_delay_print("Your foe wasn't even that strong...", False, 0.2)
                    game_delay_print("I guess...", False, 0.21)
                    game_delay_print("This is...", False, 0.25)
                    game_delay_print("|[THE END]|", False, 0.3)
                    filepath = "ROOM_Data.csv"
                    with open(filepath, "w") as file:
                        None
                    filepath = "ROOMS_Map.csv"
                    with open(filepath, "w") as file:
                        None
                    return True
                defense_multiplier = 0
                en_defense_multiplier = 0
                damage = 0
                print("You are " + str(distance) + " units away from the target")
                game_delay_print("Should you |[fight]| or |[flee]|\n\n", False, 0.1)
                user_input_choice = input()
                while user_input_choice != "fight" and user_input_choice != "flee":
                    user_input_choice = input("Please select the 2 above! \n")
                if user_input_choice == "fight": # Add Rock paper scissors but with a slight twist, rock is attack, paper is block, and scissors is I guess shoot? anyways add a stat to player called stamina and make it so attack wastes stamina and also add a distance thing where attacking at a distance closest to your weapon length increases damage. This means you should add "step" where you waste stamina to get closer to or further away from the enemy. Thats all. no it aint, also add a reload function to reload your weapon and set its magazine back to 1: drawback is that it wastes a turn
                    user_input = input("Now choose... rock, paper, scissors, reload or step - ")
                    while user_input != "rock" and user_input != "paper" and user_input != "scissors" and user_input != "step" and user_input != "reload":
                        user_input = input("Choose the 4 above!\n")
                    if user_input == "rock" and player.stats["Energy"] == 0:
                        print("You flail around like a donut due to your lack of energy so nothing happens...")
                        sleep(4)
                    elif user_input == "rock":
                        melee_weapons = []
                        for ind_item in player.items:
                            if ind_item.equipped == True and isinstance(ind_item.item_type, weapon):
                                if isinstance(ind_item.item_type.weapon_type, melee):
                                    melee_weapons.append(ind_item)
                        length = 0
                        if len(melee_weapons) == 2:
                            if melee_weapons[0].item_type.weapon_type.length > melee_weapons[1].item_type.weapon_type.length:
                                length = melee_weapons[0].item_type.weapon_type.length
                            else:
                                length = melee_weapons[1].item_type.weapon_type.length
                        elif len(melee_weapons) == 1:
                            length = melee_weapons[0].item_type.weapon_type.length
                        else:
                            length = 1
                        multiplier = length / distance
                        multiplier += 1
                        damage = player.stats["Attack"] * multiplier
                        curr_hostile.damage_dealt(damage, player)
                    elif user_input == "paper":
                        while defense_multiplier == 0 and defense_multiplier > 1:
                            defense_multiplier = randint(1,10) / player.stats["Defense"]
                        energy = player.stats["Energy"]
                        energy += randint(0,20)
                        player.stats["Energy"] = energy
                        if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                            energy = player.stats["Max Energy"]
                            player.stats["Energy"] = energy
                    elif user_input == "scissors" and ammo == 0:
                        print("You stare at your gun baffled like a retard. You forgot to reload it you idiot!")
                        sleep(4)
                    elif user_input == "scissors":
                        multiplier = randint(1,5)
                        multiplier /= randint(1,10)
                        damage = player.stats["Attack"] * multiplier
                        print("------"+str(damage)+"------")
                        en_hp = curr_hostile.stats["HP"]
                        en_hp -= damage
                        en_hp = en_hp + (curr_hostile.stats["Defense"] / randint(1,10))
                        en_hp = int(en_hp)
                        curr_hostile.stats["HP"] = en_hp
                        print("The enemy is now on " + str(en_hp))
                        ammo -= 1
                        print("You are now on " + str(ammo) + " ammo.")
                        energy = player.stats["Energy"]
                        energy += randint(0,20)
                        player.stats["Energy"] = energy
                        if player.stats["Energy"] > player.stats["Max Energy"]: # key error Max Energy is appar not a key so just figure out from print statement
                            energy = player.stats["Max Energy"]
                            player.stats["Energy"] = energy
                    elif user_input == "step":
                        step_input = input("Would you like to step |[forward]| or |[back]|")
                        while step_input != "forward" and step_input != "back":
                            step_input = input("Please input foward or back")
                        if step_input == "forward":
                            print("Distance Now --- " + str(distance))
                            distance -= randint(1,50)
                            if abs(distance) != distance or distance == 0:
                                distance = 1
                            print("Distance After --- " + str(distance))
                            energy = player.stats["Energy"]
                            energy -= randint(1,20)
                        elif step_input == "back":
                            distance += randint(1,50)
                            energy = player.stats["Energy"]
                            energy -= randint(1,20)
                    elif user_input == "reload":
                        ammo = ammo_capac
                    ai_choice = randint(0,2)
                    #print("Ai Choice: ------------- " + str(ai_choice))
                    if ai_choice == 0:
                        print("\nThe enemy strikes out\n.")
                        multiplier = en_opt_dist / distance
                        additive = abs(en_opt_dist - distance)
                        additive /= en_opt_dist
                        multiplier += additive
                        en_attack = curr_hostile.stats["Attack"]
                        damage = multiplier * en_attack
                        damage = int(damage)
                        if defense_multiplier != 0:
                            damage *= defense_multiplier
                        pl_hp = player.stats["HP"]
                        player.stats["HP"] = pl_hp - damage
                        print("\nThe enemy deals " + str(damage) + " damage.\n")
                        print("You are now on " + str(player.stats["HP"]) + " HP.")
                        sleep(4)
                    elif ai_choice == 1:
                        print("\nThe enemy blocks.\n")
                        while en_defense_multiplier == 0 and en_defense_multiplier > 1 or en_check == en_defense_multiplier:
                            if curr_hostile.stats["Defense"] > damage:
                                en_defense_multiplier = 1
                            else:
                                en_defense_multiplier = curr_hostile.stats["Defense"]/damage
                        if damage <= 0:
                            continue
                        else:
                            new_damage = damage * en_defense_multiplier
                            new_damage = abs(damage - new_damage)
                            en_hp = curr_hostile.stats["HP"]
                            prev_hp = en_hp
                            curr_hostile.stats["HP"] = en_hp + new_damage
                            if prev_hp < en_hp:
                                en_hp = prev_hp
                            en_check = en_defense_multiplier
                        print("\nThe enemy absorbed " + str(int(new_damage)) + " damage.\n")
                        print("\nThe enemy is now on " + str(int(en_hp + new_damage)) + " HP. \n")
                        sleep(4)
                    elif ai_choice == 2:
                        random_shoot_choices = ["It threw a molotov at you...", "It tore off its wing and threw it at you...", "It stared at you causing you to have emotional damage?"]
                        multiplier = 1 / distance
                        additive = abs(1 - distance)
                        additive /= en_opt_dist
                        multiplier += additive
                        en_attack = curr_hostile.stats["Attack"]
                        damage = (multiplier + 0.1) * en_attack
                        damage = int(damage)
                        if defense_multiplier != 0:
                            damage *= defense_multiplier
                        pl_hp = player.stats["HP"]
                        player.stats["HP"] = pl_hp - damage
                        print(choice(random_shoot_choices))
                        print("\nThe enemy deals " + str(damage) + " damage.\n")
                        print("\nYou are now on " + str(player.stats["HP"]) + " HP.\n")
                        sleep(4)
                elif user_input_choice == "flee":
                    player.move(rooms)
                    return False

#print("testing")
#print(item)

def map_maker():
    size = (randint(6,16),randint(6,16))
    #print(size)
    plan_map = {}
    n = 0
    row = 1
    x = 0
    while x != size[1]:
        x += 1
        n = 0
        plan_map[x] = []
        while n != size[0]:
            #print(n)
            plan_map[x].append(1)
            n += 1
    return plan_map, size
def debug_display_map(plan_map):
    for key in plan_map:
        row = plan_map[key]
        print(row)
class Room:
    def __init__(self, player_loc,coords,discovered,items,hostiles,move):
        self.player_loc = player_loc
        self.coords = coords
        self.discovered = discovered
        self.items = items
        self.hostiles = hostiles
        self.move = move
def initialise_starter_pos(plan_map):
    row = len(plan_map)
    start_row = plan_map[row]
    length = len(start_row)
    #print(length)
    start_pos = randint(1,length) - 1
    #print(start_pos)
    start_row[start_pos] = 1
    creating = True
    start = True
    """
    while creating == True:
    if row == len(plan_map) or row == 1: #""" """If it's at the beggining or end, add 3 branches or add 2"""
    """
    if start == True:
    room = (start_pos, row)
    if start_pos == len(start_row) - 1 or start_pos == 0:
    branch = randint(1,2)
    #start = False
    else:
    branch = randint(1,3)
    else:
    branch = randint(1,3)
    if branch == 1:
    for i in
    """
    
    return start_pos,row
rooms = []
def initialise_rooms(plan_map,player_coords,rooms):
    for row in plan_map:
        row_value = plan_map[row]
        #print(row_value)
        for index, room in enumerate(row_value):
            move = ["N","E","S","W"]
            #print(move)
            #print(index)
            #print("else")
            #print("row: ", row)
            if row == 1:
                move = ["E","S","W"]
            elif row == len(plan_map):
                move = ["N","E","W"]
            else:
                move = ["N","E","S","W"]
            if index == len(row_value) - 1:
                #print("len")
                #print("last_index")
                #print(move)
                move_index = move.index("E")
                move.pop(move_index)
            elif index == 0:
                #print("0")
                #print("first_index")
                #print(move)
                move_index = move.index("W")
                move.pop(move_index)
            coordinates = (index,row)
            #print(move)
            if coordinates == player_coords:
                initialised_room = Room(True,coordinates,True,False,[],move)
            else:
                initialised_room = Room(False,coordinates,False,False,[],move)
            #print(initialised_room.coords, initialised_room.move)
            rooms.append(initialised_room)
    return rooms
import csv
def save_map(rooms):
    with open("ROOMS_Map.csv", "w") as file:
        writer = csv.writer(file)
        data = []
        for room in rooms:
            values = [room.player_loc, room.coords, room.discovered]
            items = {}
            for item_val in room.items:
                #print(item_val.name)
                length = len(items)
                if isinstance(item_val.item_type, armour):
                    items[length] = [item_val.name, item_val.equippable, item_val.equipped,item_val.spawnable,item_val.spawn_probability,item_val.item_type.body_type,item_val.item_type.defense_stats,item_val.item_type.durability, item_val.item_type.storage]
                elif isinstance(item_val.item_type, weapon):
                    weapon_type = item_val.item_type.weapon_type
                    if isinstance(weapon_type, melee):
                        items[length] = [item_val.name, item_val.equippable, item_val.equipped,item_val.spawnable,item_val.spawn_probability, item_val.item_type.wielding_type, item_val.item_type.attack_damage, item_val.item_type.durability, item_val.item_type.weapon_type.length]
                    else:
                        items[length] = [item_val.name, item_val.equippable, item_val.equipped,item_val.spawnable,item_val.spawn_probability, item_val.item_type.wielding_type, item_val.item_type.attack_damage, item_val.item_type.durability, item_val.item_type.weapon_type.magazine]
            #values.append(room.hostiles)
            hostile_values = []
            if room.hostiles != [False]:
                #print("--",room.hostiles,"--")
                if room.hostiles != [] and isinstance(room.hostiles, hostile):
                    hostile_values = [room.hostiles.stats, room.hostiles.hostile_type.name, room.hostiles.speed, room.hostiles.spawn_chance]
                else:
                    for ind_hostile in room.hostiles:
                        #print("---------------",ind_hostile,"-------------------")
                        #print("d")
                        #if ind_hostile == False or ind_hostile == []:
                        #hostile_values = []
                        #print(type(ind_hostile))
                        #print(ind_hostile.hostile_type)
                        hostile_values = [ind_hostile.stats, ind_hostile.hostile_type.name, ind_hostile.speed, ind_hostile.spawn_chance]
            values.append(items)
            values.append(hostile_values)
            values.append(room.move)
            #print(values)
            data.append(values)
        def cleaner(bit):
            if bit != []:
                return True
            else:
                return False
        data = list(filter(cleaner, data))
        #print(data)
        writer.writerows(data)
def load_map(rooms, game_items, hostiles):
    #global item
    #if item == item:
        #del item
    with open("ROOMS_Map.csv", "r") as file:
        reader = csv.reader(file)
        data = []
        true_data_row = []
        def comma_remover(character):
            #print(character)
            if character != "," and character != ", " and character != "'" and character != "[" and character != "]" and character != "{" and character != "}":
                return True
        def value_merger(x,y):
            #print(x+y)
            return x + y
        def value_converter(value):
            if "." in value:
                #print("found")
                try:
                    float(value)
                except:
                    pass
                else:
                    value = float(value)
            else:
                try:
                    int(value)
                except:
                    pass
                else:
                    value = int(value)
                if type(value) == int:
                    pass
                else:
                    try:
                        bool(value)
                    except:
                        pass
                    else:
                    #print("Is this a bool value????????????----", value)
                        if value == "False":
                            value = False
                        if value == "True":
                            value = True
            return value
        #item_data = None
        for rows in reader:
            #print(rows)
            #print(type(rows))
            true_data_row = []
            if rows == []:
                continue
            for index, value in enumerate(rows):
                #print("--------------",value,"-------------- Index: ", index)
                if index == 0:
                    if value == "True":
                        true_data_row.append(True)
                    else:
                        true_data_row.append(False)
                if value == rows[1]:
                    length = len(value)
                    numbers = []
                    for substring in value:
                        try:
                            int(substring)
                        except:
                            if substring == ",":
                                numbers.append(substring)
                        else:
                            numbers.append(substring)
                    range_length = len(numbers)
                    first_set = 0
                    second_set = 0
                    i = numbers.index(",") + 1
                    flag = True
                    for number in numbers:
                        if flag == True:
                            if number != ",":
                                if first_set == 0:
                                    first_set = number
                                else:
                                    first_set = first_set + number
                            else:
                                flag = False
                        else:
                            continue
                    for I in range(i,range_length):
                        number = numbers[I]
                        if second_set == 0:
                            second_set = number
                        else:
                            second_set = second_set + number
                    first_set = int(first_set)
                    second_set = int(second_set)
                    #print(first_set, second_set)
                    tup = (first_set, second_set)
                    true_data_row.append(tup)
                if index == 2:
                    if value == "True":
                        true_data_row.append(True)
                    else:
                        true_data_row.append(False)
                if value == rows[3]:
                    room_items = []
                    if value == "{}":
                        true_data_row.append([])
                    else:
                        character_list = []
                        filtered_stringed = []
                        stringed = value.split()
                        converted_stringed = []
                        fixed_stringed = []
                        for bit in stringed:
                            characters = list(filter(comma_remover, bit))
                            character_list.append(characters)
                            #print(character_list)
                        for character in character_list:
                            #print(character)
                            character = list(filter(comma_remover, character))             
                            character = reduce(value_merger, character)
                            #print(character)
                            filtered_stringed.append(character)
                            #print(filtered_stringed)
                        for value in filtered_stringed:
                            value = value_converter(value)
                            converted_stringed.append(value)
                        #print(filtered_stringed)
                        #print(converted_stringed)
                        name_index_1 = None
                        name_index_2 = None
                        for value in converted_stringed:
                            #print("value is: ", value)
                            try:
                                if ":" in value:
                                    fixed_stringed.append(value)
                                    key_index = converted_stringed.index(value)
                                    name_index_1 = key_index + 1
                                    name_index_2 = name_index_1 + 1
                                    #print(converted_stringed[name_index_1], converted_stringed[name_index_2])
                                    name = converted_stringed[name_index_1] + " " + converted_stringed[name_index_2]
                                    value = name
                                    fixed_stringed.append(value)
                                elif converted_stringed[name_index_1] == value:
                                    continue
                                elif converted_stringed[name_index_2] == value:
                                    continue
                                else:
                                    fixed_stringed.append(value)
                            except:
                                #print(converted_stringed[name_index_1], converted_stringed[name_index_2], value)
                                if name_index_1 == None or name_index_2 == None:
                                    fixed_stringed.append(value)
                                elif converted_stringed[name_index_1] == value:
                                    continue
                                elif converted_stringed[name_index_2] == value:
                                    continue
                                else:
                                    fixed_stringed.append(value)
                        #print(fixed_stringed)
                        room_items = []
                        game_items_sub = []
                        for value in fixed_stringed:
                            #print(game_items_sub)
                            #print(value)
                            if value == "True":
                                value = True
                            if value == "False":
                                value = False
                            try:
                                if ":" in value:
                                    #print("found")
                                    if game_items_sub != []:
                                        for items in game_items:
                                            name = items.name
                                            #print(name, value)
                                            if name == game_items_sub[0]:
                                                #print(name, game_items_sub[0])
                                                #print(type(items.item_type))
                                                if isinstance(items.item_type.weapon_type, melee):
                                                    #print("melee")
                                                    Melee = melee(game_items_sub[8])
                                                    Weapon = weapon(game_items_sub[5],game_items_sub[6],game_items_sub[7], Melee)
                                                    appending_item = item(game_items_sub[0],game_items_sub[1],game_items_sub[2],game_items_sub[3],game_items_sub[4],Weapon)
                                                    #print(appending_item)
                                                    #print("Length of the weapon is -------------------", appending_item.item_type.weapon_type.length)
                                                elif isinstance(items.item_type, armour):
                                                    #print("armour")
                                                    Armour = armour(game_items_sub[5],game_items_sub[6],game_items_sub[7],game_items_sub[8])
                                                    appending_item = item(game_items_sub[0],game_items_sub[1],game_items_sub[2],game_items_sub[3],game_items_sub[4], Armour)
                                                elif isinstance(items.item_type.weapon_type, ranged):
                                                    #print("You know what it is.")
                                                    Ranged = weapon(game_items_sub[6],game_items_sub[7],game_items_sub[8],ranged(game_items_sub[9]))
                                                    appending_item = item(game_items_sub[0],game_items_sub[1],game_items_sub[2],game_items_sub[3],game_items_sub[4],Ranged)
                                        #print(appending_item)
                                        room_items.append(appending_item)
                                        #print(room_items)
                                    game_items_sub = []
                                else:
                                    if ":" in value:
                                        #print("skipped")
                                        continue
                                    else:
                                        if ":" in value:
                                            continue
                                        else:
                                            #print(value)
                                            game_items_sub.append(value)
                            except Exception as E:
                                #print(E)
                                if type(value) == str:
                                    continue
                                else:
                                    game_items_sub.append(value)
                        #print(room_items)
                        #print(filtered_stringed)
                        #print(stringed)
                        true_data_row.append(room_items)
                if value == rows[4]:
                    #print("-----------------------",value,"-------------------------------")
                    if value == "[]":
                        true_data_row.append([])
                        continue
                    #print(type(value))
                    splitted = value.split()
                    filtered = []
                    for values in splitted:
                        add_val = list(filter(comma_remover, values))
                        filtered.append(add_val)
                    #print("------------------------",filtered)
                    stringed = []
                    for values in filtered:
                        string = reduce(value_merger,values)
                        stringed.append(string)
                    #print(stringed)
                    converted = list(map(value_converter, stringed))
                    #print(converted)
                    true_hostiles = []
                    for index, values in enumerate(converted):
                        #print(index, values)
                        try:
                            if ":" in values:
                                #print("found")
                                #print(values)
                                index_val = index + 1
                                new_values = values.replace(":", "")
                                if true_hostiles == []:
                                    #print("ye notin inside")
                                    true_hostiles.append({new_values: converted[index_val]})
                                else:
                                    #print("going in")
                                    true_hostiles[0][new_values] = converted[index_val]
                            else:
                                try:
                                    if ":" in converted[index-1]:
                                        continue
                                    else:
                                        true_hostiles.append(values)
                                except:
                                    true_hostiles.append(values)
                        except:
                            #print(E)
                            try:
                                if ":" in converted[index-1]:
                                    #print("skipping")
                                    continue
                                else:
                                    #print("appending")
                                    true_hostiles.append(values)
                            except:
                                #print("ok")
                                true_hostiles.append(values)
                    #print(true_hostiles)
                    #hostile_obj = hostile(true_hostiles[0], true_hostiles[1], true_hostiles[2], true_hostiles[3])
                    for index, values in enumerate(true_hostiles):
                        #print(index, values)
                        if index == 1:
                            #print("Name Found")
                            for a_hostile in hostiles:
                                #print(a_hostile.hostile_type.name)
                                if a_hostile.hostile_type.name == values:
                                    #print("Found name")
                                    if a_hostile.hostile_type.name == "Goblin":
                                        #print("Found")
                                        hostile_obj = hostile(true_hostiles[0], hostile.goblins(true_hostiles[1]), true_hostiles[2], true_hostiles[3])
                                        true_data_row.append(hostile_obj)
                                    elif a_hostile.hostile_type.name == "Hellhound":
                                        hostile_obj = hostile(true_hostiles[0], hostile.hellhounds(true_hostiles[1]), true_hostiles[2], true_hostiles[3])
                                        true_data_row.append(hostile_obj)
                                    elif a_hostile.hostile_type.name == "Gargoyle":
                                        hostile_obj = hostile(true_hostiles[0], hostile.gargoyles(true_hostiles[1]), true_hostiles[2], true_hostiles[3])
                                        true_data_row.append(hostile_obj)
                    #print(hostile_obj)
                
                move = []
                if value == rows[5]:
                    for substring in value:
                        try:
                            if substring == "N" or substring == "E" or substring == "S" or substring == "W":
                               move.append(substring)
                        except:
                            #print("failed")
                            pass
                    true_data_row.append(move)
            #print([rows[0],tup,rows[2],room_items,move])
            for item_val in room_items:
                if item_val.equipped == "True":
                    item_val.equipped = True
                else:
                    item_val.equipped = False
                if item_val.equippable == "True":
                    item_val.equippable = True
                else:
                    item_val.equippable = False
                if item_val.spawnable == "True":
                    item_val.spawnable = True
                else:
                    item_val.spawnable = False
            #true_data_row = [val1,tup,val3,room_items,[hostile_obj],move]
            #print(true_data_row)
            data.append(true_data_row)
            #true_data_row = []
        #print(data)
        #print(item_data)
        def cleaner(bit):
            if bit != []:
                return True
            else:
                return False
        data = list(filter(cleaner, data))
        true_data = []
        for list_value in data:
            #print(list_value)
            room = Room(list_value[0],list_value[1],list_value[2],list_value[3],list_value[4],list_value[5])
            true_data.append(room)
        #print()
        #print("\n" * 3 + "Break")
        #print(true_data)
        return true_data
#plan_map,size = map_maker()
#debug_display_map(plan_map)
#start_pos,row = initialise_starter_pos(plan_map)
#print("\n" *3)
#debug_display_map(plan_map)
#print(start_pos,row)
#print(size)
#player_coords = (start_pos, row)
#rooms = initialise_rooms(plan_map, player_coords, rooms)
#print(rooms)
#for room in rooms:
    #print(room.coords, room.move, room.player_loc)
#save_map(rooms)
#rooms = load_map(rooms)
#print(rooms)
#print(start_pos)
# 180 for f-strings is the centre
def debug_display_player_map(rooms, size):
    string_map = ""
    for room in rooms:
        #print(room.player_loc, room.coords)
        if room.player_loc == True and room.hostiles == True:
            display_room = "[XO]"
        elif room.player_loc == True:
            display_room = "[O]"
        elif room.hostiles == True:
            #print(room.hostiles != False)
            display_room = "[X]"
        else:
            display_room = "[]"
        #print(room.player_loc,room.hostiles,room.coords,display_room)
        #print(room.coords, size)
        if room.coords[0] == size[0] - 1:
            #print(room.coords[0],size[0])
            if room.coords[1] == size[1]:
                string_map = string_map + display_room
            else:
                string_map = string_map + display_room + "\n" + "|| " * size[0] + "\n"
        else:
            string_map = string_map + display_room + "="
        #print(string_map)
    #print(size)
    return string_map
class Player:
    def __init__(self,coords,storage,items,stats):
        self.coords = coords
        self.storage = storage
        self.items = items
        self.stats = stats
    def move(self, rooms):
        move_choice = []
        #print("Poo")
        #print(rooms)
        for room in rooms:
            #print("why")
            #print(room.coords, self.coords, room.player_loc)
            #print(type(room.player_loc))
            if room.player_loc == True:
                #print("found")
                move_choice = room.move
        move_input = input(f"What direction would you like to move in? {move_choice} - \n")
        if move_input == "/cancel":
            return
        else:
            while move_input not in move_choice:
                move_input = input(f"You need to select one of the following. {move_choice} - \n")
                if move_input == "/cancel":
                    return
        if move_input in move_choice:
            prev_coords = self.coords
            if move_input == "N":
                self.coords = (self.coords[0],self.coords[1] - 1)
            elif move_input == "E":
                self.coords = (self.coords[0] + 1,self.coords[1])
            elif move_input == "S":
                self.coords = (self.coords[0],self.coords[1] + 1)
            else:
                self.coords = (self.coords[0] - 1,self.coords[1])
            for room in rooms:
                #print(room.coords, self.coords, room.player_loc)
                if room.coords == prev_coords:
                    #print("Previous Room")
                    room.player_loc = False
                if room.coords == self.coords:
                    room.discovered = True
                    room.player_loc = True
        return self
    def display_player_map(self, rooms, size):
        rows = {}
        size_index = list(size)
        size_index = size_index[0]
        size_row = list(size)
        size_row = size_row[1]
        for room in rooms:
            #room.discovered = True
            row = list(room.coords)
            index = row[0]
            row = row[1]
            #print(list(room.coords))
            try:
                rows[row]
            except:
                rows[row] = ""
            #print(room.coords)
            #print(room.discovered)
            #print(type(room.discovered))
            #print(room.player_loc)
            if room.player_loc == True and room.hostiles != []:
                if "E" in room.move and "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[XO]=")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "=[XO]="
                        #print(val)
                        rows[row] = val
                elif "E" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[XO]=")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "[XO]="
                        #print(val)
                        rows[row] = val
                elif "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[XO]")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "=[XO]"
                        #print(val)
                        rows[row] = val
                else:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[XO]")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "[XO]"
                        #print(val)
                        rows[row] = val
            elif room.player_loc == True:
                if "E" in room.move and "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[O]=")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "=[O]="
                        #print(val)
                        rows[row] = val
                elif "E" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[O]=")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "[O]="
                        #print(val)
                        rows[row] = val
                elif "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[O]")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "=[O]"
                        #print(val)
                        rows[row] = val
                else:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[O]")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "[O]"
                        #print(val)
                        rows[row] = val
            elif room.hostiles != []:
                if "E" in room.move and "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[X]=")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "=[X]="
                        #print(val)
                        rows[row] = val
                elif "E" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[X]=")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "[X]="
                        #print(val)
                        rows[row] = val
                elif "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[X]")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "=[X]"
                        #print(val)
                        rows[row] = val
                else:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[X]")
                        spacing = " " * (length - 1)
                        rows[row] = val + spacing
                    else:
                        val = val + "[X]"
                        #print(val)
                        rows[row] = val
            else:
                if "E" in room.move and "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[]=")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "=[]="
                        #print(val)
                        rows[row] = val
                elif "E" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[]=")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "[]="
                        #print(val)
                        rows[row] = val
                elif "W" in room.move:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("=[]")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "=[]"
                        #print(val)
                        rows[row] = val
                else:
                    val = rows[row]
                    if room.discovered == False:
                        length = len("[]")
                        spacing = " " * length
                        rows[row] = val + spacing
                    else:
                        val = val + "[]"
                        #print(val)
                        rows[row] = val
        #print(rows)
        True_map = {}
        verticals = {}
        for key in rows:
            #print(key)
            #print(size_row)
            if key == size_row:
                break
            top = False
            bottom = False
            verticals[key] = []
            ref = verticals[key]
            top_row = rows[key]
            if key + 1 > size_row:
                bottom_row = ""
            else:
                bottom_row = rows[key+1]
            top_row_list = list(top_row)
            #print(key)
            #print(top_row_list)
            bottom_row_list = list(bottom_row)
            #print(bottom_row_list)
            if len(top_row_list) > len(bottom_row_list):
                length = len(top_row_list)
            elif len(top_row_list) < len(bottom_row_list):
                length = len(bottom_row_list)
            else:
                length = len(top_row_list)
            #print(top,bottom)
            for i in range(0,length):
                try:
                    top_value = top_row_list[i]
                except:
                    if bottom_row == "":
                        bottom_value = ""
                        #print("bottom_value empty")
                    else:
                        bottom_value = bottom_row_list[i]
                else:
                    try:
                        if bottom_row == "":
                            bottom_value = ""
                            #print("bottom_value empty")
                        else:
                            bottom_value = bottom_row_list[i]
                    except:
                        pass
                #print(top_value, bottom_value)
                if top_value == "]" and bottom_value == "]":
                    ref.append("|")
                elif top_value == "]" and bottom_value == "=":
                    ref.append("/")
                elif top_value == "=" and bottom_value == "]":
                    ref.append("\\")
                elif top_value == "=" and bottom_value == "[":
                    ref.append("/")
                elif top_value == "[" and bottom_value == "=":
                    ref.append("\\")
                elif top_value == "[" and bottom_value == "[":
                    ref.append("|")
                elif top_value == "" and bottom_value == "[" or top_value == " " and bottom_value == "[" or top_value == "" and bottom_value == "]" or top_value == " " and bottom_value == "]":
                    ref.append("|")
                elif top_value == "[" and bottom_value == "" or top_value == "[" and bottom_value == " " or top_value == "]" and bottom_value == "" or top_value == "]" and bottom_value == " ":
                    ref.append("|")
                else:
                    ref.append(" ")
        #print(verticals)
        for key in rows:
            row = rows[key]
            try:
                vertical_row = verticals[key]
            except:
                print(row)
            else:
                print(row)
                for index, val in enumerate(vertical_row):
                    print(val, end="")
                    #print(index+1, len(row))
                    if index + 1 == len(vertical_row):
                        print(val)
    def check_inventory(self):
        user_input = input("Would you like to |[storage]| |[character]| |[stats]| |[cancel]| \n\n")
        print()
        while user_input != "storage" and user_input != "character" and user_input != "stats" and user_input != "cancel":
            user_input = input("Please select the following above!")
        if user_input == "storage":
            storage = self.storage
            num_str = 0
            items_str = None
            for items in self.items:
                if items.equipped == False:
                    num_str += 1
                    if items_str == None:
                        items_str = [items]
                    else:
                        items_str.append(items)
                    #print(items_str)
            if items_str == None:
                print("There are no items in storage \n")
                return
            print(str(num_str) + "/" + str(storage))
            for items in items_str:
                if isinstance(items.item_type, armour):
                    print(f"Name: {items.name}, Body-Type: {items.item_type.body_type}, Defense: {items.item_type.defense_stats}, Durability: {items.item_type.durability}, Storage: {items.item_type.storage}")
                elif isinstance(items.item_type, weapon):
                    if isinstance(items.item_type.weapon_type, melee):
                        print(f"Name: {items.name}, Wielding-Type: {items.item_type.wielding_type}, Damage: {items.item_type.attack_damage}, Durability: {items.item_type.attack_damage}, Length: {items.item_type.weapon_type.length}")
                    elif isinstance(items.item_type.weapon_type, ranged):
                        print(f"Name: {items.name}, Wielding-Type: {items.item_type.wielding_type}, Damage: {items.item_type.attack_damage}, Durability: {items.item_type.attack_damage}, Shots before reload: {items.item_type.weapon_type.magazine}")
            print("\n--------------------------------\n")
            user_input = input("Select the item you want by typing in the item's name. Enter 'cancel' if you want to exit the inventory tab. - ")
            if user_input == "cancel":
                return
            else:
                found = False
                for items in items_str:
                    #print(items.name , user_input)
                    if items.name == user_input:
                        found = True
                if found == False:
                    while found == False:
                        user_input = input("Couldn't find item. Please try again - ")
                        if user_input == "cancel":
                            return
                        for items in items_str:
                            if items.name == user_input:
                                found = True
                print()
                user_input_choice = input(f"Would you like to equip or discard {user_input} - ")
                while user_input_choice != "equip" and user_input_choice != "discard" and user_input_choice != "cancel":
                    user_input_choice = input("Equip or discard!? (or if you want cancel)")
                if user_input_choice == "cancel":
                    return
                elif user_input_choice == "equip":
                    select = None
                    for items in self.items:
                        if items.name == user_input:
                            select = items
                    occurence = 0
                    for items in self.items:
                        #print(items.name)
                        #print(occurence)
                        if occurence == 2:
                            print("You have 2 One Handed weapons so you can't equip this weapon. De-equip those to free up space for this weapon")
                            sleep(2)
                            return
                        if items.equipped == True:
                            #print("It's Equipped")
                            if type(items.item_type) == type(select.item_type):
                                #print("They're the same type")
                                if isinstance(select.item_type, armour):
                                    #print("Its armour")
                                    if items.item_type.body_type == select.item_type.body_type:
                                        print(str(items.item_type.body_type) + " armour has already been equipped. De-equip that to equip this.")
                                        sleep(2)
                                        return
                                elif isinstance(select.item_type, weapon):
                                    #print("Its a weapon")
                                    if items.item_type.wielding_type == "one_handed":
                                        if items.item_type.wielding_type == "one_handed" and select.item_type.wielding_type == "two_handed":
                                            print("The weapon you are trying to equip: " + str(select.name) + " cannot be equipped because its wielding-type is: " + str(select.item_type.wielding_type) + " and you already have a weapon equipped. De-equip that to equip this.")
                                            sleep(2)
                                            return
                                        #print("Room for 1 more")
                                        occurence += 1
                                    elif items.item_type.wielding_type == "two_handed" or occurence == 2:
                                        print("Weapon type: " + str(items.item_type.wielding_type) + " has already been equipped. De-equip that to equip this.")
                                        sleep(2)
                                        return
                    if occurence == 2:
                        print("You have 2 One Handed weapons so you can't equip this weapon. De-equip those to free up space for this weapon")
                        sleep(2)
                        return
                    select.equipped = True
                    Player.update_stats(self)
                elif user_input_choice == "discard":
                    length = len(items_str)
                    for index, items in enumerate(self.items):
                        if items.name == user_input:
                            self.items.pop(index)
        elif user_input == "character":
            print("\n")
            equipped = []
            for items in self.items:
                if items.equipped == True:
                    equipped.append(items)
            for items in equipped:
                if isinstance(items.item_type, armour):
                    #print(items.item_type.body_type)
                    print()
                    if items.item_type.body_type == "head":
                        print({"Head": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Defense - ", items.item_type.defense_stats, "Storage - ", items.item_type.storage]})
                        print()
                    elif items.item_type.body_type == "torso":
                        print({"Torso": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Defense - ", items.item_type.defense_stats, "Storage - ", items.item_type.storage]})
                        print()
                    elif items.item_type.body_type == "legs":
                        print({"Legs": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Defense - ", items.item_type.defense_stats, "Storage - ", items.item_type.storage]})
                        print()
                    elif items.item_type.body_type == "arms":
                        print({"Arms": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Defense - ", items.item_type.defense_stats, "Storage - ", items.item_type.storage]})
                        print()
                    elif items.item_type.body_type == "feet":
                        print({"Feet": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Defense - ", items.item_type.defense_stats, "Storage - ", items.item_type.storage]})
                        print()
                elif isinstance(items.item_type, weapon):
                    if isinstance(items.item_type.weapon_type, melee):
                        print({"Weapon": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Attack Damage - ", items.item_type.attack_damage, "Type - ", items.item_type.wielding_type, "Length - ", items.item_type.weapon_type.length]})
                        print()
                    elif isinstance(items.item_type.weapon_type, ranged):
                        print({"Weapon": ["Name - ", items.name, "Durability - ", items.item_type.durability, "Attack Damage - ", items.item_type.attack_damage, "Type - ", items.item_type.wielding_type, "Shots before reload - ", items.item_type.weapon_type.magazine]})
                        print()
            user_input_choice = input("Would you like to |[unequip]| |[cancel]|\n\n")
            while user_input_choice != "unequip" and user_input_choice != "cancel":
                user_input_choice = input("Please select one of the above!\n")
            if user_input_choice == "unequip":
                if abs(len(equipped) - len(self.items)) == self.storage:
                    print("Storage is full\n\n")
                    sleep(2)
                    return
                user_input = input("Type in the name of the item you want to unequip - ")
                found = None
                for items in equipped:
                    if items.name == user_input:
                        found = items
                        if isinstance(found.item_type, armour):
                            check_storage = found.item_type.storage
                            storage = 0
                            for items in self.items:
                                if items.equipped == False:
                                    storage += 1
                            if storage + 1 > self.storage - check_storage:
                                print("This will Exceed storage capacity and therefore cannot be done")
                                sleep(2)
                                return
                if found == None:
                    print("Item not found")
                    sleep(2)
                    return
                for items in self.items:
                    if items == found:
                        #print(True)
                        items.equipped = False
                Player.update_stats(self)
            elif user_input_choice == "cancel":
                return
            print("Item has been unequipped.")
            sleep(2)
        elif user_input == "stats":
            print("\n",self.stats,"\n")
            print()
            input("Type ENTER to continue. - ")
        #Player.update_stats(self)
    def update_stats(self):
        self.stats["Attack"] = 0
        self.stats["Defense"] = 0
        self.storage = 0
        storage = 0
        app_defense = []
        app_attack = []
        app_storage = []
        for items in self.items:
            if items.equipped == True:
                if isinstance(items.item_type, armour):
                    if type(items.item_type.defense_stats) == int:
                        defense = items.item_type.defense_stats
                    else:
                        defense = int(items.item_type.defense_stats)
                    if type(items.item_type.storage) == int:
                        storage = items.item_type.storage
                    else:
                        storage = int(items.item_type.storage)
                    app_defense.append(defense)
                    app_storage.append(storage)
                elif isinstance(items.item_type, weapon):
                    if type(items.item_type.attack_damage) == int:
                        attack = items.item_type.attack_damage
                    else:
                        attack = int(items.item_type.attack_damage)
                    app_attack.append(attack)
        if app_attack == []:
            self.stats["Attack"] = 0
        else:
            self.stats["Attack"] = reduce(lambda x,y: x+y, app_attack)
        if app_defense == []:
            self.stats["Defense"] = 0
        else:
            self.stats["Defense"] = reduce(lambda x,y: x+y, app_defense)
        #print(storage)
        if app_storage == []:
            self.storage = 0
        else:
            self.storage = reduce(lambda x,y: x+y, app_storage)
    def search_room(self, rooms):
        print()
        for room in rooms:
            if room.player_loc == True:
                room_items = room.items
                for items in room_items:
                    if isinstance(items.item_type, armour):
                        print(f"Name: {items.name}, Body-Type: {items.item_type.body_type}, Defense: {items.item_type.defense_stats}, Durability: {items.item_type.durability}, Storage: {items.item_type.storage}")
                    elif isinstance(items.item_type, weapon):
                        if isinstance(items.item_type.weapon_type, melee):
                            print(f"Name: {items.name}, Wielding-Type: {items.item_type.wielding_type}, Damage: {items.item_type.attack_damage}, Durability: {items.item_type.durability}, Length: {items.item_type.weapon_type.length}")
                        elif isinstance(items.item_type.weapon_type, ranged):
                            print(f"Name: {items.name}, Wielding-Type: {items.item_type.wielding_type}, Damage: {items.item_type.attack_damage}, Durability: {items.item_type.durability}, Shots before reload: {items.item_type.weapon_type.magazine}")
        print("\n")
        player_input_choice = input("Do you want to interact with these items? y/n - ")
        if player_input_choice == "n":
            return
        elif player_input_choice == "y":
            pass
        else:
            while player_input_choice != "y" and player_input_choice != "n":
                player_input_choice = input("You didnt type in \"y\" or \"n\". Please type it in. - ")
        while True:
            print()
            clear_shell()
            for room in rooms:
                if room.player_loc == True:
                    room_items = room.items
                    for items in room_items:
                        if isinstance(items.item_type, armour):
                            print(f"Name: {items.name}, Body-Type: {items.item_type.body_type}, Defense: {items.item_type.defense_stats}, Durability: {items.item_type.durability}, Storage: {items.item_type.storage}")
                        elif isinstance(items.item_type, weapon):
                            if isinstance(items.item_type.weapon_type, melee):
                                print(f"Name: {items.name}, Wielding-Type: {items.item_type.wielding_type}, Damage: {items.item_type.attack_damage}, Durability: {items.item_type.durability}, Length: {items.item_type.weapon_type.length}")
                            elif isinstance(items.item_type.weapon_type, ranged):
                                print(f"Name: {items.name}, Wielding-Type: {items.item_type.wielding_type}, Damage: {items.item_type.attack_damage}, Durability: {items.item_type.durability}, Shots before reload: {items.item_type.weapon_type.magazine}")
            print("\n")
            user_input = input("Please select an item from above to pick it up or type 'cancel' to return back to the room. \n")
            if user_input == "cancel":
                return
            else:
                found = False
                storage = 0
                for items in self.items:
                    if items.equipped == False:
                        storage += 1
                for ind_room in rooms:
                    if ind_room.player_loc == True:
                        for index, items in enumerate(ind_room.items):
                            if items.name == user_input:
                                found = True
                                if self.storage == storage:
                                    print("Player can't pick up item. Storage is full.")
                                    sleep(2)
                                else:
                                    print("Item picked up.\n")
                                    sleep(2)
                                    ind_item = ind_room.items.pop(index)
                                    self.items.append(ind_item)
                if found == False:
                    print("Item wasn't found. Please Enter its name correctly.")
                    sleep(2)
    def deal_damage(self):
        pass
        #finds the hostile in the same room as the player, receives the damage multiplier from countdown and applies damage based on the multiplier and the players attack_damage stats


#string_map = debug_display_player_map(rooms,size)
#print("\n" * 3)
#print(string_map)
#player.move()
#string_map = debug_display_player_map(rooms,size)
#print("\n" * 3)
#print(string_map)
#gun = item(True,True).weapon("one_handed", 50, None).ranged(6)
#print(gun.magazine)
#starter_shirt = item("Commoner's Shirt",True,False,False,None,item.armour("torso",0,50,3))
#starter_trousers = item("Commoner's Trousers",True,False,False,None,item.armour("legs",0,50,3))
#starter_shoes = item("Commoner's Shoes",True,False,False,None,item.armour("Feet",0,25,0))
#fists = item("Bare Fists",True,False,False,None,item.weapon("two_handed",3,None,item.weapon.melee(20)))
#print(fists.item_type.weapon_type.length) #prints 20
#stick = item("Wooden Stick",True,False,True,25,item.weapon("one_handed",5,20,item.weapon.melee(40)))
#rusty_dagger = item("Rusty Dagger",True,False,True,25,item.weapon("one_handed",6,25,item.weapon.melee(25)))
#dull_iron_dagger = item("Dull Iron Dagger",True,False,True,25,item.weapon("one_handed",8,60,item.weapon.melee(25)))
#iron_dagger = item("Iron Dagger",True,False,True,25,item.weapon("one_handed",12,100,item.weapon.melee(25)))
#aristocrat_dagger = item("Aristocrat Dagger", True,False,True,25,item.weapon("one_handed",18,250,item.weapon.melee(30)))
#rusty_longsword = item("Rusty Longsword",True,False,True,25,item.weapon("two_handed",3,50,item.weapon.melee(50)))
#dull_iron_longsword = item("Dull Iron Longsword", True,False,True,25,item.weapon("two_handed",6,100,item.weapon.melee(50)))
#iron_longsword = item("Iron Longsword",True,False,True,25,item.weapon("two_handed",9,150,item.weapon.melee(50)))
#aristocrat_longsword = item("Aristocrat Longsword",True,False,True,25,item.weapon("two_handed",15,400,item.weapon.melee(50)))
#print(starter_shirt.item.name)
#game_items = [fists,stick,rusty_dagger,dull_iron_dagger,iron_dagger,aristocrat_dagger,rusty_longsword,dull_iron_longsword,iron_longsword,aristocrat_longsword]
def room_item_giver(game_items,rooms):
    for room in rooms:
        room.items = []
        for item_val in game_items:
            if item_val.spawnable == False:
                continue
            probability = item_val.spawn_probability
            num_choice = randint(1,100)
            #print(num_choice)
            try:
                if probability >= num_choice:
                    #print(probability,num_choice)
                    #print(item.name,room.coords)
                    room.items.append(item_val)
            #print(room.items)
            except:
                pass
    return rooms

#rooms = room_item_giver(game_items,rooms)

import os

def running_program():
    def save_data(size,player):
        with open("ROOM_Data.csv", "w") as file:
            writer = csv.writer(file)
            data = []
            data.append([size])
            items = {}
            for ind_item in player.items:
                length = len(items)
                if isinstance(ind_item.item_type, armour):
                    items[length] = [ind_item.name, ind_item.equippable, ind_item.equipped, ind_item.spawnable, ind_item.spawn_probability, ind_item.item_type.body_type, ind_item.item_type.defense_stats, ind_item.item_type.durability, ind_item.item_type.storage]
                elif isinstance(ind_item.item_type, weapon):
                    if isinstance(ind_item.item_type.weapon_type, melee):
                        items[length] = [ind_item.name, ind_item.equippable, ind_item.equipped, ind_item.spawnable, ind_item.spawn_probability, ind_item.item_type.wielding_type, ind_item.item_type.attack_damage, ind_item.item_type.durability, ind_item.item_type.weapon_type.length]
                    elif isinstance(ind_item.item_type.weapon_type, ranged):
                        items[length] = [ind_item.name, ind_item.equippable, ind_item.equipped, ind_item.spawnable, ind_item.spawn_probability, ind_item.item_type.wielding_type, ind_item.item_type.attack_damage, ind_item.item_type.durability, ind_item.item_type.weapon_type.magazine]
            data.append([player.coords,player.storage,items,player.stats])
            writer.writerows(data)
    def load_data(game_items):
        def cleaning(piece):
            if piece != "," and piece != "\\" and piece != "{" and piece != "}" and piece != "[" and piece != "]" and piece != "'" and piece != "\"":
                return True
        with open("ROOM_Data.csv", "r") as file:
            reader = csv.reader(file)
            size = ()
            coords = None
            storage = None
            items = None
            stats = None
            n=0
            for rows in reader:
                if n == 0:
                    numbers = []
                    for value in rows:
                        for substring in value:
                            #print(substring)
                            try:
                                int(substring)
                            except:
                                if substring == ",":
                                    numbers.append(substring)
                            else:
                                numbers.append(substring)
                    #print(numbers)
                    range_length = len(numbers)
                    first_set = 0
                    second_set = 0
                    i = numbers.index(",") + 1
                    flag = True
                    for number in numbers:
                        if flag == True:
                            if number != ",":
                                if first_set == 0:
                                    first_set = number
                                else:
                                    first_set = first_set + number
                            else:
                                flag = False
                        else:
                            continue
                    for I in range(i,range_length):
                        number = numbers[I]
                        if second_set == 0:
                            second_set = number
                        else:
                            second_set = second_set + number
                    first_set = int(first_set)
                    second_set = int(second_set)
                    #print(first_set, second_set)
                    tup = (first_set, second_set)
                    #print(tup)
                    size = tup
                    numbers = []
                    tup = ()
                    first_set = ""
                    second_set = ""
                else:
                    i = 0
                    for value in rows:
                        #print(value)
                        if i == 0:
                            #print("making coords")
                            for substring in value:
                                #print(i)
                                #print(substring)
                                try:
                                    int(substring)
                                except:
                                    if substring == ",":
                                        numbers.append(substring)
                                else:
                                    numbers.append(substring)
                            #print(numbers)
                            range_length = len(numbers)
                            first_set = 0
                            second_set = 0
                            ind = numbers.index(",") + 1
                            flag = True
                            for number in numbers:
                                if flag == True:
                                    if number != ",":
                                        if first_set == 0:
                                            first_set = number
                                        else:
                                            first_set = first_set + number
                                    else:
                                        flag = False
                                else:
                                    continue
                            for I in range(ind,range_length):
                                number = numbers[I]
                                if second_set == 0:
                                    second_set = number
                                else:
                                    second_set = second_set + number
                            first_set = int(first_set)
                            second_set = int(second_set)
                            #print(first_set, second_set)
                            tup = (first_set, second_set)
                            #print(tup)
                            coords = tup
                            i += 1
                        elif i == 1:
                            try:
                                storage = int(value)
                            except:
                                storage = value
                            i +=1
                        elif i == 2:
                            str_items = value
                            #print(str_items)
                            str_list = str_items.split()
                            fixed_list = []
                            #print(str_list)
                            for string in str_list:
                                #print(string)
                                string = list(filter(cleaning, string))
                                fixed_list.append(string)
                            #print(fixed_list)
                            combined_list = []
                            for pair in fixed_list:
                                pair = reduce(lambda x, y: x+y , pair)
                                combined_list.append(pair)
                            def converter(value):
                                if ":" in value:
                                    return value
                                if value == "True":
                                    return True
                                elif value == "False":
                                    return False
                                elif value == "None":
                                    return None
                                else:
                                    try:
                                        int(value)
                                    except:
                                        return value
                                    else:
                                        return int(value)
                            #print(combined_list)
                            converted_list = list(map(converter, combined_list))
                            true_list = []
                            ind_1 = 0
                            ind_2 = 0
                            for value in converted_list:
                                try:
                                    if ":" in value:
                                        ind_1 = converted_list.index(value) + 1
                                        ind_2 = ind_1 + 1
                                        name_1 = converted_list[ind_1]
                                        name_2 = converted_list[ind_2]
                                        new_name = name_1 + " " + name_2
                                        if new_name == "Commoners Shirt":
                                            new_name = "Commoner's Shirt"
                                        elif new_name == "Commoners Shoes":
                                            new_name = "Commoner's Shoes"
                                        elif new_name == "Commoners Trousers":
                                            new_name = "Commoner's Trousers"
                                        #print(new_name)
                                        true_list.append(value)
                                        true_list.append(new_name)
                                    elif converted_list[ind_1] == value or converted_list[ind_2] == value:
                                        continue
                                    else:
                                        true_list.append(value)
                                except:
                                    #print(E)
                                    true_list.append(value)
                            #print(true_list)
                            #print(converted_list)
                            current_item = []
                            player_items = []
                            true_list.append(":")
                            #print(true_list)
                            for val in true_list:
                                #print(val)
                                if type(val) == str:
                                    if ":" in val:
                                        if current_item == []:
                                            continue
                                        else:
                                            for items in game_items:
                                                if current_item == []:
                                                    continue
                                                #print(current_item)
                                                if items.name == current_item[0]:
                                                    if isinstance(items.item_type, armour): #5,4 len:9
                                                            #print(current_item)
                                                            Armour = armour(current_item[5], current_item[6], current_item[7], current_item[8])
                                                            appending_item = item(current_item[0],current_item[1], current_item[2], current_item[3], current_item[4], Armour)
                                                            current_item = []
                                                            player_items.append(appending_item)
                                                    elif isinstance(items.item_type, weapon): #5,3,1 len:9
                                                        if isinstance(items.item_type.weapon_type, melee):
                                                            print(current_item, len(current_item))
                                                            Melee = melee(current_item[8])
                                                            Weapon = weapon(current_item[5], current_item[6], current_item[7], Melee)
                                                            appending_item = item(current_item[0], current_item[1], current_item[2], current_item[3],current_item[4], Weapon)
                                                            current_item = []
                                                            player_items.append(appending_item)
                                                        if isinstance(items.item_type.weapon_type, ranged):
                                                            Ranged = ranged(current_item[8])
                                                            Weapon = weapon(current_item[5], current_item[6], current_item[7], Ranged)
                                                            appending_item = item(current_item[0],current_item[1], current_item[2], current_item[3], current_item[4], Weapon)
                                                            current_item = []
                                                            player_items.append(appending_item)
                                    else:
                                        current_item.append(val)
                                else:
                                    current_item.append(val)
                            i +=1
                        elif i == 3:
                            str_list = value.split()
                            cleaned_list = []
                            def new_cleaning(piece):
                                if piece != "," and piece != "\\" and piece != "{" and piece != "}" and piece != "[" and piece != "]" and piece != "'" and piece != "\"" and piece != ":":
                                    return True
                            for val in str_list:
                                new_val = list(filter(new_cleaning, val))
                                cleaned_list.append(new_val)
                            #print(cleaned_list)
                            fixed_list = []
                            for bunch in cleaned_list:
                                new_bunch = reduce(lambda x,y:x+y, bunch)
                                fixed_list.append(new_bunch)
                            #print(fixed_list)
                            true_list = []
                            for val in fixed_list:
                                try:
                                    new_val = int(val)
                                    true_list.append(new_val)
                                except:
                                    true_list.append(val)
                            #print("----------------",true_list,"--------------------")
                            true_dict = {}
                            for index, val in enumerate(true_list):
                                if index != 0 and index != 1 and true_list[index - 1] == "Max" or true_list[index - 2] == "Max":
                                    continue
                                elif index % 2 == 0 and true_list[index] != "Max" and true_list[index - 1] != "Energy":
                                    #print("Its a key")
                                    true_dict[val] = ""
                                else:
                                    if index % 2 == 0:
                                        key_index = index
                                    else:
                                        key_index = index - 1
                                    if true_list[key_index] == "Max" and true_list[key_index+1] == "Energy":
                                        #print("found the pair")
                                        new_key = "Max Energy"
                                        new_val = true_list[key_index + 2]
                                        true_dict[new_key] = new_val
                                    else:
                                        #print("not the pair")
                                        key = true_list[key_index]
                                        true_dict[key] = val
                            #print("/////////----------",true_dict,"----------\\\\\\")
                            player = Player(coords,storage,player_items,true_dict)
                            i +=1
                n += 1
            try:
                return size, player
            except:
                return None, None
    import platform
    #clear_shell()
    def initialise_hostiles(hostiles,rooms,size):
        length = list(size)[1]
        #print("------"*50,length,"------"*50)
        gargoyle_spawned = False
        for ind_room in rooms:
            #print(list(ind_room.coords)[1], length)
            for ind_hostile in hostiles:
                spawning = False
                #print("Room row: ", list(ind_room.coords)[1])
                #print("Length: ", length)
                if ind_hostile.hostile_type.name == "Gargoyle":
                    if list(ind_room.coords)[1] != 1:
                        continue
                    if gargoyle_spawned == True:
                        continue
                    spawning = randint(1,100) <= ind_hostile.spawn_chance
                    if list(size)[0] == ind_room.coords[0] + 1:
                        spawning = True
                elif ind_hostile.hostile_type.name == "Goblin" and list(ind_room.coords)[1] != length and list(ind_room.coords)[1] != length - 1:
                    spawning = randint(1,100) <= ind_hostile.spawn_chance
                elif ind_hostile.hostile_type.name == "Hellhound" and list(ind_room.coords)[1] != length and list(ind_room.coords)[1] != length - 1 and list(ind_room.coords)[1] != length - 2 and list(ind_room.coords)[1] != length - 3:
                    #print([length, length - 1, length - 2, length - 3])
                    spawning = randint(1,100) <= ind_hostile.spawn_chance
                if spawning == True:
                    #print(ind_room.coords, ind_hostile.hostile_type.name)
                    ind_room.hostiles.append(ind_hostile)
        return rooms
    print("[MAIN-MENU]\n\n")
    print("Enter /load to load your game. \n\n")
    print("Enter /new to start a new game. \n\n")
    print("Enter /leave to exit. \n\n")
    user_main_menu_choice = input()
    while user_main_menu_choice != "/load" and user_main_menu_choice != "/new" and user_main_menu_choice != "/leave":
        user_main_menu_choice = input("There is no available command, please try again. - \n\n")
    if user_main_menu_choice == "/load":
        #clear_shell()
        rooms = []
        size = []
        player = []
#print(starter_shirt.item.name)
        starter_shirt = item("Commoner's Shirt",True,True,False,False,armour("torso",0,50,3))
        starter_trousers = item("Commoner's Trousers",True,True,False,False,armour("legs",0,50,3))
        starter_shoes = item("Commoner's Shoes",True,True,False,False,armour("feet",0,25,0))
        fists = item("Bare Fists",True,True,False,False,weapon("two_handed",3,False,melee(20)))
#print(fists.item_type.weapon_type.length) #prints 20
        stick = item("Wooden Stick",True,False,True,75,weapon("one_handed",5,20,melee(40)))
        rusty_dagger = item("Rusty Dagger",True,False,True,50,weapon("one_handed",6,25,melee(25)))
        dull_iron_dagger = item("Dull Dagger",True,False,True,45,weapon("one_handed",8,60,melee(25)))
        iron_dagger = item("Iron Dagger",True,False,True,35,weapon("one_handed",12,100,melee(25)))
        aristocrat_dagger = item("Aristocrat Dagger",True,False,True,15,weapon("one_handed",18,250,melee(30)))
        rusty_longsword = item("Rusty Longsword",True,False,True,70,weapon("two_handed",3,50,melee(50)))
        dull_iron_longsword = item("Dull Longsword", True,False,True,50,weapon("two_handed",6,100,melee(50)))
        iron_longsword = item("Iron Longsword",True,False,True,20,weapon("two_handed",9,150,melee(50)))
        aristocrat_longsword = item("Aristocrat Longsword",True,False,True,10,weapon("two_handed",15,400,melee(50)))
        leather_helmet = item("Leather Helmet", True, False,True, 40,armour("head",5,75,0))
        leather_chestplate = item("Leather Chestplate", True, False, True, 40, armour("torso",5,100,3))
        leather_trousers = item("Leather Trousers", True, False, True, 40, armour("legs",5,75,1))
        leather_shoes = item("Leather Shoes", True, False, True, 40, armour("feet", 5, 50, 0))
        iron_helmet = item("Iron Helmet", True, False, True, 20, armour("head", 10, 100, 0))
        iron_chestplate = item("Iron Chestplate", True, False, True, 20, armour("torso", 10, 150, 3))
        iron_trousers = item("Iron Trousers", True, False, True, 20, armour("legs", 10, 100, 0))
        iron_shoes = item("Iron Shoes", True, False, True, 20, armour("feet", 10, 75, 0))
        bow = item("Ranger Bow", True, False, True, 20, weapon("one_handed",10, 500, ranged(1)))
        revolver = item("Golden Revolver", True, False, True, 10, weapon("one_handed", 20, 10000, ranged(6)))
        player = Player((0,0),6,[starter_shirt, starter_trousers,starter_shoes,fists],{"Attack": 3, "Defense": 0, "HP": 100, "Energy": 100, "Max Energy": 100})
#print(starter_shirt.item.name)
        game_items = [fists,stick,rusty_dagger,dull_iron_dagger,iron_dagger,aristocrat_dagger,rusty_longsword,dull_iron_longsword,iron_longsword,aristocrat_longsword,starter_shirt,starter_trousers,starter_shoes, leather_helmet, leather_chestplate, leather_trousers, leather_shoes, iron_helmet, iron_chestplate, iron_trousers, iron_shoes, bow, revolver]
        goblin = hostile({"Attack": 3, "Defense": 2, "HP": 60}, hostile.goblins("Goblin"), 0.1, 25)
        hellhound = hostile({"Attack": 5, "Defense": 4, "HP": 120}, hostile.hellhounds("Hellhound"), 0.05, 10)
        gargoyle = hostile({"Attack": 7, "Defense": 6, "HP": 200}, hostile.gargoyles("Gargoyle"), 0.05, 10)
        hostiles = [goblin, hellhound,gargoyle]
        true_data = load_map(rooms, game_items, hostiles)
        rooms = true_data
        #print(rooms)
        size, player = load_data(game_items)
        #print(player.coords)
        running = True
    elif user_main_menu_choice == "/new":
        clear_shell()
        running = True
        plan_map, size = map_maker()
        #print(plan_map, size)
        start_pos,row = initialise_starter_pos(plan_map)
        player_coords = (start_pos,row)
        #print(player_coords)
        rooms = []
        rooms = initialise_rooms(plan_map,player_coords,rooms)
        #print(rooms)
        #for room in rooms:
            #print(room.coords)
        starter_shirt = item("Commoner's Shirt",True,True,False,False,armour("torso",0,50,3))
        starter_trousers = item("Commoner's Trousers",True,True,False,False,armour("legs",0,50,3))
        starter_shoes = item("Commoner's Shoes",True,True,False,False,armour("feet",0,25,0))
        fists = item("Bare Fists",True,True,False,False,weapon("two_handed",3,False,melee(20)))
#print(fists.item_type.weapon_type.length) #prints 20
        stick = item("Wooden Stick",True,False,True,75,weapon("one_handed",5,20,melee(40)))
        rusty_dagger = item("Rusty Dagger",True,False,True,50,weapon("one_handed",6,25,melee(25)))
        dull_iron_dagger = item("Dull Dagger",True,False,True,45,weapon("one_handed",8,60,melee(25)))
        iron_dagger = item("Iron Dagger",True,False,True,35,weapon("one_handed",12,100,melee(25)))
        aristocrat_dagger = item("Aristocrat Dagger",True,False,True,15,weapon("one_handed",18,250,melee(30)))
        rusty_longsword = item("Rusty Longsword",True,False,True,70,weapon("two_handed",3,50,melee(50)))
        dull_iron_longsword = item("Dull Longsword", True,False,True,50,weapon("two_handed",6,100,melee(50)))
        iron_longsword = item("Iron Longsword",True,False,True,20,weapon("two_handed",9,150,melee(50)))
        aristocrat_longsword = item("Aristocrat Longsword",True,False,True,10,weapon("two_handed",15,400,melee(50)))
        leather_helmet = item("Leather Helmet", True, False,True, 40,armour("head",5,75,0))
        leather_chestplate = item("Leather Chestplate", True, False, True, 40, armour("torso",5,100,3))
        leather_trousers = item("Leather Trousers", True, False, True, 40, armour("legs",5,75,1))
        leather_shoes = item("Leather Shoes", True, False, True, 40, armour("feet", 5, 50, 0))
        iron_helmet = item("Iron Helmet", True, False, True, 20, armour("head", 10, 100, 0))
        iron_chestplate = item("Iron Chestplate", True, False, True, 20, armour("torso", 10, 150, 3))
        iron_trousers = item("Iron Trousers", True, False, True, 20, armour("legs", 10, 100, 0))
        iron_shoes = item("Iron Shoes", True, False, True, 20, armour("feet", 10, 75, 0))
        bow = item("Ranger Bow", True, False, True, 20, weapon("one_handed",10, 500, ranged(1)))
        revolver = item("Golden Revolver", True, False, True, 10, weapon("one_handed", 20, 10000, ranged(6)))
        player = Player(player_coords,6,[starter_shirt, starter_trousers,starter_shoes,fists],{"Attack": 3, "Defense": 0, "HP": 100, "Energy": 100, "Max Energy": 100})
#print(starter_shirt.item.name)
        game_items = [fists,stick,rusty_dagger,dull_iron_dagger,iron_dagger,aristocrat_dagger,rusty_longsword,dull_iron_longsword,iron_longsword,aristocrat_longsword,starter_shirt,starter_trousers,starter_shoes, leather_helmet, leather_chestplate, leather_trousers, leather_shoes, iron_helmet, iron_chestplate, iron_trousers, iron_shoes, bow, revolver]
        rooms = room_item_giver(game_items,rooms)
        goblin = hostile({"Attack": 12, "Defense": 5, "HP": 60}, hostile.goblins("Goblin"), 0.1, 25)
        hellhound = hostile({"Attack": 15, "Defense": 10, "HP": 120}, hostile.hellhounds("Hellhound"), 0.05, 10)
        gargoyle = hostile({"Attack": 20, "Defense": 20, "HP": 200}, hostile.gargoyles("Gargoyle"), 0.05, 10)
        hostiles = [goblin, hellhound,gargoyle]
        #print(hostiles)
        rooms = initialise_hostiles(hostiles, rooms, size)
        print(".", end="", flush=True)
        sleep(1.5)
        print(".", end="", flush=True)
        sleep(1.5)
        print(".", end="\n", flush=True)
        game_delay_print("You wake up...", False,0.3)
        game_delay_print("You take a quick glance around the room.", False, 0.25)
        game_delay_print("Grey concrete walls, Brown mosaic tiles and no windows.", False, 0.2)
        game_delay_print("However", False, 0.5)
        game_delay_print("Something stood out to you", False, 0.1)
        game_delay_print("A brown oak door, light was peering through...", False, 0.1)
        game_delay_print("That was when...", False, 0.05)
        sleep(0.5)
        message = "\n[" + " " * 48 + "]\n" + " " * 3 + "You have received a new message from {ADMIN}" + " " * 3 + "\n[" + " " * 48 + "]\n"
        print(f"{message}")
        sleep(2)
        game_delay_print("[ Would you like to open or ignore the message? ]", False, 0.1)
        game_delay_print("You: Open", False,0.2)
        game_delay_print("To your dismay, the message is empty. Whoever sent it must've had the intention of discouraging you.", False, 0.1)
        game_delay_print("Whatever the case", False, 0.2)
        game_delay_print("You need to find a way out of here, so you should probably do exactly that.", False, 0.05)
        game_delay_print("You walk towards the oak door and open it, only to find yourself in the same room.", False, 0.1)
        game_delay_print("The only difference this time is...", False, 0.1)
        game_delay_print("There are 3 doors...", False,0.2)
        game_delay_print("[THIS IS WHERE YOU START]", False, 0.3)
        game_delay_print("\n" * 45, False, 0.001)
        save_map(rooms)
        rooms = load_map(rooms, game_items, hostiles)
        save_data(size,player)
        size, player = load_data(game_items)
    clear_shell()
    hostile_encounter = False
    while running == True:
        clear_shell()
        #for ind_room in rooms:
            #if ind_room.hostiles != [False]:
            #print(ind_room.hostiles)
            #print(ind_room.coords)
        game_delay_print("You are in a room full of various furniture:", False, 0.05)
        if hostile_encounter == True:
            for ind_room in rooms:
                if ind_room.player_loc == True and ind_room.hostiles != []:
                    curr_hostile = ind_room.hostiles
                    #print("Coords:", ind_room.coords,"Player_coords:", player.coords, "Hostile:", ind_room.hostiles, "Player_loc:", ind_room.player_loc)
            #print(curr_hostile)
            #print(type(curr_hostile))
            if isinstance(curr_hostile, list):
                hostile_encounter = curr_hostile[0].hostile_type.encounter(player, hostiles, rooms)
            elif isinstance(curr_hostile, hostile):
                hostile_encounter = curr_hostile.hostile_type.encounter(player, hostiles, rooms)
            #else:
                #print("Could'nt define")
                #print(curr_hostile)    
        if hostile_encounter == True:
            return
        elif hostile_encounter == "end":
            game_delay_print("You've slain the gargoyle, you're most formidable enemy yet...", False, 0.01)
            game_delay_print("But...", False, 0.05)
            game_delay_print("As he fell, you couldn't help but notice...", False, 0.05)
            game_delay_print("The wooden hatch behind the creature.", False, 0.01)
            game_delay_print("You acted instinctively stepping over the lifeless creature's body...", False, 0.01)
            game_delay_print("Flinging open the hatch, you loom your eyes over the dark abyss.", False, 0.01)
            game_delay_print("A staircase leading into the unknown dark lay ahead of you.", False, 0.01)
            game_delay_print("You tread carefully down the steps, awaiting any fate that will befall before you...", False, 0.01)
            game_delay_print("|[THE TRUE END]|", False, 0.2)
        print()
        game_delay_print("Would you like to |[move]| |[inventory]| |[search]| |[map]| |[main-menu]|", False, 0.05)   
        user_room_input = input()
        #debug_display_player_map(rooms, size)
        clear_shell()
        if user_room_input == "move":
            player.move(rooms)
            player.display_player_map(rooms, size)
            input("Type \"ENTER\" to Continue.")
            for ind_room in rooms:
                if ind_room.player_loc == True:
                    if ind_room.hostiles != []:
                        #print("App hostile here ------>", ind_room.hostiles)
                        hostile_encounter = True
        elif user_room_input == "search":
            player.search_room(rooms)
        elif user_room_input == "inventory":
            player.check_inventory()
        elif user_room_input == "map":
            player.display_player_map(rooms, size)
            input("Type \"ENTER\" to Continue.")
        elif user_room_input == "main-menu":
            print("[MAIN-MENU]\n\n")
            print("Enter /leave to save and exit. \n\n")
            print("Enter /return to return. \n\n")
            print("Enter /save to save your game. \n\n")
            user_main_menu_choice = input()
            while user_main_menu_choice != "/leave" and user_main_menu_choice != "/return" and user_main_menu_choice != "/save":
                user_main_menu_choice = input("There is no available command, please try again. - \n\n")
            if user_main_menu_choice == "/leave":
                save_data(size, player)
                save_map(rooms)
                return
            elif user_main_menu_choice == "/save":
                save_data(size, player)
                save_map(rooms)
running_program()

