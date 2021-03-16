

class Land:

    def __init__(self, name, boss, gold, hero):
        self.name = name
        self.boss = boss
        self.gold = gold
        self.hero = hero
        self.enemies = []
        self.treasures = []

    def land_enemies(self, *enemies):
        return self.enemies.append(*enemies)

    def land_treasures(self, *treasures):
        return self.treasures.append(*treasures)







