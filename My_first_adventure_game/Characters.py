# charakterystyka postaci, bohaterów

import random
import Spells_And_Weapons
fireball, icebolt, blessing = Spells_And_Weapons.game_spells
sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone = Spells_And_Weapons.game_equipment
burn, freeze, restore = Spells_And_Weapons.spells_effects
o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2 = Spells_And_Weapons.equipment_atributes

#komunikaty statystyk i umiejętności:

empty_mana = "You have not enough mana in your manapool..."
full_mana = "You have already full manapool..."
not_enought_gold = "You have not enough gold..."
full_life = "You can't get more life..."
no_equipment = "You have no equipment"
knight_not_allowed = "Knight can not buy a magical equipment..."
mage_not_allowed = "Mage can not buy weapon..."
exit_place = "Good Bye stranger! May the Python by with you..."

class Hero:

    def __init__(self, name):
        self.name = name
        self.total_life = 30
        self.life = 30
        self.max_mana = 30
        self.manapoll = 30
        self.gold = 20
        self.equipment = []
        self.spellbook = []
        self.attack = 5
        self.armor = 0
        self.damage = 0

    def spellbook_check(self):
        spells = []
        for spell in self.spellbook:
            spells.append(spell.Name)
        return spells

    def attack_check(self):
        info_damage = self.damage
        for equipment in self.equipment:
            info_damage = info_damage + equipment.Damage
        info_damage = info_damage + self.attack
        return info_damage

    def equipment_check(self):
        equipments = []
        for equipment in self.equipment:
            equipments.append(equipment.Name)
        if len(equipments) == 0:
            return no_equipment
        else:
            return equipments

    def get_life(self, life):
        if self.life < self.total_life:
            if self.life + life > self.total_life:
                self.life = self.total_life
            else:
                self.life = self.life + life
        else:
            return full_life

    def loose_life(self, life):
        self.life = self.life - life

    def get_equipment(self, equipment):
        self.equipment.append(equipment)

    def get_gold(self, gold):
        self.gold = self.gold + gold

    def buy_equipment(self, equipment, gold):
        if self.gold >= equipment.Price:
            self.gold = self.gold - gold
            self.equipment.append(equipment)
        else:
            return print(not_enought_gold)

    def sell_equipment(self, equipment, gold):
        self.equipment.remove(equipment)
        self.gold = self.gold + gold

    def buy_a_spell(self, spell, gold):
        if self.gold >= spell.Price:
            self.gold = self.gold - gold
            self.spellbook.append(spell)
        else:
            return print(not_enought_gold)

    def learn_a_spell(self, spell):
        self.spellbook.append(spell)

    def fill_mana(self, mana):
        if self.manapoll < self.max_mana:
            if self.manapoll + mana > self.max_mana:
                self.manapoll = self.max_mana
            else:
                self.manapoll = self.manapoll + mana
        else:
            return print(full_mana)

    def cast_a_spell(self, spell):
        cost = spell.Mana
        damage = spell.Damage
        for equipment in self.equipment:
            if equipment.Effect == reduce1:
                cost = spell.Mana - (spell.Mana / 4)
                damage = spell.Damage + (spell.Damage / 4)
            if equipment.Effect == reduce2:
                cost = spell.Mana - (spell.Mana / 2)
                damage = spell.Damage + (spell.Damage / 2)

        if  self.manapoll >= cost:
            self.manapoll = self.manapoll - cost
            self.damage = self.damage + damage
            if spell.Effect == burn:
                pass
            if spell.Effect == freeze:
                pass
            if spell.Effect == restore:
                self.life = self.total_life
        else:
            return print(empty_mana)

    def fight(self):
        for equipment in self.equipment:
            self.damage = self.damage + equipment.Damage
        self.damage = self.damage + self.attack

class Knight(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.total_life = 50
        self.life = self.life + (self.total_life - self.life)
        self.max_mana = 20
        self.manapoll = 20
        self.armor = 20
        self.attack = 25

    def buy_equipment(self, equipment, gold):
        if equipment.Type == w:
            self.gold = self.gold - (gold / 2)
            self.equipment.append(equipment)
        else:
            return print(knight_not_allowed)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.total_life = 40
        self.life = self.life + (self.total_life - self.life)
        self.max_mana = 50
        self.manapoll = 50
        self.armor = 5
        self.attack = 10
        self.spellbook.append(fireball)

    def buy_equipment(self, equipment, gold):
        if equipment.Type == m_w:
            self.gold = self.gold - (gold / 2)
            self.equipment.append(equipment)
        else:
            return print(mage_not_allowed)

class Enemy:
    def __init__(self, name, attack, life):
        self.name = name
        self.attack = attack
        self.life = life
        self.damage = 0
        self.armor = 0
        self.gold = 0
        self.equipment = []

    def loose_life(self, life):
        self.life = self.life - life

    def fight(self):
        for equipment in self.equipment:
             self.damage = self.damage + equipment.Damage
        self.damage = self.damage + self.attack

    def defeated(self):
        gold = self.gold + random.randint(0, 25)
        if len(self.equipment) > 0:
            equipment = random.choice(self.equipment)
            return gold, equipment
        else:
            return gold

class Warrior(Enemy):
    def __init__(self, name, attack, life):
        super().__init__(name, attack, life)
        self.damage = 10
        self.armor = 10
        self.gold = 10
        self.equipment = [sword, shield, stone, stone, stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone]

class Ogr(Enemy):
    def __init__(self, name, attack, life):
        super().__init__(name, attack, life)
        self.damage = 20
        self.armor = 30
        self.gold = 50
        self.equipment = [axe, stone, stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone, golden_stone, silver_stone, emerald_stone]

class Skeleton(Enemy):
    def __init__(self, name, attack, life):
        super().__init__(name, attack, life)
        self.damage = 5
        self.armor = 5
        self.gold = 5
        self.equipment = [sword, armour, stone, stone, stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone, bronze_stone]

class Dragon(Enemy):
    def __init__(self, name, attack, life):
        super().__init__(name, attack, life)
        self.damage = 30
        self.armor = 20
        self.gold = 100
        self.equipment = [wand, mage_robe, emerald_stone, sapphire_stone, ruby_stone, diamond_stone, crystal_stone]




def fight(hero, enemy):
    while True:
        if len(hero.spellbook) > 0 and hero.cast_a_spell(fireball) != empty_mana and hero.cast_a_spell(icebolt) != empty_mana and hero.cast_a_spell(blessing) != empty_mana:
            magic = input("Do you want to use a spell? (Yes/No) -> ")
            if magic == "Yes":
                spell = input(f"Choose a spell from your spellbook: ({hero.spellbook_check()} -> ")
                if spell == "fireball":
                    hero.cast_a_spell(fireball)
                    print(f"You have {hero.manapoll} mana in your manapool.")
                elif spell == "icebolt":
                    hero.cast_a_spell(icebolt)
                    print(f"You have {hero.manapoll} mana in your manapool.")
                elif spell == "blessing":
                    hero.cast_a_spell(blessing)
                    print(f"You have {hero.manapoll} mana in your manapool.")
            else:
                break
        else:
            break
    hero.fight()
    while True:
        if hero.damage >= enemy.life:
            if len(enemy.defeated()) > 1:
                gold, equipment = enemy.defeated()
                hero.get_gold(gold)
                hero.get_equipment(equipment)
                print(f"You win, and find {gold} gold and {equipment.Name}\nyour total gold now is {hero.gold}\nand you have {hero.equipment_check()}\nyour life after fight is {hero.life}")

            else:
                gold = enemy.defeated()
                hero.get_gold(gold)
                print(f"You win, and find {gold} gold\nyour total gold now is {hero.gold}\nnyour life after fight is {hero.life}")
            break
        elif hero.damage < enemy.life:
            enemy.loose_life(hero.damage)
            enemy.fight()
            hero.loose_life(enemy.damage)
            if hero.life <= 0:
                print(f"Game Over")
                break
            else:
                continue

def make_a_hero():
    name = input("What is your name? ")
    name = Hero(name)
    return name

def charlatan(hero):
    question = input(f"Welcome to\n'Bazaar Care Center'\nYou can restore your life\nWhether you agree\nto take full responsibility\nfor undesirable effects\nof our care\n(Yes/No)\n-> ")
    if question == "Yes":
        heal = input(f"1.Restoration of 10 life points costs 20gold\n2.Full life points restoration costs 100gold\n(1/2)\n-> ")
        if heal == "1":
            if hero.gold >= 20:
                hero.get_gold(-20)
                healing = [0, 5, 10]
                effect = random.choice(healing)
                hero.get_life(effect)
                print(f"The wind still blows where it wants to...\nToday we could restore {effect} of your life points\n{exit_place}")
            else:
                return print(not_enought_gold)
        if heal == "2":
            if hero.gold >= 100:
                hero.get_gold(-100)
                full = hero.total_life - hero.life
                half = (hero.total_life - hero.life) / 2
                healing = [0, half, full]
                effect = random.choice(healing)
                hero.get_life(effect)
                print(f"The wind still blows where it wants to...\nToday we could restore {effect} of your life points\n{exit_place}")
            else:
                return print(not_enought_gold)
    else:
        return print(exit_place)

def market(hero):
    question = input(f"Welcom to our\n'Bazaar Market Center'\nDo you have any interesting things to sell?\n(Yes/No)\n-> ")
    if question == "Yes":
        if len(hero.equipment) > 0:
            for equipment in hero.equipment:
                if equipment.Type == art:
                    price = equipment.Price - (equipment.Price / 5)
                    sell = input(f"This is really nice\nbut a little damagedn\n{equipment.Name}\nwe can release you\nfrom carry this useless artifact\nfor {price} gold!\nand belive me\nthis is the best price\nthat you can get for it\nDo you agree?\n(Yes/No)\n-> ")
                    if sell == "Yes":
                        hero.sell_equipment(equipment, price)
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
    print(exit_place)




def bazaar(hero):
    while True:
        question = input("Where would you like to go?\n1.'Bazaar Care Center'\n2.'Bazaar Market Center'\n3.leave bazzar ")
        if question == "1":
            charlatan(hero)
        if question == "2":
            market(hero)
        if question == "3":
            print(exit_place)
            break







def game():
     hero = make_a_hero()
     hero.get_equipment(sword)
     print(hero.equipment_check())
     print(hero.equipment)
     print(f"You have {hero.life} life\n{hero.attack} attack points\n{hero.manapoll} mana")
     norman = Warrior("Norman", 10, 10)
     print("There is Norman the warrior on your way")
     fight_decision = input("Do you fight? (Yes/No) ")
     if fight_decision == "Yes":
         fight(hero, norman)
     guild = input("Do you want to go to bazaar? (Yes/No) ")
     if guild == "Yes":
         bazaar(hero)
     print(hero.gold)

     pass
game()
















