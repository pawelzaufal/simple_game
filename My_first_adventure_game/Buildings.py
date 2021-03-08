#Funkcje opisujące działanie budynków:

import Spells_And_Weapons
fireball, icebolt, blessing = Spells_And_Weapons.game_spells
sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone = Spells_And_Weapons.game_equipment
burn, freeze, restore = Spells_And_Weapons.spells_effects
o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2 = Spells_And_Weapons.equipment_atributes
import Characters

# Gildia magów:

def buy_a_spell_in_magic_guild(hero):
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

def refill_manapoll_in_magic_guild(hero):
    question = input("Do you want to refill your manapool for 200 gold? (Yes/No) -> ")
    if question == "Yes":
        if hero.gold >= 200:
            hero.gold = hero.gold - 200
            hero.manapoll = hero.max_mana
        else:
            return print(Characters.not_enought_gold)
    else:
        return print(Characters.exit_place)

def magic_guild(hero):
    buy_a_spell_in_magic_guild(hero)
    refill_manapoll_in_magic_guild(hero)

# Warsztat kowala:

def buy_from_a_blacksmith(hero):
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


def sell_to_the_blacksmith(hero):
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


def blcksmiths_workshop(hero):
    buy_from_a_blacksmith(hero)
    sell_to_the_blacksmith(hero)

