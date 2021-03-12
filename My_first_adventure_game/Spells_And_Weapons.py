import collections


# Spells description:


Spell = collections.namedtuple('Spell', ['Name', 'Mana', 'Damage', 'Effect', 'Price'])

burn = "burn"
freeze = "freeze"
restore = "restore your total life points"

spells_effects = (burn, freeze, restore)

fireball = Spell("fireball", 10, 15, burn, 200)
icebolt = Spell("icebolt", 5, 5, freeze, 150)
blessing = Spell("blessing", 5, 0, restore, 100)

game_spells = (fireball, icebolt, blessing)


# Equipment description:


Equipment = collections.namedtuple('Equipment', ['Name', 'Type', 'Damage', 'Armor', 'Placement', 'Effect', 'Price'])

o_h = "one-handed equipment"
t_h = "two_handed equipment"
carry = "wear on yourself or carry with you"
f_w = "this weapon increase your damge in fights"
d_w = "this weapon increase your armor to protect you in fights"
w = "weapon"
m_w = "magical weapon"
art = "artifct"
sell = "You can sell it in a proper place"
reduce1 = "reduce the cost of spells by 25%, increase spell damge by 25%"
reduce2 = "reduce the cost of spells by 50%, increase spell damge by 50%"

equipment_atributes = (o_h, t_h, carry, f_w, d_w, w, m_w, art, sell, reduce1, reduce2)

sword = Equipment("sword", w, 10, 0, o_h, f_w, 200)
axe = Equipment("axe", w, 15, 0, t_h, f_w, 250)
shield = Equipment("shield", w, 0, 10, o_h, d_w, 150)
armour = Equipment("armour", w, 0, 20, carry, d_w, 300)
wand = Equipment("wand", m_w, 0, 0, o_h, reduce1, 200)
mage_robe = Equipment("mage robe", m_w, 0, 10, carry, reduce2, 300)
stone = Equipment("stone", art, 1, 0, o_h, f_w, 0)
bronze_stone = Equipment("bronze stone", art, 0, 0, carry, sell, 25)
golden_stone = Equipment("golden stone", art, 0, 0, carry, sell, 100)
silver_stone = Equipment("silver stone", art, 0, 0, carry, sell, 150)
crystal_stone = Equipment("crystal stone", art, 0, 0, carry, sell, 300)
ruby_stone = Equipment("ruby stone", art, 0, 0, carry, sell, 200)
emerald_stone = Equipment("emerald stone", art, 0, 0, carry, sell, 200)
sapphire_stone = Equipment("sapphire stone", art, 0, 0, carry, sell, 200)
diamond_stone = Equipment("diamond", art, 0, 0, carry, sell, 500)

game_equipment = (sword, axe, shield, armour, wand, mage_robe, stone, bronze_stone, golden_stone, silver_stone, crystal_stone, ruby_stone, emerald_stone, sapphire_stone, diamond_stone)

def spells_and_equimnet():
    return game_spells, spells_effects, game_equipment, equipment_atributes

if __name__ == '__main__':
    spells_and_equimnet()
