import time
import random


def pause(phrase):
    print(phrase)
    time.sleep(2)


def game_over():
    pause("You fall to the ground as the strength to stand escapes you.")
    pause("Your vision fades and your thoughts stand still.")
    while True:
        retry = input("try again?\n y/n\n")
        if retry == "y":
            start()
        elif retry == "n":
            exit()


def stats():
    global max_hp
    max_hp = 30
    global hp
    hp = 30
    global defence
    defence = 5
    global power
    power = 5
    global xp
    xp = 0
    global xp_max
    xp_max = 10


def level_up():
    global max_hp
    global hp
    global defence
    global power
    global xp_max
    global xp
    xp -= xp_max
    xp_max += 5
    value = random.randint(1, 3)
    max_hp += value
    pause("your max hp goes up by " + str(value))
    value = random.randint(1, 2)
    power += value
    pause("your power goes up by " + str(value))
    value = random.randint(0, 1)
    defence += value
    pause("your defence goes up by " + str(value))
    hp = max_hp
    print("max hp is " + str(max_hp))
    print("power is " + str(power))
    print("defence is " + str(defence))


def equipment():
    global weapons
    weapons = ["shortsword"]
    global armor
    armor = ["leather shield"]
    global potions
    potions = ["healing potion"]
    global camping
    camping = []
    global artifacts
    artifacts = []


def opening():
    pause("""The message board in town spoke of an ancient forest
    untouched by human hands.""")
    pause("""After paying most of your life savings to get the map
    to this forest you finally arrive with somewhat basic gear in tow.""")
    pause("""You double check your gear. In your pack you have a
    shortsword a leather sheild and a healing potion""")
    pause("""You notice that the landscape consists of massive trees some
    reaching more then 800 feet tall.""")
    pause("""In the distance you spot a river and further in a part of the
    forest that doesn't receive sunlight.""")
    pause("""Currently you find yourself in a large clearing with light
    filtering through the distant treetops""")
    pause("""Nearby you notice some peculiar tracks you dont recognize but
    you can tell that whatever left them is quite large""")


def clearing():
    if "camping_gear" in camping:
        camp()
    pause("you can see three paths leading from the clearing.")
    pause("The path on the left is a game trail heading towords a river.")
    pause("""the center path seems like a trail of destruction
        left by whatever made those footprints""")
    pause("The path on the right leads to a darker part of the forest")
    pause("which path would you like to take?")
    destination = input("(1)left path\n(2)middle path\n(3)right path\n")
    if destination == "1":
        game_trail()
    elif destination == "2":
        broken_path()
    elif destination == "3":
        dark_forest()
    else:
        pause("Unexpected input please try again.")
        clearing()


def broken_path():
    pause("You feel eyes on you as you go down this path of destruction.")
    pause("You feel malice on the back of your neck and hear a low growl.")
    pause("This is your last chance to turn back.")
    answer = input("Turn back?\ny\nn").lower()
    if answer == "y":
        clearing()
    elif answer == "n":
        boss_battle()
    else:
        pause("try again")
        broken_path()


def camp():
    global max_hp
    global hp
    global day
    answer = input("rest at camp?\n(y/n)\n").lower()
    if answer == "y":
        time.sleep(10)
        pause("the night passes and you awaken rested")
        hp = max_hp
    elif answer == "n":
        pause("you decide not to rest at camp")
    elif answer == "godmode":
        max_hp += 1000000
        camp()
    else:
        pause("please enter y or n")
        camp()
    pause("take a moment to check your gear?")
    check = 0
    while (check != "y" and check != "n"):
        check = input("y/n\n")
        if check == "y":
            check_gear()
        elif check == "n":
            pause("you don't check your gear")
        else:
            pause("please enter y or n")


def game_trail():
    pause("You walk along the game trail.")
    pause("Along the path you notice several animal dens perfect for hunting.")
    pause("up ahead you see a river.")
    pause("will you\n(1) go back to the clearing")
    choice = input("(2) hunt\n(3) continue towords the river\n")
    if choice == "1":
        clearing()
    elif choice == "2":
        easy()
    elif choice == "3":
        river()
    else:
        pause("Unexpected input please try again.")
        game_trail()


def river():
    global camping
    pause("""you approach the river. It seems too deep to cross
    but along the bank you see many useful plants.""")
    if "camping_gear" in camping:
        pause("there isn't any more reason to be here")
        pause("you head back to the game trail")
        game_trail()
    else:
        pause("""you take some time to gather enough materials
        to make a set of camping gear""")
        camping.append("camping_gear")
        pause("you head back to the clearing to set up camp")
        clearing()


def dark_forest():
    pause("""you arrive in the darker part of the ancient forest
    where the trees are more dense and sunlight is rare.""")
    pause("""nearby you see tracks of recognizable animals with one key
    difference all these tracks are three times the size of normal tracks""")
    pause("""You feel piercing eyes on you at all times peering from
    the dancing shadows and creaking depths of this wood.""")
    pause("""further forward you see a part of the wood with red trees
    and glowing mushrooms""")
    pause("What will you do?")
    pause("1: head back to the clearing.\n2: follow some tracks.")
    destination = input("3: head deeper into the red wood.\n")
    if destination == "1":
        clearing()
    elif destination == "2":
        medium()
    elif destination == "3":
        heart_wood()
    else:
        pause("unexpected input please try again")
        dark_forest()


def heart_wood():
    pause("""cautiously stepping into the deepest part
    of the red wood you find the largest tree youve seen yet""")
    pause("""it appears as a darker red that the trees around it
    and if you listen closely it almost seems to hum and vibrate""")
    pause("""the outside seems to be caked in crimson amber
    and surrounded by monster skeletons""")
    pause("""you look around and a horde of terrible
    monstocities forming a ring around the tree""")
    pause("""none seem to approach past thirty feet
    or so and none seem to notice your presence""")
    pause("What will you do?")
    choice = input("""1: carefully retreat\n2: isolate a monster to fight
    3: investigate the tree\n""")
    if choice == "1":
        dark_forest()
    elif choice == "2":
        hard()
    elif choice == "3":
        trial()
    else:
        pause("unexpected input please try again")
        heart_wood()


def trial():
    global equipment
    global hp
    global power
    global defence
    pause("""as you approach the tree the monsters
    around the circle look right at you.""")
    pause("""once you near the great tree within its amber
    you spot a spherical object glowing faintly""")
    pause("""once you reach 5 feet from the amber
    the forest goes quiet and you can't hear a sound""")
    pause("""the monsters around you seem to be
    pointing and laughing but no sound escapes their lips""")
    pause("""with terror you ralize you can't hear the sound
    of your own breathing but your heartbeat only grows louder""")
    pause("""filled with terror you quickly spot the path back
    and realize that you can escape but you sense a pressence nearby """)
    while (True):
        answer = input("do you run y/n\n")
        if answer == "y" or answer == "Y":
            pause("""you turn to run but the moment your vison
            leaves the tree something hits your back""")
            pause("gravely wounded you retreat with haste")
            hp = 1
            print("hp is now 1")
            heart_wood()
        elif answer == "n" or answer == "N":
            pause("""suddenly you're attacked by
            a dangerous enemy with glowing black eyes""")
            hard()
            pause("""you begin chipping away at the amber
            and as you go along you feel weaker than ever before""")
            pause("""a voice deep within your mind
            asks you 'relent upon this folly please'""")
            pause("""'you weaken yourself beyond repair
            i ask, for your saefty, cease'""")
        else:
            pause("unexpected input try again")
            while (True):
                relent = input("relent? y/n\n")
                if relent == "y" or relent == "Y":
                    game_over()
                elif relent == "n" or relent == "N":
                    pause("""you push on despite the plea
                    and finally aquire the orb you sought""")
                    pause("""taking a moment to catch your breath
                    you realize you can hear again""")
                    pause("""this orb you hold has immense power and is
                    a larger version of the ancient orbs you have seen""")
                    pause("""you feel your strength return greater
                    than before as you place the orb in your pouch""")
                    power += 20
                    defence += 10
                    max_hp += 40


def wolf():
    return [13, 0, 7, 2, 1]


def bear():
    return [17, 2, 9, 5, 1]


def deer():
    return [7, 3, 3, 1, 1]


def squirrel():
    return [3, 5, 5, 2, 1]


def snake():
    return [25, 8, 15, 10, 2]


def raptor():
    return [30, 5, 20, 15, 2]


def dreadwolf():
    return [26, 4, 14, 10, 2]


def multibear():
    return [40, 10, 17, 30, 2]


def bloodwolf():
    return [50, 15, 30, 50, 3]


def drake():
    return [60, 20, 35, 60, 3]


def specter():
    return [20, 35, 30, 75, 3]


def harpy():
    return [40, 30, 25, 50, 3]


def fight(enemy):
    enemy_hp = enemy[0]
    enemy_defence = enemy[1]
    enemy_attack = enemy[2]
    enemy_xp = enemy[3]
    location = enemy[4]
    global hp
    global power
    global defence
    global xp
    global xp_max
    while hp > 0 and enemy_hp > 0:
        enemy_hp -= player_action(location, enemy_defence)
        damage = random.randint(enemy_attack - 3, enemy_attack + 3) - defence
        if damage < 1:
            damage = 1
        hp -= damage
        print("you take", damage, "damage")
        if hp < 0:
            hp = 0
        if enemy_hp < 0:
            enemy_hp = 0
        print("you have", hp, "hp")
        print("the enemy has", enemy_hp, "hp")
    if hp <= 0:
        game_over()
    else:
        print("you win you get ", str(enemy_xp), " xp")
        xp += enemy_xp
        if xp >= xp_max:
            level_up()
        if location == 1:
            easy_loot()
            game_trail()
        elif location == 2:
            medium_loot()
            dark_forest()
        elif location == 3:
            hard_loot()
            heart_wood()
        elif location == 4:
            you_win()


def player_action(location, enemy_defence):
    pause("what will you do?")
    action = input("(1) attack\n(2) use item\n(3) run\n")
    if action == "1":
        value = random.randint(power-3, power+3) - enemy_defence
        if value < 1:
            value = 1
        pause("you attack for " + str(value) + " damage.")
        return (value)
    elif action == "2":
        if useitem() == 1:
            return (player_action(location, enemy_defence))
        else:
            return (0)
    elif action == "3":
        if random.randint(1, 3) == 1:
            pause("you can't get away.")
            return (0)
        else:
            if location == 1:
                pause("you retreat to the game trail.")
                game_trail()
            elif location == 2:
                pause("you retreat to the dark forest.")
                dark_forest()
            elif location == 3:
                pause("you retreat to the heart wood.")
                heart_wood()
            elif location == 4:
                pause("you sprint towords the clearing as fast as you can")
                clearing()
    else:
        pause("incorrect input try again")
        return (player_action(location, enemy_defence))


def useitem():
    global potions
    global hp
    global max_hp
    if potions == []:
        pause("no potions avaliable")
        return 1
    pause("use?")
    if "lesser healing potion" in potions:
        number = potions.count("lesser healing potion")
        print("1: lesser healing potion" + '(' + str(number) + ')' + "\n")
    if "healing potion" in potions:
        number = potions.count("healing potion")
        print("2: healing potion" + '(' + str(number) + ')' + "\n ")
    if "greater healing potion" in potions:
        number = potions.count("greater healing potion")
        print("3: greater healing potion" + '(' + str(number) + ')' + "\n ")
    print("4: back\n")
    answer = str(input())
    if answer == "1":
        if "lesser healing potion" in potions:
            was_hp = hp
            hp += 15
            if hp > max_hp:
                hp = max_hp
            potions.remove("lesser healing potion")
        else:
            pause("none left")
            return useitem()
    if answer == "2":
        if "healing potion" in potions:
            was_hp = hp
            hp += 30
            if hp > max_hp:
                hp = max_hp
            potions.remove("healing potion")
        else:
            pause("none left")
            return useitem()
    if answer == "3":
        if "greater healing potion" in potions:
            was_hp = hp
            hp = max_hp
            potions.remove("greater healing potion")
        else:
            pause("none left")
            return useitem()
    if answer == "4":
        return 1
    if answer not in ["1", "2", "3", "4"]:
        print("try again")
        return (useitem())
    pause("you healed " + str(hp - was_hp) + " pts")
    return 0


def easy():
    enemies = ["wolf", "bear", "deer", "squirrel"]
    enemy = (random.choice(enemies))
    pause("you find a " + enemy)
    fight(eval(enemy + "()"))


def easy_loot():
    global power
    global defence
    global max_hp
    global hp
    global weapons
    global armor
    global potions
    global artifacts
    loot = ["bone blade", "hide helmet", "lesser healing potion", "no", "no"]
    rare = ["lesser strength orb", "lesser tough orb", "lesser hearty orb"]
    reward = random.randint(1, 20)
    if reward == 20:
        pause("""in the animal's den you spot
        a shining object known as an ancient orb""")
        orb = random.choice(rare)
        pause("This one is a " + orb)
        artifacts.append(orb)
        if orb == "lesser strength orb":
            power += 2
        if orb == "lesser tough orb":
            defence += 1
        if orb == "lesser hearty orb":
            max_hp += 3
            hp += 3
    else:
        gear = random.choice(loot)
        if gear == "bone blade" and ("bone blade" in weapons) is False:
            power += 4
            weapons.append("bone blade")
        elif gear == "hide helmet" and ("hide helmet" in armor) is False:
            defence += 3
            armor.append("hide helmet")
        elif gear == "lesser healing potion":
            potions.append("lesser healing potion")
        else:
            pause("you find nothing of value in the animal's den")
            return
        pause("In the animal's den you find the materials for a " + gear)
        pause("you quickly assemble the item and put it in your pack")


def medium():
    enemies = ["snake", "raptor", "dreadwolf", "multibear"]
    enemy = (random.choice(enemies))
    pause("you find a " + enemy)
    fight(eval(enemy + "()"))


def medium_loot():
    global power
    global defence
    global max_hp
    global hp
    global weapons
    global armor
    global potions
    global artifacts
    loot = ["bone hammer", "hide armor", "healing potion", "no", "no"]
    rare_loot = ["strength orb", "tough orb", "hearty orb"]
    reward = random.randint(1, 20)
    if reward == 20:
        pause("""in the carcass of the great beast
        you spot a shining object known as an ancient orb""")
        orb = random.choice(rare_loot)
        pause("This one is a " + orb)
        artifacts.append(orb)
        if orb == "strength orb":
            power += 4
        if orb == "tough orb":
            defence += 2
        if orb == "hearty orb":
            max_hp += 6
            hp += 6
    else:
        gear = random.choice(loot)
        if gear == "bone hammer" and ("bone hammer" in weapons) is False:
            power += 6
            weapons.append("bone hammer")
        elif gear == "hide armor" and ("hide armor" in armor) is False:
            defence += 5
            armor.append("hide armor")
        elif gear == "healing potion":
            potions.append("healing potion")
        else:
            pause("you find nothing of value.")
            return
        pause("On the animal's carcass you find the materials for a " + gear)
        pause("you quickly assemble the item and put it in your pack")


def hard():
    enemies = ["bloodwolf", "drake", "specter", "harpy"]
    enemy = (random.choice(enemies))
    pause("you find a " + enemy)
    fight(eval(enemy + "()"))


def hard_loot():
    global power
    global defence
    global max_hp
    global hp
    global weapons
    global armor
    global potions
    global artifacts
    loot = ["poison", "steel plate", "greater healing potion", "no", "no"]
    rare_loot = ["titanic orb", "unbreakable orb", "abundant orb"]
    reward = random.randint(1, 25)
    if reward == 25:
        pause("""on the ground where the monster stood you spot
        a shining object known as an ancient orb""")
        orb = random.choice(rare_loot)
        pause("This one is a " + orb)
        artifacts.append(orb)
        if orb == "titanic orb":
            power += 8
        if orb == "unbreakable orb":
            defence += 5
        if orb == "abundant orb":
            max_hp += 10
            hp += 10
    else:
        gear = random.choice(loot)
        if gear == "poison" and ("poison" in weapons) is False:
            power += 6
            weapons.append("poison")
        elif gear == "steel plate" and ("steel plate" in armor) is False:
            defence += 5
            armor.append("steel plate")
        elif gear == "greater healing potion":
            potions.append("greater healing potion")
        else:
            pause("you find nothing of value.")
            return
        pause("in the monsters gear you find a " + gear)
        pause("you quickly assemble the item and put it in your pack")


def boss_battle():
    pause("""You press on and before long you enter
    another clearing filled with growling stronger than before.""")
    pause("""In the center of the clearing stands
    a collosal wolf maybe twenty times the size of a dreadwolf.""")
    pause("""Around the clearing there stands
    a horde of monsters and animals watching intently.""")
    pause("Suddenly the great beast attacks.")
    fight([150, 50, 45, 0, 4])


def you_win():
    pause("""As the titanic beast falls to the ground
    all the animals and monsters watching run in terror.""")
    pause("""Now that you have beaten the wolf no foe will fight you,
    in this forest you may do as you please.""")
    pause("""With the guardian of the forest disposed of
    you take anything you want and go back home richer than ever before.""")
    answer = input("You win\nplay again? (y/n)\n").lower()
    if answer == "y":
        start()
    elif answer == "n":
        exit()
    else:
        pause("try again.")
        you_win()


def check_gear():
    print("you have")
    pause("in your weapon pouch: " + ", ".join(weapons))
    pause("in your armor pouch: " + ",".join(armor))
    pause("on your potion belt: " + ",".join(potions))
    pause("in the artifact slot: " + ",".join(artifacts))


def start():
    stats()
    equipment()
    opening()
    clearing()


start()