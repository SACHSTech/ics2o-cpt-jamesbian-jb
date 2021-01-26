import time
import random
import sys
from playsound import playsound



# Make sure that all commands input are capital case
# The training allows the spell with a cool down to be used twice
# This is on purpose as to let you try the move more

def introduction():
    time.sleep(2)
    print("It all began when you heard the tale of the legendary dungeon in town.")
    time.sleep(3)
    print(
        "The old men whispered about the treasures inside, and the amount of ladies one would \n attract just by reaching the end, and capturing the legendary pufferfish of the dungeon. ")
    time.sleep(4)
    print("Without any wait, you head into the dungeon, hoping to \nbecome the most popular man on earth...")
    time.sleep(4.5)
    print("Loading...")
    time.sleep(5)

    print(name, ", your first enemy is the training dummy to practice your moves.")
    time.sleep(3)
    print("Your first move is slash.")
    time.sleep(3)
    print("Slash is a melee attack with your blade, where you deal 10 damage \n to enemies without armour.")
    time.sleep(4)

def scary_rock():
    prayer = 8
    cooldown = 3
    rock_hp = 170
    burn = 20
    prayer_buff = 0
    slash = 10
    name_hp = 100
    magic_type_1 = ""
    Glaciate_rng = 10
    # if boost == "Attack":
    #     slash = 12
    # if boost == "Health":
    #     name_hp = 102
    print("You encounter an armoured Gargoyle, looming over the large corridor!")
    time.sleep(2)
    while rock_hp > 0:
        time.sleep(1)
        print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat_c = input("")
        if combat_c != "Slash" and combat_c != "Magic" and combat_c != "Prayer":
            print("Let's use an actual action. ")
            time.sleep(2)
            print("What move will you use? ")
            print("Slash, Magic, Prayer: ")
            combat_c = input("").lower()

        if combat_c == "Slash":
            print("")
            print("You slashed the gargoyle for damage!")
            time.sleep(2)
            print("Gargoyle hp:", rock_hp - slash / 2)
            rock_hp = rock_hp - slash / 2
            if prayer_buff > 8:
                print("")
                print("You slashed the Gargoyle for some damage! (Empowered due to prayer)")
                print("Gargoyle hp:", rock_hp - slash)
                rock_hp = rock_hp - (slash + 2)
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
                print("you burned the Gargoyle for 20 damage!")
                rock_hp = rock_hp - burn
                print("Gargoyle hp: ", rock_hp)
                if cooldown % 3 != 0:
                    print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)
                    cooldown = cooldown + 1

            elif magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 7:
                    print("You froze the Gargoyle!")
                elif Glaciate_rng > 7:
                    print("Glaciate failed!")
                    time.sleep(2)

            print("")
        elif combat_c == "Prayer":
            print("")
            print("You healed for 8 hp")
            time.sleep(1)
            print(name, "'s hp: ", name_hp + prayer)
            prayer_buff = random.randint(1, 10)
            if prayer_buff > 8:
                print("Your attack damage also got buffed!")

        if Glaciate_rng < 7:
            print("The Gargoyle was frozen!")
            time.sleep(1)
            print("He can't move!")
        elif Glaciate_rng > 7:
            print("The Gargoyle slams you for 11 damage!")
            time.sleep(1)
            print("Your hp: ", name_hp)
        else:
            print("Let's use an actual action")
        if rock_hp <= 0:
            break
        if name_hp <= 0:
            time.sleep(1)
            print("You died a sad an painful death, forgotten in the depths of  the dungeon. ")
            time.sleep(2)

def hobgoblin():
    cooldown = 3
    hobgoblin_hp = 100
    slash = 10
    burn = 20
    prayer_buff = 0
    name_hp = 100
    magic_type_1 = ""
    prayer = 8

    print("You encounter a Hobgoblin, guarding the entrance to the next room!")
    time.sleep(1.5)
    while hobgoblin_hp > 0:
        print("What move will you use? ")
        time.sleep(2)
        print("Slash, Magic, Prayer: ")
        prayer_move = False
        combat_c = input("")

        if combat_c == "Slash":
            print("")
            print("You slashed the hobgoblin for  some damage!")
            time.sleep(2)
            print("hobgoblin hp:", hobgoblin_hp - slash)
            hobgoblin_hp = hobgoblin_hp - slash
            if prayer_buff > 8:
                print("")
                print("You slashed the Hobgoblin for some damage! (Empowered due to prayer)")
                print("Gargoyle hp:", hobgoblin_hp - slash)
                hobgoblin_hp = hobgoblin_hp - (slash + 2)
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
                print("you burned the hobgoblin for 20 damage!")
                hobgoblin_hp = hobgoblin_hp - burn
                print("Hobgoblin hp: ", hobgoblin_hp)
                if cooldown % 3 != 0:
                    print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)
                    cooldown = cooldown + 1
            elif magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 7:
                    print("You froze the Hobgoblin!")
                elif Glaciate_rng > 7:
                    print("Glaciate failed!")
                    time.sleep(2)

        print("")
        if combat_c == "Prayer":
            prayer_move = True
            print("")
            print("You healed for 8 hp")
            time.sleep(1)
            print("Your hp: ", name_hp + prayer)
            name_hp = name_hp + prayer
            prayer_buff = random.randint(1, 10)
            if prayer_buff > 8:
                print("Your attack damage also got buffed!")

        if magic_type_1 != "Glaciate" or prayer_move == False:
            print("The hobgoblin smacked you for some damage!")
            time.sleep(2)
            name_hp = name_hp - 8
            print("Your hp: ", name_hp)

        if name_hp <= 0:
            time.sleep(1)
            print("You died a sad an painful death, forgotten in the depths of  the dungeon. ")
            time.sleep(2)
            sys.exit()

def dummy():
    print("")
    print("What move will you use? ")
    print("Slash, Magic, Prayer: ")
    combat = input("")
    dummy_hp = 99999
    while combat != "Slash":
        print("I said we doin slash today.")
        time.sleep(1.5)
        print("")
        print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat = input("")
    if combat == "Slash":
        slash = 10
        dummy_hith = dummy_hp - slash
        print("")
        print("You slashed the dummy for 10 damage!")
        print("dummy hp:", dummy_hith)
        time.sleep(2)
    print("")
    print("Your next move is Magic.")
    time.sleep(2)
    print("Currently, you have 2 magic skills: Glaciate, and Incinerate.")
    time.sleep(2)
    print("Glaciate freezes the target for 1 turn, but deals no damage, and has a chance to fail.")
    time.sleep(3.5)
    print("Incinerate ignites the enemy, dealing 20 damage, but can only be used once every 3 turns.")
    time.sleep(2.5)
    print("Try one of the spells on the dummy right now.")
    time.sleep(1)

    print("")
    print("What move will you use? ")
    print("Slash, Magic, Prayer: ")
    combat_a = input("")
    while combat_a != "Magic":
        print("I said we doin Magic today.")
        time.sleep(1.5)
        print("")
        print("What move will you use? ")
        print("Slash, Magic, Prayer, talk: ")
        combat_a = input("")
    if combat_a == "Magic":
        burn = 20
        dummy_hith_2 = dummy_hith - burn
        print ("Incinerate or Glaciate: ")
        magic_type = input("")
        while combat_a != "Incinerate" or "Glaciate":
            print("I said we doin Magic today.")
            time.sleep(1.5)
            print("")
            print ("Incinerate or Glaciate: ")
        magic_type = input("")

        if magic_type == "Glaciate":
            Glaciate_rng = random.randint(1, 10)
            if Glaciate_rng <= 7:
                print("You froze the dummy!")
                print("Not that it could move anyways..")
            elif Glaciate_rng > 7:
                print("Glaciate failed!")
            time.sleep(2)
        if magic_type == "Incinerate":
            print("You burned the dummy  for 20 damage!")
            print("dummy hp: ", dummy_hith - 20)

    print("")
    print("Your third move is Prayer.")
    time.sleep(1.5)
    print("Prayer heals you for 8 hp, and has a small chance to buff your attack damage. ")
    time.sleep(2.5)
    print("lets try it. ")
    time.sleep(1.5)
    print("")
    print("What move will you use? ")
    print("Slash, Magic, Prayer: ")
    combat_b = input("")
    while combat_b != "Prayer":
        print("Let's do Prayer this time.")
        time.sleep(1)
        print("")
        print("What move will you use? ")
        print("Slash, Magic, Prayer, talk: ")
        combat_b = input("")
    if combat_b == "Prayer":
        prayer_buff = 0
        name_hp = 100
        print("")
        print("You healed for 8 hp")
        print(name, "'s hp: ", name_hp)
        prayer_buff = random.randint(1, 10)
        if prayer_buff > 8:
            print("Your attack damage also got buffed!")

        time.sleep(2)

    print("You can try any move for this round. ")
    time.sleep(2)
    print("Go wild!")
    time.sleep(2)
    print("")
    print("What move will you use? ")
    print("Slash, Magic, Prayer: ")
    combat_c = input("")
    if combat_c == "Slash":
        print("")
        print("You slashed the dummy for 10 damage!")
        print("dummy hp:", dummy_hith_2 - 10)
        if prayer_buff > 8:
            print("")
            print("You slashed the dummy for 12 damage! (Empowered due to prayer)")
            print("dummy hp:", dummy_hith_2 - 12)

    if combat_c == "Magic":
        print("Incinerate or Glaciate: ")
        magic_type_1 = input("")
        if magic_type_1 == "Glaciate":
            Glaciate_rng = random.randint(1, 10)
            if Glaciate_rng <= 7:
                print("You froze the dummy!")
                print("Not that it could move anyways..")
            elif Glaciate_rng > 7:
                print("Glaciate failed!")
            time.sleep(2)
        if magic_type_1 == "Incinerate":
            print("You burned the dummy for 20 magic damage!")
            time.sleep(1)
            print("dummy hp:", dummy_hith_2 - 20)

    print("")

    if combat_c == "Prayer":
        Prayer = 8
        name_hp = 100
        print("")
        print("You healed for 8 hp")
        time.sleep(1)
        print(name, "'s hp: ", name_hp)
        prayer_buff = random.randint(1, 10)
        if prayer_buff > 8:
            print("Your attack damage also got buffed!")

    time.sleep(2)
    print("Great job on finishing the practice. ")
    time.sleep(3)
    print("Now we will go into the real dungeon. ")
    time.sleep(3)
    print("Loading...")
    time.sleep(5)
    print("")
    print("")
    print("")
    print("")
    print("")

def Wyvren():
    prayer = 8
    cooldown = 3
    rock_hp = 170
    burn = 20
    prayer_buff = 0
    slash = 10
    name_hp = 100
    magic_type_1 = ""
    Glaciate_rng = 0
    dragon_hp = 300
    # if boost == "Attack":
    #     slash = 12
    # if boost == "Health":
    #     name_hp = 102
    # if second_boost == "Attack":
    #     slash = slash + 4
    # if second_boost == "Health":
    #   name_hp = name_hp + 4
    # if second_boost == "Incinerate":
    #   burn = 24
    # if second_boost == "Prayer":
    #   prayer = 10
    print("The Wyvren roars in approval, and accepts your challenge. ")
    time.sleep(2)
    while dragon_hp > 0:
        time.sleep(1)
        print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat_c = input("")
        if combat_c != "Slash" and combat_c != "Magic" and combat_c != "Prayer":
            print("Let's use an actual action. ")
            time.sleep(1)
            print("What move will you use? ")
            print("Slash, Magic, Prayer: ")
            combat_c = input("").lower()

        if combat_c == "Slash":
            print("")
            print("You slashed the Wyvren for damage!")
            time.sleep(2)
            print("Wyvren hp:", dragon_hp - slash)
            dragon_hp = dragon_hp - slash
            if prayer_buff > 8:
                print("")
                print("You slashed the Wyvren for some damage! (Empowered due to prayer)")
                print("Wyvren hp:", dragon_hp - slash)
            dragon_hp = dragon_hp - (slash + 2)
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
                print("you burned the Wyvren for 10 damage!")
                dragon_hp = dragon_hp - burn
                print("Wyvren hp: ", dragon_hp)
                cooldown = cooldown + 1
                if cooldown % 3 != 0:
                    print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)


            elif magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 6:
                    print("You froze the Wyvren!")
                    time.sleep(1.5)
                    print("It froze his fire! ")
                    time.sleep(1.5)
                    print("It took heavy damage! ")
                    dragon_hp = dragon_hp - 90
                    print("Wyvren hp: ", dragon_hp)
                elif Glaciate_rng > 7:
                    print("Glaciate failed!")
                    time.sleep(2)

            print("")
        elif combat_c == "Prayer":
            print("")
            print("You healed for 8 hp")
            time.sleep(1)
            print(name, "'s hp: ", name_hp + prayer)
            prayer_buff = random.randint(1, 10)
            if prayer_buff > 8:
                print("Your attack damage also got buffed!")

        elif Glaciate_rng > 7:
            print("The Wyvren slams you for 15 damage!")
            time.sleep(1)
            name_hp = name_hp - 11
            print("Your hp: ", name_hp)
        elif combat_c != str:
            print("Let's use an actual action")
            print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat_c = input("").lower()
        if rock_hp <= 0:
            break
        if name_hp <= 0:
            time.sleep(1)
            print("You died a sad an painful death, forgotten in the depths of  the dungeon. ")
            time.sleep(2)

def left_path():
    print("You chose to enter the left path. ")
    time.sleep(2)
    print("The room is filled with fire, except the main path. ")
    time.sleep(2)
    print("In the middle of the room, a Wyvren asleep in the middle. ")
    time.sleep(2)
    print("Challenge? ")
    print(" Y/N?")
    challenge = input("")
    if challenge == "Y":
      Wyvren()
    elif challenge == "N":
        print("You return to the main path in cowardice. ")
        time.sleep(2)
        choice()
    while challenge != "Y" and challenge != "N":
      print("You cannot", challenge, "it. ")
      time.sleep(2)
      print("Challenge? ")
      print(" Y/N?")
      challenge = input("").lower()

def right_path():
  print("You enter the dark, haunting room. ")
  time.sleep(1.5)
  print("Many graves surround you as you walk deeper into the room. ")
  time.sleep(1.5)
  print("One of the shadows in the room stir.")
  time.sleep(2)
  necromancer()

def choice():
    time.sleep(2)
    print("The next room splits into two different rooms. ")
    time.sleep(2)
    print("The room on the left is smells of sulfur, and you can feel an instense heat coming from that room. ")
    time.sleep(2)
    print("The second room smells of corpses, and a musty scent emanates from it. ")
    time.sleep(1.5)
    print("Which room do you choose to enter? ")
    left_or_right = input("").lower()
    if left_or_right == "Left":
        left_path()
    if left_or_right == "Right":
        right_path()

def necromancer():
    print("A Necromancer comes out of the shadow and attacks you! ")

print("-----------------------")
print("Welcome to The Dungeon")
print("-----------------------")
playsound.playsound("ello.mp3")



time.sleep(1.5)
name = input("State your name: ")
time.sleep(0.5)

while name == "":
    print("Enter an actual name, loser.")
    name = input("State your name: ")
if name == "a":
    print("Skipping...")
    time.sleep(1.5)
    hobgoblin()
if name == "b":
    print("Skipping...")
    time.sleep(1.5)
    scary_rock()
if name == "c":
    print("Skipping...")
    time.sleep(1.5)
    left_path()
if name == "d":
    print("Skipping...")
    time.sleep(1.5)
    right_path()

print("")

introduction()

dummy()

hobgoblin()
time.sleep(2)
print("You have slain the Hobgoblin!")
time.sleep(2)
print("You gained 2 levels!")
time.sleep(2)
print("You may choose to upgrade your health or your attack.")
time.sleep(2)
print("Which do you choose:")
boost = input("").lower()
if boost == "Attack":
    print("Your attack increased by 2 points!")
    slash = 12
elif boost == "Health":
    print("Your health increased by 2 points")
    name_hp = 102
else:
    print("Enter one of the upgrades you desire, please")
    boost = input("").lower()
time.sleep(3)
burn = 20
prayer = 8
print("")
print("")
print("")
print("")
print("")
print("")

print("The next room is locked with the power of a word question.")
time.sleep(3)
print("The word question presents you with a question about... computers????")
time.sleep(3)
print("Answer thee next question correct to passeth onto thy next dungeon room.\n (Answer with the correct letter.) ")
time.sleep(2)
print("Which part of your computer is respponsible for generating graphics? ")
quiz_choice = ["A. The Fan,", "B. The CPU,", " C. The Graphics producer machine,", " D. GPU"]
print(quiz_choice[0])
print(quiz_choice[1])
print(quiz_choice[2])
print(quiz_choice[3])
print("What is thy answer? ")
quiz_one = input("").lower()
time.sleep(1)
while quiz_one != "D":
    ("Wrong Answer. ")
    print("Which part of your computer is respponsible for generating graphics? ")
    quiz_choice = ["A. The Fan,", "B. The CPU,", " C. The Graphics producer machine,", " D. GPU"]
    time.sleep(2.5)
    print(quiz_choice[0])
    print(quiz_choice[1])
    print(quiz_choice[2])
    print(quiz_choice[3])
    print("What is thy answer? ")
    quiz_one = input("").lower()
if quiz_one == "D":
    print("Well done!")
    time.sleep(1.5)
    print("Onto the next one. ")
    time.sleep(2)
    print("Which type of malware, when infecting a computer, locks the user out, and demands money in return? ")
    quiz_choice_2 = ["A. SpyWare,", "B. Adware,", " C. Ransomeware,", " D. The bad virus"]
    time.sleep(2.5)
    print(quiz_choice_2[0])
    print(quiz_choice_2[1])
    print(quiz_choice_2[2])
    print(quiz_choice_2[3])
    print("What is thy answer? ")
    quiz_two = input("").lower()
    while quiz_two != "C":
        print("Wrong answer")
        time.sleep(2)
        print("Which type of malware, when infecting a computer, locks the user out, and demands money in return? ")
        quiz_choice_2 = ["A. SpyWare,", "B. Adware,", " C. Ransomeware,", " D. The bad virus"]
        time.sleep(2.5)
        print(quiz_choice_2[0])
        print(quiz_choice_2[1])
        print(quiz_choice_2[2])
        print(quiz_choice_2[3])
        print("What is thy answer? ")
        quiz_two = input("").lower()
    if quiz_two == "C":
        print("Well done!")
        time.sleep(2)
        print("Onto the next room. ")
        scary_rock()

print("You have slain the Gargoyle! ")
time.sleep(1.5)
print("You gained 4 levels!")
time.sleep(2)
print("You can upgrade your hp, attack, Incinerate, and Prayer.")
time.sleep(2)
print("What would you like to upgrade this time? ")
second_boost = input("").lower()
while second_boost != "Health" or "Attack" or "Incinerate" or "prayer":
    if second_boost == "Health":
        print("Your hp increased by 4 points!")
        name_hp = name_hp + 4
        time.sleep(2)
        print("Your hp: ", name_hp)
    elif second_boost == "Incinerate":
        print("Your Incinerate damage increased by 4 points! ")
        burn = burn + 4
        time.sleep(2)
        print("Your Incinerate damage: ", burn)
    elif second_boost == "Attack":
        print("Your attack damage increased by 4 points! ")
        slash = slash + 4
        time.sleep(2)
        print("Your attack damage: ", slash)
    elif second_boost == "Prayer":
        print("Your prayer healing increased! ")
        time.sleep(2)
        print("Your empowered attack chance increased to 30%! ")
        prayer = prayer + 2
        print("Prayer healing: ", prayer)
    else:
        print("Enter a valid answer.")
        time.sleep(2)
        print("What would you like to upgrade this time? ")
        second_boost = input("")

time.sleep(1)
choice()
