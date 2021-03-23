
import random
import Spells_And_Weapons
fireball, icebolt, blessing = Spells_And_Weapons.game_spells
sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone = Spells_And_Weapons.game_equipment
burn, freeze, restore = Spells_And_Weapons.spells_effects
o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2 = Spells_And_Weapons.equipment_atributes
import Characters
empty_mana, full_mana, not_enought_gold, full_life, no_equipment, knight_not_allowed, mage_not_allowed, exit_place = Characters.status_list
import Lands


class Settlement(Lands.Land):

    def __init__(self, name):
        super().__init__(name)



#Methods for settlement buildings:

# Mage Guild:


    def buy_a_spell_in_mage_guild(self, hero):
        print(f"You can buy a spell\nfireball for {fireball.Price} gold\nicebolt for {icebolt.Price} gold\nblessig for {blessing.Price} gold")
        question = input("Do you want to buy any of this spells? (Yes/No) -> ")
        if question == "Yes":
            spell = input("Which one: (fireball, icebolt, blessing) -> ")
            if spell == "fireball":
                return hero.buy_a_spell(fireball, fireball.Price)
            elif spell == "icebolt":
                return hero.buy_a_spell(icebolt, icebolt.Price)
            elif spell == "blessing":
                return hero.buy_a_spell(blessing, blessing.Price)


    def refill_manapoll_in_mage_guild(self, hero):
        question = input("Do you want to refill your manapool for 200 gold? (Yes/No) -> ")
        if question == "Yes":
            if hero.gold >= 200:
                hero.gold = hero.gold - 200
                mana = hero.max_mana - hero.manapool
                return hero.fill_mana(mana)
            else:
                return print(Characters.not_enought_gold)
        else:
            return print(Characters.exit_place)


    def mage_guild(self, hero):
        self.buy_a_spell_in_mage_guild(hero)
        self.refill_manapoll_in_mage_guild(hero)


# Blacksmiths workshop:


    def buy_from_a_blacksmith(self, hero):
        print(f"You can buy here a weapon:\nsword for {sword.Price + 50}\naxe for {axe.Price + 50}\nshield for {shield.Price + 50}\narmour for {armour.Price + 50}\n")
        question = input("Do you want to buy any of these weapons? (Yes/No) -> ")
        if question == "Yes":
            weapon = input("Wich one do you want to buy: (sword, axe, shield, armour) -> ")
            if weapon == "sword":
                gold = sword.Price + 50
                return hero.buy_equipment(sword, gold)
            elif weapon == "axe":
                gold = axe.Price + 50
                return hero.buy_equipment(axe, gold)
            elif weapon == "shield":
                gold = shield.Price + 50
                return hero.buy_equipment(shield, gold)
            elif weapon == "armour":
                gold = armour.Price + 50
                return hero.buy_equipment(armour, gold)


    def sell_to_the_blacksmith(self, hero):
        question = input("If you want we can buy some of your inventory: (Yes/No) -> ")
        if question == "Yes":
            print("Let's see what you got here...")
            for equipment in hero.equipment:
                if equipment.Type == w:
                    print(f"We can buy {equipment.Name} for {equipment.Price - 50}")
                    weapon = input("Do you want to sell it for this price? (Yes/No) -> ")
                    if weapon == "Yes":
                        gold = equipment.Price - 50
                        hero.sell_equipment(equipment, gold)
                        continue
                    else:
                        continue
        else:
            return Characters.exit_place


    def blacksmiths_workshop(self, hero):
        self.buy_from_a_blacksmith(hero)
        self.sell_to_the_blacksmith(hero)


#Bazaar:


    def charlatan(self, hero):
        question = input(f"Welcome to\n'Bazaar Care Center'\nYou can restore your life\nWhether you agree\nto take full responsibility\nfor undesirable effects\nof our care\n(Yes/No)\n-> ")
        if question == "Yes":
            heal = input(f"1.Restoration of 10 life points costs 20gold\n2.Full life points restoration costs 100gold\n(1/2)\n-> ")
            if heal == "1":
                if hero.gold >= 20:
                    healing = [0, 5, 10]
                    effect = random.choice(healing)
                    print(f"The wind still blows where it wants to...\nToday we could restore {effect} of your life points\nYou heve {hero.life} life points now\n{exit_place}")
                    return hero.get_gold(-20), hero.get_life(effect)
                else:
                    return print(not_enought_gold)
            if heal == "2":
                if hero.gold >= 100:
                    full = hero.total_life - hero.life
                    half = (hero.total_life - hero.life) / 2
                    healing = [0, half, full]
                    effect = random.choice(healing)
                    print(f"The wind still blows where it wants to...\nToday we could restore {effect} of your life points\nYou have {hero.life} life points now\n{hero.total_life} is the limit of life points for you at the moment\n{exit_place}")
                    return hero.get_gold(-100), hero.get_life(effect)
                else:
                    return print(not_enought_gold)
        else:
            return print(exit_place)


    def market(self, hero):
        question = input(f"Welcom to our\n'Bazaar Market Center'\nDo you have any interesting things to sell?\n(Yes/No)\n-> ")
        if question == "Yes":
            if len(hero.equipment) > 0:
                for equipment in hero.equipment:
                    if equipment.Type == art:
                        price = equipment.Price - (equipment.Price / 5)
                        sell = input(f"This is really nice\nbut a little damaged\n{equipment.Name}\nwe can release you\nfrom carry this useless artifact\nfor {price} gold!\nand belive me\nthis is the best price\nthat you can get for it\nDo you agree?\n(Yes/No)\n-> ")
                        if sell == "Yes":
                            hero.sell_equipment(equipment, price)
                            print(f"we will take care about {equipment.Name}\nHere is your {price} gold!")

                        else:
                            print("Oh, maybe next time...")

            else:
                print(no_equipment)
        question = input(f"You can also buy some weapons here\nDo you want anything?\n(Yes/No)\n-> ")
        if question == "Yes":
            assortment = [sword, axe, shield, armour, wand, mage_robe]
            today = random.choice(assortment)
            price = today.Price - (today.Price / random.randint(4, 9))
            buy = input(f"Today we heve\n{today.Name}\nolny for {price} gold\nDo you want it?\n(Yes/No)\n-> ")
            if buy == "Yes":
                hero.buy_equipment(today, price)
                print(f"Take good care of {today.Name}")
        print(exit_place)


    def witch(self, hero):
        question = input(f"I can see...\nyou\nyour\nwho are you?\n ")
        if question == hero.name:
            print("UUHH\nyes\nnow I can see\nyes\nclearly\nyes")
            print("\nMay the Python be with you...\n")
            question = input("Would you like to show me what you got?\n(Yes/No)\n ")
            if question == "Yes":
                counter = 0
                for equipment in hero.equipment:
                    if equipment.Type == art:
                        counter += 1
                if counter >= 2:
                    print("Some interesting stones you got")
                    question = input("I can try to combine them\nbut it is an ancient art\nof mystrrious legendary\nrecipes of the witches\nfor you only for 50 gold\nAre we cooking or not?\n(Yes/No)\n ")
                    if question == "Yes":
                        if hero.gold >= 50:
                            hero.get_gold(-50)
                            counter = 0
                            equipments_list = []
                            for equipment in hero.equipment:
                                if equipment.Type == art:
                                    counter += 1
                                    equipments_list.append((counter, equipment))
                                    print(counter, equipment.Name)

                            first_ingredient = input("Choose the number of first ingredient -> ")
                            second_ingredient = input("Choose another -> ")
                            stones_price = 0
                            for ingredient in equipments_list:
                                if first_ingredient == ingredient[0]:
                                    first = ingredient[1]
                                    stones_price += first.Price

                                elif second_ingredient == ingredient[0]:
                                    second = ingredient[1]
                                    stones_price += second.Price

                            if stones_price < 100:
                                witch_menu = ["gold", "life", "mana", "attack", "armor", "damage"]
                                the_dish = random.choice(witch_menu)
                                if the_dish == "gold":
                                    hero.get_gold(100)
                                    print(f"The wind still blows where it wants to\nYou have {hero.gold} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_gold(100)
                                elif the_dish == "life":
                                    hero.total_life = hero.total_life + 10
                                    hero.get_life(10)
                                    print(f"The wind still blows where it wants to\nYou have {hero.life} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.total_life, hero.get_life(10)
                                elif the_dish == "mana":
                                    hero.max_mana = hero.max_mana + 10

                                    print(f"The wind still blows where it wants to\nYou have {hero.max_mana} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.max_mana, hero.fill_mana(10)
                                elif the_dish == "attack":
                                    hero.attack = hero.attack + 5
                                    print(f"The wind still blows where it wants to\nYou have {hero.attack} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.attack
                                elif the_dish == "armor":
                                    hero.armor = hero.armor + 5
                                    print(f"The wind still blows where it wants to\nYou have {hero.armor} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.armor
                                elif the_dish == "damage":
                                    hero.damage = hero.damage + 5
                                    print(f"The wind still blows where it wants to\nYou have {hero.damage} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.damage
                            elif 100 <= stones_price < 300:
                                witch_menu = ["gold", "life", "mana", "attack", "damage", "armor", "equimpent"]
                                equipments_list = [sword, shield]
                                the_dish = random.choice(witch_menu)
                                if the_dish == "gold":
                                    hero.get_gold(300)
                                    print(f"The wind still blows where it wants to\nYou have {hero.gold} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_gold(300)
                                elif the_dish == "life":
                                    hero.total_life = hero.total_life + 30
                                    hero.get_life(30)
                                    print(f"The wind still blows where it wants to\nYou have {hero.life} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.total_life, hero.get_life(30)
                                elif the_dish == "mana":
                                    hero.max_mana = hero.max_mana + 30

                                    print(f"The wind still blows where it wants to\nYou have {hero.max_mana} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.max_mana, hero.fill_mana(30)
                                elif the_dish == "attack":
                                    hero.attack = hero.attack + 10
                                    print(f"The wind still blows where it wants to\nYou have {hero.attack} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.attack
                                elif the_dish == "armor":
                                    hero.armor = hero.armor + 10
                                    print(f"The wind still blows where it wants to\nYou have {hero.armor} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.armor
                                elif the_dish == "damage":
                                    hero.damage = hero.damage + 10
                                    print(f"The wind still blows where it wants to\nYou have {hero.damage} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.damage
                                elif the_dish == "equipment":
                                    reward = random.choice(equipments_list)
                                    print(f"The wind still blows where it wants to\nYou have {reward.Name} in your {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_equipment(reward)
                            elif 300 <= stones_price < 500:
                                witch_menu = ["gold", "life", "mana", "attack", "damage", "armor", "equimpent", "spell"]
                                equipments_list = [sword, axe, shield, wand]
                                spells_list = [icebolt, blessing]
                                the_dish = random.choice(witch_menu)
                                if the_dish == "gold":
                                    hero.get_gold(500)
                                    print(f"The wind still blows where it wants to\nYou have {hero.gold} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_gold(500)
                                elif the_dish == "life":
                                    hero.total_life = hero.total_life + 50
                                    hero.get_life(50)
                                    print(f"The wind still blows where it wants to\nYou have {hero.life} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.total_life, hero.get_life(50)
                                elif the_dish == "mana":
                                    hero.max_mana = hero.max_mana + 50
                                    print(f"The wind still blows where it wants to\nYou have {hero.max_mana} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.max_mana,  hero.fill_mana(50)
                                elif the_dish == "attack":
                                    hero.attack = hero.attack + 20
                                    print(f"The wind still blows where it wants to\nYou have {hero.attack} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.attack
                                elif the_dish == "armor":
                                    hero.armor = hero.armor + 20
                                    print(f"The wind still blows where it wants to\nYou have {hero.armor} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.armor
                                elif the_dish == "damage":
                                    hero.damage = hero.damage + 20
                                    print(f"The wind still blows where it wants to\nYou have {hero.damage} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.damage
                                elif the_dish == "equipment":
                                    reward = random.choice(equipments_list)
                                    print(f"The wind still blows where it wants to\nYou have {reward.Name} in your {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_equipment(reward)
                                elif the_dish == "spell":
                                    reward = random.choice(spells_list)
                                    print(f"The wind still blows where it wants to\nYou have {reward.Name} in your spellbook now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.learn_a_spell(reward)
                            elif stones_price >= 500:
                                witch_menu = ["gold", "life", "mana", "attack", "damage", "armor", "equimpent", "spell"]
                                equipments_list = [sword, axe, shield, armour, wand, mage_robe]
                                spells_list = [fireball, icebolt, blessing]
                                the_dish = random.choice(witch_menu)
                                if the_dish == "gold":
                                    hero.get_gold(1000)
                                    print(f"The wind still blows where it wants to\nYou have {hero.gold} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_gold(1000)
                                elif the_dish == "life":
                                    hero.total_life = hero.total_life + 100
                                    hero.get_life(100)
                                    print(f"The wind still blows where it wants to\nYou have {hero.life} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.total_life,)
                                elif the_dish == "mana":
                                    hero.max_mana = hero.max_mana + 100
                                    print(f"The wind still blows where it wants to\nYou have {hero.max_mana} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.max_mana, hero.fill_mana(100)
                                elif the_dish == "attack":
                                    hero.attack = hero.attack + 30
                                    print(f"The wind still blows where it wants to\nYou have {hero.attack} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.attack
                                elif the_dish == "armor":
                                    hero.armor = hero.armor + 30
                                    print(f"The wind still blows where it wants to\nYou have {hero.armor} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.armor
                                elif the_dish == "damage":
                                    hero.damage = hero.damage + 30
                                    print(f"The wind still blows where it wants to\nYou have {hero.damage} {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.damege
                                elif the_dish == "equipment":
                                    reward = random.choice(equipments_list)
                                    print(f"The wind still blows where it wants to\nYou have {reward.Name} in your {the_dish} now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.get_equipment(reward)
                                elif the_dish == "spell":
                                    reward = random.choice(spells_list)
                                    print(f"The wind still blows where it wants to\nYou have {reward.Name} in your spellbook now\nthanks to my cooking ablities")
                                    return hero.sell_equipment(second, 0), hero.sell_equipment(first, 0), hero.learn_a_spell(reward)
                        else:
                            return print(not_enought_gold)
                else:
                    return print(f"I need at least two ingredients...\nThe wind still blows where it wants to...\n{exit_place}")
        else:
            return print("...", exit_place)



    def bazaar(self, hero):
        while True:
            question = input("Where would you like to go to?\n1.'Bazaar Care Center'\n2.'Bazaar Market Center'\n3.'The Witch'\n4.leave bazzar ")
            if question == "1":
                self.charlatan(hero)
            if question == "2":
                self.market(hero)
            if question == "3":
                self.witch(hero)
            if question == "4":
                print(exit_place)
                break


    def main_square(self, hero):
        print(f"Hello {hero.name}!\nFeel welcome to rock {self.name}")
        while True:
            place = input(f"""Which place would you like to visit?
1. Tawern
2. Bazaar
3. Mage guild
4. Blacksmith workshop
5. Say 'goodbye' to {self.name}
""")
            if place == "1":
                self.tawern(hero)
            elif place == "2":
                self.bazaar(hero)
            elif place == "3":
                self.mage_guild(hero)
            elif place == "4":
                self.blacksmiths_workshop(hero)
            elif place == "5":
                print(exit_place)
                break


# if __name__ == '__main__':
#     pass