import time
import random
import sys
from playsound import playsound



# Make sure that all commands input are capital case
# The training allows the spell with a cool down to be used twice
# This is on purpose as to let you try the move moRE

# Defining Functions
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
    rock_hp = 135
    burn = 20
    prayer_buff = 0
    slash = 10
    name_hp = 100
    magic_type_1 = ""
    Glaciate_rng = 10
    Slash_done = False
    if boost == "Attack":
        slash = 12
    if boost == "Health":
        name_hp = 120
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
            combat_c = input("")

        if combat_c == "Slash":
            print("")
            print("You slashed the gargoyle for damage!")
            time.sleep(2)
            print("Gargoyle hp:", rock_hp - (slash / 2) + 3)
            rock_hp = rock_hp - (slash / 2) + 3
            Slash_done == True
            if prayer_buff > 8:
                print("")
                print("You slashed the Gargoyle for some damage! (Empowered due to prayer)")
                print("Gargoyle hp:", rock_hp - slash + 3)
                rock_hp = rock_hp - (slash + 3)
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
              if cooldown % 3 != 0:
                print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)
              if cooldown % 3 == 0:
                print("you burned the Gargoyle for 30 damage!")
                time.sleep(2)
                print("It was effective! ")
                rock_hp = rock_hp - (burn + 10)
                print("Gargoyle hp: ", rock_hp)
            if magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 7:
                    print("You froze the Gargoyle!")
                    time.sleep(2)
                elif Glaciate_rng > 7:
                    print("Glaciate failed!")
                    time.sleep(2)

            print("")
        if combat_c == "Prayer":
            print("")
            print("You healed for 8 hp")
            time.sleep(1)
            print("Your hp: ", name_hp + prayer)
            name_hp = name_hp + prayer
            prayer_buff = random.randint(1, 10)
            if prayer_buff > 8:
                print("Your attack damage also got buffed!")

        if magic_type_1 != "Glaciate" or Glaciate_rng > 7 or Slash_done == True:
            print("The Gargoyle smacked you for some damage!")
            time.sleep(2)
            name_hp = name_hp - 11
            print("Your hp: ", name_hp)
            Slash_done = False
            cooldown = cooldown + 1

        if Glaciate_rng <= 7:
            print("The Gargoyle was frozen!")
            time.sleep(1)
            print("He can't move!")
            Glaciate_rng = 10
            cooldown = cooldown + 1

        if rock_hp <= 0:
            break
        if name_hp <= 0:
            time.sleep(1)
            print("You died a sad an painful death, forgotten in the depths of  the dungeon. ")
            time.sleep(2)
            sys.exit()

def hobgoblin():
  # Creating Variables for the combat including: Damage, Health, Prayer, Magic
    cooldown = 3
    gob_hp = 100
    slash = 10
    burn = 20
    prayer_buff = 0
    name_hp = 100
    magic_type_1 = ""
    prayer = 8
    Glaciate_rng = 10
    Slash_done = False

    print("You encounter a Hobgoblin, Guarding the entrance to the next room! ")
    time.sleep(2)
    while gob_hp > 0:
        time.sleep(1)
        print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat_c = input("")
        if combat_c != "Slash" and combat_c != "Magic" and combat_c != "Prayer":
            print("Let's use an actual action. ")
            time.sleep(2)
            print("What move will you use? ")
            print("Slash, Magic, Prayer: ")
            combat_c = input("")

        if combat_c == "Slash":
            print("")
            print("You slashed the Hobgoblin for damage!")
            time.sleep(2)
            print("Hobgoblin hp:", gob_hp - slash)
            gob_hp = gob_hp - slash
            Slash_done == True
            if prayer_buff > 8:
                print("")
                print("You slashed the Hobgoblin for some damage! (Empowered due to prayer)")
                print("Hobgoblin hp:", gob_hp - slash + 3)
                gob_hp = gob_hp - (slash + 3)
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
              if cooldown % 3 != 0:
                print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)
              if cooldown % 3 == 0:
                print("you burned the Hobgoblin for some damage!")
                time.sleep(2)
                gob_hp = gob_hp - burn
                print("Hobgoblin hp: ",gob_hp)
            if magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 7:
                    print("You froze the Hobgoblin!")
                    time.sleep(2)
                elif Glaciate_rng > 7:
                    print("Glaciate failed!")
                    time.sleep(2)

            print("")
        if combat_c == "Prayer":
            print("")
            print("You healed for 8 hp")
            time.sleep(1)
            print("Your hp: ", name_hp + prayer)
            name_hp = name_hp + prayer
            prayer_buff = random.randint(1, 10)
            if prayer_buff > 8:
                print("Your attack damage also got buffed!")

        if magic_type_1 != "Glaciate" or Glaciate_rng > 7 or Slash_done == True:
            print("The Hobgoblin smacked you for some damage!")
            time.sleep(2)
            name_hp = name_hp - 8
            print("Your hp: ", name_hp)
            Slash_done = False
            cooldown = cooldown + 1

        if Glaciate_rng <= 7:
            print("The Hobgoblin was frozen!")
            time.sleep(1)
            print("He can't move!")
            Glaciate_rng = 10
            cooldown = cooldown + 1

        if gob_hp <= 0:
            break
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
    time.sleep(3)
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
    if combat_a != "Magic":
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
        while magic_type != "Incinerate" and magic_type != "Glaciate":
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
  # Assigning Variables for the combat
    prayer = 8
    cooldown = 3
    rock_hp = 170
    burn = 20
    prayer_buff = 0
    slash = 10
    name_hp = 100
    magic_type_1 = ""
    Glaciate_rng = 0
    drag_hp = 300
    Slash_done = False
    if boost == "Attack":
        slash = 18
    if boost == "Health":
        name_hp = 120
    if second_boost == "Attack":
        slash = slash + 8
    if second_boost == "Health":
      name_hp = name_hp + 40
    if second_boost == "Incinerate":
      burn = 40
    if second_boost == "Prayer":
      prayer = 10
    print("The Wyvren roars in approval, and accepts your challenge. ")
    time.sleep(2)

    # While Loop
    while drag_hp > 0:
        time.sleep(1)
        print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat_c = input("")
        if combat_c != "Slash" and combat_c != "Magic" and combat_c != "Prayer":
            print("Let's use an actual action. ")
            time.sleep(2)
            print("What move will you use? ")
            print("Slash, Magic, Prayer: ")
            combat_c = input("")
        #Slash Function
        if combat_c == "Slash":
            print("")
            print("You slashed the Wyvren for damage!")
            time.sleep(2)
            print("Wyvren hp:", drag_hp - slash)
            drag_hp = drag_hp - slash
            Slash_done == True
            if prayer_buff > 8:
                print("")
                print("You slashed the Wyvren for some damage! (Empowered due to prayer)")
                print("Wyvren hp:", drag_hp - slash + 3)
                drag_hp = drag_hp - (slash + 3)
        # Magic Function
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
              if cooldown % 3 != 0:
                print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)
              if cooldown % 3 == 0:
                print("you burned the Wyvren for 10 damage!")
                time.sleep(2)
                print("It wasn't effective! ")
                rock_hp = rock_hp - burn
                print("Wyvren hp: ", drag_hp)
            if magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 7:
                    print("You froze the Wyvren!")
                    time.sleep(2)
                    print("It took heavy damage from the freeze! ")
                    drag_hp = drag_hp - 90
                    print("Wyvren hp: ",drag_hp)
                elif Glaciate_rng > 7:
                    print("Glaciate failed!")
                    time.sleep(2)

            print("")
        #Prayer Function
        if combat_c == "Prayer":
            print("")
            print("You healed for 8 hp")
            time.sleep(1)
            print("Your hp: ", name_hp + prayer)
            name_hp = name_hp + prayer
            prayer_buff = random.randint(1, 10)
            if prayer_buff > 8:
                print("Your attack damage also got buffed!")

        if magic_type_1 != "Glaciate" or Glaciate_rng > 7 or Slash_done == True:
            print("The Wyvren scorches you for some damage!")
            time.sleep(2)
            name_hp = name_hp - 30
            print("Your hp: ", name_hp)
            Slash_done = False
            cooldown = cooldown + 1

        if Glaciate_rng <= 7:
            print("The Wyvren was frozen!")
            time.sleep(1)
            print("He can't move!")
            Glaciate_rng = 10
            cooldown = cooldown + 1

        if drag_hp <= 0:
          final()
        if name_hp <= 0:
            time.sleep(1)
            print("You died a sad an painful death, forgotten in the depths of the dungeon. ")
            time.sleep(2)
            sys.exit()

def left_path():
    print("You chose to enter the left path. ")
    time.sleep(2)
    print("The room is filled with fire, except the main path. ")
    time.sleep(2)
    print("In the middle of the room, a Wyvren asleep in the middle. ")
    time.sleep(2)
    print("Challenge? ")
    print(" Y/N?")
    # Input for whether or not they wish to fight the Wyvren
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
  time.sleep(3)
  print("Many graves surround you as you walk deeper into the room. ")
  time.sleep(2.5)
  print("One of the shadows in the room stir.")
  time.sleep(3)
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
    prayer = 8
    cooldown = 3
    rock_hp = 170
    burn = 20
    prayer_buff = 0
    slash = 10
    name_hp = 100
    magic_type_1 = ""
    Glaciate_rng = 0
    dead_hp = 300
    if boost == "Attack":
        slash = 12
    if boost == "Health":
        name_hp = 120
    if second_boost == "Attack":
        slash = slash + 4
    if second_boost == "Health":
      name_hp = name_hp + 40
    if second_boost == "Incinerate":
      burn = 24
    if second_boost == "Prayer":
      prayer = 10
    time.sleep(2)
    while dead_hp > 0:
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
            print("You slashed the Necromancer for damage!")
            time.sleep(2)
            print("Necromancer hp:", dead_hp - slash)
            dead_hp = dead_hp - slash
            if prayer_buff > 8:
                print("")
                print("You slashed the Necromancer for some damage! (Empowered due to prayer)")
                print("Necromancer hp:", dead_hp - slash)
            dead_hp = dead_hp - (slash + 2)
        elif combat_c == "Magic":
            magic_type_1 = input("incinerate or Glaciate: ")
            if magic_type_1 == "Incinerate":
                print("you burnedNecromancer for 10 damage!")
                dead_hp = dead_hp - burn
                print("Necromancer hp: ", dead_hp)
                cooldown = cooldown + 1
                if cooldown % 3 != 0:
                    print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)


            elif magic_type_1 == "Glaciate":
                Glaciate_rng = random.randint(1, 10)
                if Glaciate_rng <= 6:
                    print("You froze the Necromancer!")
                    time.sleep(1.5)
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
            print("The Necromancer curses you for 0 damage!")
            time.sleep(1)
            name_hp = name_hp - 11
            print("Your hp: ", name_hp)
        elif combat_c != "Magic" and combat_c != "attack" and combat_c != "Prayer":
            print("Let's use an actual action")
            print("What move will you use? ")
        print("Slash, Magic, Prayer: ")
        combat_c = input("").lower()
        if dead_hp <= 0:
            break
        if name_hp <= 0:
            time.sleep(1)
            print("You died a sad an painful death, forgotten in the depths of  the dungeon. ")
            time.sleep(2)
            sys.exit()

def final():
  print("When the Wyvren finally lays down it's head forever, you see the Legendary Pufferfish on a pedastal behind it. ")
  time.sleep(3)
  print("When you reach out to grab it, the pufferfish puffs it's spikes out.")
  time.sleep(2)
  print("One last question before you walk out of here alive.")
  time.sleep(2)
  print("What python Package allows you to design and code games?")
  quiz_choice = ["A. Google Games,", "B. Pygames,", " C. Graphics Python Engine ,", " D. Vs Code"]
  print(quiz_choice[0])
  print(quiz_choice[1])
  print(quiz_choice[2])
  print(quiz_choice[3])
  print("What is thy answer? ")
  quiz_one = input("").lower()
  time.sleep(2)
  while quiz_one != "B":
    ("Wrong Answer. ")
    quiz_choice = ["A. Google Games,", "B. Pygames,", " C. Graphics Python Engine ,", " D. Vs Code"]
    time.sleep(2.5)
    print(quiz_choice[0])
    print(quiz_choice[1])
    print(quiz_choice[2])
    print(quiz_choice[3])
    print("What is thy answer? ")
    quiz_one = input("").lower()
  if quiz_one == "B":
    print("The pufferfish finally unpuffs, and you pick up the Golden pufferfish.")
    time.sleep(2)
    print("The pufferfish quietly aeughs in the background. ")
    time.sleep(2)
    print("Congrats on beating the game!")

  

print("-----------------------")
print("Welcome to The Dungeon")
print("-----------------------")


# Asks for name input, which the person will be referred to as
time.sleep(1.5)
name = input("State your name: ")
time.sleep(0.5)
# If name us blank, it loops the code again
while name == "":
    print("Enter an actual name, loser.")
    name = input("State your name: ")
if name == "a":
    print("Skipping...")
    time.sleep(1.5)
    hobgoblin()
    sys.exit()
if name == "b":
    print("Skipping...")
    time.sleep(1.5)
    scary_rock()
    sys.exit()
if name == "c":
    print("Skipping...")
    time.sleep(1.5)
    left_path()
    sys.exit()
if name == "d":
    print("Skipping...")
    time.sleep(1.5)
    right_path()
    sys.exit()
else:
  print("Interesting name, ", name)

print("")
# Calling Functions
introduction()

dummy()

hobgoblin()
time.sleep(2)
# Upgrades for killing the Hobgoblin
print("You have slain the Hobgoblin!")
time.sleep(2)
print("You gained 2 levels!")
time.sleep(2)
print("You may choose to upgrade your health or your attack.")
time.sleep(2)
print("Which do you choose:")
boost = input("")
if boost == "Attack":
    print("Your attack increased by 2 points!")

if boost == "Health":
    print("Your health increased by 2 points")

else:
    print("Enter one of the upgrades you desire, please")
    boost = input("")
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
    quiz_one = input("")
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
second_boost = input("")
name_hp = 100
slash = 10
if boost == "Health":
  name_hp == 140
if boost == "Attack":
  slash == 18
while second_boost != "Health" or "Attack" or "Incinerate" or "prayer":
    if second_boost == "Health":
        print("Your hp increased by 4 points!")
        name_hp = name_hp + 4
        time.sleep(2)
        print("Your hp: ", name_hp)
    elif second_boost == "Incinerate":
        print("Your Incinerate damage increased! ")
        burn = burn + 4
        time.sleep(2)
        print("Your Incinerate damage: ", burn)
    elif second_boost == "Attack":
        print("Your attack damage increased! ")
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

print("")
print("")
print("")
print("")
print("")
print("")

time.sleep(1)
print("The next room is locked with the power of a word question.")
time.sleep(3)
print("Answer thee next question correct again to passeth onto thy next dungeon room.\n (Answer with the correct letter.) ")
time.sleep(2)
print("Which part of your machine routes internet connection to your home? ")
quiz_choice = ["A. The Router,", "B. The MotherBoard,", " C. The Wifi machine,", " D. The Internet Extender"]
print(quiz_choice[0])
print(quiz_choice[1])
print(quiz_choice[2])
print(quiz_choice[3])
print("What is thy answer? ")
quiz_one = input("").lower()
time.sleep(1)
while quiz_one != "A":
    ("Wrong Answer. ")
    print("Which part of your machine routes internet connection to your home? ")
    quiz_choice = ["A. The Router,", "B. The MotherBoard,", " C. The Wifi machine,", " D. The Internet Extender"]
    time.sleep(2.5)
    print(quiz_choice[0])
    print(quiz_choice[1])
    print(quiz_choice[2])
    print(quiz_choice[3])
    print("What is thy answer? ")
    quiz_one = input("").lower()
if quiz_one == "A":
  print("The door unlocks, and you pass onto the next room. ")
  choice()
