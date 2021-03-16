
import Spells_And_Weapons
fireball, icebolt, blessing = Spells_And_Weapons.game_spells
sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone = Spells_And_Weapons.game_equipment
burn, freeze, restore = Spells_And_Weapons.spells_effects
o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2 = Spells_And_Weapons.equipment_atributes
import Characters
empty_mana, full_mana, not_enought_gold, full_life, no_equipment, knight_not_allowed, mage_not_allowed, exit_place = Characters.status_list



class Land:

    def __init__(self, name, boss, gold, hero):
        self.name = name
        self.boss = boss
        self.gold = gold
        self.hero = hero
        self.enemies = []
        self.treasures = []


    # The fight mechanics (for now):

    @staticmethod
    def fight(hero, enemy):
        while True:
            if len(hero.spellbook) > 0 and hero.cast_a_spell(fireball) != empty_mana and hero.cast_a_spell(
                    icebolt) != empty_mana and hero.cast_a_spell(blessing) != empty_mana:
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






