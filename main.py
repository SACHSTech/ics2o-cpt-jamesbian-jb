import time
import random
import sys

# Make sure that all commands input are capital case

def introduction():
   time.sleep(2)
   print("It all began when you heard the tale of the legendary dungeon in town.")
   time.sleep(3)
   print(
       "The old men whispered about the treasures inside, and the amount of ladies one would get just by clearing it. ")
   time.sleep(4)
   print("Without any wait, you head into the dungeon, hoping to attract all the ladies...")
   time.sleep(4.5)
   print("Loading...")
   time.sleep(5)

   print(name, ", your first enemy is the training dummy to practice your moves.")
   time.sleep(3)
   print("Your first move is slash.")
   time.sleep(3)
   print("Slash is a melee attack with your blade, where you deal 10 damage to enemies without armour.")
   time.sleep(4)

print("------------------------")
print("Welcome to The Dungeons")
print("------------------------")

time.sleep(1.5)
name = input("State your name: ")
time.sleep(0.5)

if name == "Fabroa":
   print("I see you have arrived, Mr.Fabroa")
while name == "":
   print("Enter an actual name, loser.")
   name = input("State your name: ")
if name != "Fabroa":
   print("interesting name,", name)
print("")

introduction()


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
           print("dummy hp: ", dummy_hith_2)

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
       Prayer = 8
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
       print("dummy hp:", dummy_hith - 10)
       if prayer_buff > 8:
           print("")
           print("You slashed the dummy for 12 damage! (Empowered due to prayer)")
           print("dummy hp:", dummy_hith - 12)

   if combat_c == "Magic":
       magic_type_1 = input("Incinerate or Glaciate: ")
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


dummy()


def hobgoblin():
   cooldown = 3
   hobgoblin_hp = 100
   slash = 10
   burn = 20
   prayer_buff = 0
   name_hp = 100

   print("You encounter a Hobgoblin, guarding the entrance to the next room!")
   time.sleep(3)
   while hobgoblin_hp > 0:
       print("What move will you use? ")
       time.sleep(2)
       print("Slash, Magic, Prayer: ")
       combat_c = input("")
       if combat_c == "Slash":
           print("")
           print("You slashed the dummy for 10 damage!")
           print("hobgoblin hp:", hobgoblin_hp - slash)
           hobgoblin_hp = hobgoblin_hp - slash
           if prayer_buff > 8:
               print("")
               print("You slashed the hobgoblin for 12 damage! (Empowered due to prayer)")
               print("hobgoblin hp:", hobgoblin_hp - 12)
               hobgoblin_hp = hobgoblin_hp - (slash + 2)
       elif combat_c == "Magic":
           magic_type_1 = input("incinerate or Glaciate: ")
           if magic_type_1 == "Glaciate":
               Glaciate_rng = random.randint(1, 10)
               if Glaciate_rng <= 7:
                   print("You froze the hobgoblin!")
                   print("The Hobgoblin was frozen!")
                   time.sleep(3)
                   print("He can't attack!")
               elif Glaciate_rng > 7:
                   print("Glaciate failed!")
                   time.sleep(3)
                   print("The hobgoblin smacked you for 11 damage!")
                   time.sleep(2)
                   name_hp = name_hp - 11
                   print("Your hp: ", name_hp)
                   time.sleep(3)
           if magic_type_1 == "incinerate":
               print("you burned the hobgoblin for 20 damage!")
               hobgoblin_hp = hobgoblin_hp - burn
               print("Hobgoblin hp: ", hobgoblin_hp)
               if cooldown % 3 != 0:
                   print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)

       print("")
       if combat_c == "Prayer":
           name_hp = 100
           print("")
           print("You healed for 8 hp")
           time.sleep(1)
           print(name, "'s hp: ", name_hp)
           prayer_buff = random.randint(1, 10)
           if prayer_buff > 8:
               print("Your attack damage also got buffed!")
       if magic_type_1 != "Glaciate":
           print("The hobgoblin smacked you for 8 damage!")
           time.sleep(2)
           name_hp = name_hp - 8
           print("Your hp: ", name_hp)

       if name_hp <= 0:
           time.sleep(1)
           print("You died a sad an painful death, forgotten in the depths of  the dungeon. ")
           time.sleep(2)
           sys.exit()


hobgoblin()
time.sleep(2)
print("You have slain the Hobgoblin!")
time.sleep(2)
print("You gained 2 levels!")
time.sleep(2)
print("You may choose to upgrade your health or your attack.")
time.sleep(2)
print("Which do you choose:")
time.sleep(1)
boost = input("")
if boost == "Attack":
   print("Your attack increased by 2 points!")
   slash = 12
elif boost == "Health":
   print("Your health increased by 2 points")
   name_hp = 102
else:
   print("Enter one of the upgrades you desire, please")
   boost = input("")

time.sleep(3)
print("clearing the console...")
time.sleep(3)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


def scary_rock():
   print("Well done answering that question. ")
   time.sleep(2)
   print("When you open the door to the next room, you find two chests. ")
   time.sleep(3)
   print("Which do you choose? ")
   time.sleep(2)
   chest = input("Left or right: ")
   if chest == "Left":
       print("There was nothing in the chest. ")
       time.sleep(2.5)
       print("The other chest folds, and vanishes. ")
   elif chest == "Right":
       print("The chest contained a great sword.")
       time.sleep(2)
       print("You gain attack damage!")

       slash = 17
       cooldown = 3
       rock_hp = 170
       burn = 20
       prayer_buff = 0
       print("You encounter a Gargoyle, looming over the large corridor!")
       time.sleep(3)
       while rock_hp > 0:
           time.sleep(1)
           print("What move will you use? ")
           print("Slash, Magic, Prayer: ")
           combat_c = input("")
           if combat_c == "Slash":
               print("")
               print("You slashed the gargoyle for damage!")
               print("hobgoblin hp:", rock_hp - slash)
               rock_hp = rock_hp - slash
               if prayer_buff > 8:
                   print("")
                   print("You slashed the dummy for 20 damage! (Empowered due to prayer)")
                   print("hobgoblin hp:", rock_hp - 20)
                   rock_hp = rock_hp - (slash + 3)
           elif combat_c == "Magic":
               magic_type_1 = input("incinerate or Glaciate: ")
               if magic_type_1 == "Glaciate":
                   Glaciate_rng = random.randint(1, 10)
                   if Glaciate_rng <= 7:
                       print("You froze the Gargoyle!")
                   elif Glaciate_rng > 7:
                       print("Glaciate failed!")
                   time.sleep(2)
               if magic_type_1 == "incinerate":
                   if cooldown % 3 == 0:
                       print("You cannot use that spell quite yet, currently you are on turn", cooldown - 3)
                   print("you burned the Gargoyle for 20 damage!")
                   rock_hp = rock_hp - burn
                   print("Hobgoblin hp: ", rock_hp)

           print("")
           if combat_c == "Prayer":

               name_hp = 100
               print("")
               print("You healed for 8 hp")
               time.sleep(1)
               print(name, "'s hp: ", name_hp)
               prayer_buff = random.randint(1, 10)
               if prayer_buff > 8:
                   print("Your attack damage also got buffed!")
           if Glaciate_rng <= 7:
               print("The Gargoyle was frozen!")
               time.sleep(1)
               print("He can't move!")
           elif Glaciate_rng > 7:
               print("The Gargoyle smacked you for 11 damage!")
               time.sleep(1)
               print("Your hp: ", name_hp)
           else:
               print("Let's use an actual action")


print("The next room is locked with the power of a word question.")
time.sleep(3)
print("The word question presents you with a question about... computers????")
time.sleep(3)
print("Answer thee next question correct to passeth onto thy next dungeon room. (Answer with the correct number.) ")
time.sleep(2)
print("What type of Malware threatens to share your information if money isn't given to the creator? ")

question_choice = ["1. Spyware", "2. Malware ", "3. Trojan", "4. Ransomware", ]
print(question_choice[0])
print(question_choice[1])
print(question_choice[2])
print(question_choice[3])
print(question_choice[4])
print("What is thy answer, Knave? ")
malware_answer = int(input(""))

while malware_answer != 1:
   print("Wrong, fool")
   time.sleep(2)
   print("What type of Malware threatens to share your information if money isn't given to the creator? ")
   question_choice = ["1. Spyware", "2. Malware ", "3. Trojan", "4. Ransomware", ]
   print(question_choice[0])
   print(question_choice[1])
   print(question_choice[2])
   print(question_choice[3])
   print(question_choice[4])
   print("What is thy answer, Knave? ")
if malware_answer == 1:
   scary_rock()
