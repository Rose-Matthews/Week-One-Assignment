# Task 1
character = ""
wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"

my_hp = 0
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

my_damage = 0
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

# Task 2 & 3

while True:
    character = input("Choose your character:")
     print("1) Wizard")
         print("2) Elf")
          print("3) Human")

           if (character == "1"):
                character = wizard
                my_damage = wizard_damage
                my_hp = wizard_hp
            print("You chose the Wizard")
            break

elif(character == "2"):
    character = elf
    my_damage = elf_damage
    my_hp = elf_hp
    print("You chose the Elf")
    break

elif (character == "3"):
    character = human
    my_damage = human_damage
    my_hp = human_hp
    print("You chose the Human")
    break

else:
    print("Unknown character")
