
import Spells_And_Weapons
fireball, icebolt, blessing = Spells_And_Weapons.game_spells
sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone = Spells_And_Weapons.game_equipment
burn, freeze, restore = Spells_And_Weapons.spells_effects
o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2 = Spells_And_Weapons.equipment_atributes

import Characters
empty_mana, full_mana, not_enought_gold, full_life, no_equipment, knight_not_allowed, mage_not_allowed, exit_place = Characters.status_list
import Settlement
import Lands


# TO DO:
            #how to waisly change buildings into classes, the same with spells and equipments,
            #class for places in general and then on this class raise buildings
            #places -> lairs, labirynths, castles
            # mayby class land, for mountains, swamps, fields, see, forests, for different places and enemys and rewards
            # main goal of the game -> the boss?, collect stones?, earn 1mln gold?, become a king, super hero?

# Making a hero for testing and sample main->game function, to simulate how things are working


def make_a_hero():
    name = input("What is your name? ")
    name = Characters.Hero(name)
    return name


def game():
     hero = make_a_hero()
     hero.get_equipment(sword)
     hero.get_equipment(ruby_stone)
     hero.get_equipment(sapphire_stone)
     print(hero.equipment_check())
     print(hero.equipment)
     hero.get_gold(300)
     print(hero.gold)
     print(f"You have {hero.life} life\n{hero.attack} attack points\n{hero.manapoll} mana")
     norman = Characters.Warrior("Norman", 10, 10)
     print("There is Norman the warrior on your way")
     fight_decision = input("Do you fight? (Yes/No) ")
     town = Lands.Land("Town")
     if fight_decision == "Yes":
         town.fight(hero, norman)
     guild = input("Do you want to go to tawern? (Yes/No) ")
     if guild == "Yes":
        town.tawern(hero)
     print(hero.gold)

     pass
game()
