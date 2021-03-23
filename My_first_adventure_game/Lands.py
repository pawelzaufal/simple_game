
import Spells_And_Weapons
fireball, icebolt, blessing = Spells_And_Weapons.game_spells
sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone = Spells_And_Weapons.game_equipment
burn, freeze, restore = Spells_And_Weapons.spells_effects
o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2 = Spells_And_Weapons.equipment_atributes
import Characters
empty_mana, full_mana, not_enought_gold, full_life, no_equipment, knight_not_allowed, mage_not_allowed, exit_place = Characters.status_list



class Land:

    def __init__(self, name):
        self.name = name
        self.enemies = []
        self.treasures = []


    def tawern(self, hero):
        print(f"Welcom to little tawern in {self.name}!")
        while True:
            answear = input(f"""
Take a look at our menu:
1. Check your life points
2. Check your mana points
3. Check your equimpent
4. Check your gold
5. Check your attack
6. Check your armor
7. Check your spellbook
8. Leave tavern
Choose what you want!
-> """)
            if answear == "1":
                print(f"You have {hero.life} of total {hero.total_life} life points")
            elif answear == "2":
                print(f"You have {hero.manapoll} of total {hero.max_mana} mana in your manapool")
            elif answear == "3":
                print(f"Take a look at your equipment:\n{hero.equipment_check()}")
            elif answear == "4":
                print(f"I can see you're pretty rich\nYou have {hero.gold} gold!")
            elif answear == "5":
                print(f"Your attack skills are impressive\nYou can attack with {hero.attack_check()} damge points")
            elif answear == "6":
                print(f"Strong defence!\nYou have {hero.armor} armor points")
            elif answear == "7":
                print(f"Take a look at your spellbook:\n{hero.spellbook_check()}")
            elif answear == "8":
                print(exit_place)
                break





        pass

    # The fight mechanics (for now):

    @staticmethod
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
                    print(
                        f"You win, and find {gold} gold and {equipment.Name}\nyour total gold now is {hero.gold}\nand you have {hero.equipment_check()}\nyour life after fight is {hero.life}")

                else:
                    gold = enemy.defeated()
                    hero.get_gold(gold)
                    print(
                        f"You win, and find {gold} gold\nyour total gold now is {hero.gold}\nnyour life after fight is {hero.life}")
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






