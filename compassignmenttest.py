"""
File: compassignmenttest.py
Description: The implementation of the behaviour of an alchemist who is owned by a laboratory. In the laboratory an alchemist can mix and drink potions as
well collect and refine reagents. Potions and reagents are stored in a laboratory.
Author: Yujin Chen
StudentID: 110357638
EmailID: cheyy364
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest

from .compassignmentmain import Alchemist, Reagent, Herb, Catalyst, SuperPotion, ExtremePotion, Laboratory

def initOptions():
    super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
    super_strength = SuperPotion("Super Strength", "strength", Herb("Kwuarm", 6), Catalyst("Limpwurt Root", 4, 10))
    super_defence = SuperPotion("Super Defence", "defence", Herb("Cadantine", 9), Catalyst("White Berries", 7, 9))
    super_magic = SuperPotion("Super Magic", "magic", Herb("Lantadyme", 10), Catalyst("Potato Cactus", 2, 5))
    super_ranging = SuperPotion("Super Ranging", "ranging", Herb("Dwarf Weed", 2), Catalyst("Wine of Zamorak", 7, 6))
    super_necromancy = SuperPotion("Super Necromancy", "necromancy", Herb("Arbuck", 9), Catalyst("Blood of Orcus", 9, 3))

    extreme_attack = ExtremePotion("Extreme Attack", "attack", Catalyst("Avantoe", 6, 3), super_attack)
    extreme_strength = ExtremePotion("Extreme Strength", "strength", Herb("Dwarf Weed", 6), super_strength)
    extreme_defence = ExtremePotion("Extreme Defence", "defence", Herb("Lantadyme", 9), super_defence)
    extreme_magic = ExtremePotion("Extreme Magic", "magic", Herb("Ground Mud Rune", 6), super_magic)
    extreme_ranging = ExtremePotion("Extreme Ranging", "ranging", Herb("Grenwall Spike", 6), super_ranging)
    extreme_necromancy = ExtremePotion("Extreme Necromancy", "necromancy", Herb("Ground Miasma Rune", 6), super_necromancy)
    return [super_attack, super_strength, super_defence, super_magic, super_ranging,
            super_necromancy, extreme_attack, extreme_strength, extreme_defence, extreme_magic,
            extreme_ranging, extreme_necromancy]

def initHerbs():
    herbs = []
    herbs.append(Herb("Irit", 4))
    herbs.append(Herb("Kwuarm", 6))
    herbs.append(Herb("Cadantine", 9))
    herbs.append(Herb("Lantadyme", 10))
    herbs.append(Herb("Dwarf Weed", 2))
    herbs.append(Herb("Arbuck", 9))
    herbs.append(Herb("Dwarf Weed", 6))
    herbs.append(Herb("Lantadyme", 9))
    herbs.append(Herb("Ground Mud Rune", 6))
    herbs.append(Herb("Grenwall Spike", 6))
    herbs.append(Herb("Ground Miasma Rune", 6))
    return herbs

def initCatalysts():
    catalysts = []
    catalysts.append(Catalyst("Eye of Newt", 5, 7))
    catalysts.append(Catalyst("Limpwurt Root", 4, 10))
    catalysts.append(Catalyst("White Berries", 7, 9))
    catalysts.append(Catalyst("Potato Cactus", 2, 5))
    catalysts.append(Catalyst("Wine of Zamorak", 7, 6))
    catalysts.append(Catalyst("Blood of Orcus", 9, 3))
    catalysts.append(Catalyst("Avantoe", 6, 3))
    return catalysts


def initRecipes():
    recipes = {}
    recipes['Super Attack'] = ["Irit", "Eye of Newt"]
    recipes['Super Strength'] = ["Kwuarm", "Limpwurt Root"]
    recipes['Super Defence'] = ["Cadantine", "White Berries"]
    recipes['Super Magic'] = ["Lantadyme", "Potato Cactus"]
    recipes['Super Ranging'] = ["Dwarf Weed", "Wine of Zamorak"]
    recipes['Super Necromancy'] = ["Arbuck", "Blood of Orcus"]

    recipes['Extreme Attack'] = ["Avantoe", "Super Attack"]
    recipes['Extreme Strength'] = ["Dwarf Weed", "Super Strength"]
    recipes['Extreme Defence'] = ["Lantadyme", "Super Defence"]
    recipes['Extreme Magic'] = ["Ground Mud Rune", "Super Magic"]
    recipes['Extreme Ranging'] = ["Grenwall Spike", "Super Ranging"]
    recipes['Extreme Necromancy'] = ["Ground Miasma Rune", "Super Necromancy"]

    return recipes



class TestAlchemist(unittest.TestCase):

    def test_init(self):
        lab = Laboratory(initOptions(), initHerbs(), initCatalysts())
        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        self.assertEqual(alchemist.getRecipes(), initRecipes())

    def test_getLaboratory(self):
        lab = Laboratory(initOptions(), initHerbs(), initCatalysts())
        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        self.assertEqual(alchemist.getLaboratory(), lab)

    def test_mixPotion(self):
        recipe = "Super Attack: Irit, Eye of Newt"
        lab = Laboratory([], initHerbs(), initCatalysts())
        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        alchemist.mixPotion(recipe)
        self.assertEqual(alchemist.getLaboratory().potions[0].getStat(), 'attack')
        self.assertEqual(alchemist.getLaboratory().potions[0].getName(), 'Super Attack')

    def test_drinkPotion(self):
        lab = Laboratory(initOptions(), initHerbs(), initCatalysts())
        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        super_attack = SuperPotion("Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        super_attack.calculateBoost()
        alchemist.drinkPotion(super_attack)
        self.assertEqual(alchemist.attack, super_attack.boost)

        super_strength = SuperPotion("Strength", "strength", Herb("Kwuarm", 6), Catalyst("Limpwurt Root", 4, 10))
        super_strength.calculateBoost()
        alchemist.drinkPotion(super_strength)
        self.assertEqual(alchemist.strength, super_strength.boost)

        super_defence = SuperPotion("Defence", "defence", Herb("Cadantine", 9), Catalyst("White Berries", 7, 9))
        super_defence.calculateBoost()
        alchemist.drinkPotion(super_defence)
        self.assertEqual(alchemist.defence, super_defence.boost)

        super_magic = SuperPotion("Magic", "magic", Herb("Lantadyme", 10), Catalyst("Potato Cactus", 2, 5))
        super_magic.calculateBoost()
        alchemist.drinkPotion(super_magic)
        self.assertEqual(alchemist.magic, super_magic.boost)

        super_ranging = SuperPotion("Ranging", "ranging", Herb("Dwarf Weed", 2), Catalyst("Wine of Zamorak", 7, 6))
        super_ranging.calculateBoost()
        alchemist.drinkPotion(super_ranging)
        self.assertEqual(alchemist.ranged, super_ranging.boost)

        super_necromancy = SuperPotion("Necromancy", "necromancy", Herb("Arbuck", 9), Catalyst("Blood of Orcus", 9, 3))
        super_necromancy.calculateBoost()
        alchemist.drinkPotion(super_necromancy)
        self.assertEqual(alchemist.necromancy, super_necromancy.boost)

        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        extreme_attack = ExtremePotion("Attack", "attack", Catalyst("Avantoe", 6, 3), super_attack)
        extreme_attack.calculateBoost()
        alchemist.drinkPotion(extreme_attack)
        self.assertEqual(alchemist.attack, extreme_attack.boost)

        extreme_strength = ExtremePotion("Strength", "strength", Herb("Dwarf Weed", 6), super_strength)
        extreme_strength.calculateBoost()
        alchemist.drinkPotion(extreme_strength)
        self.assertEqual(alchemist.strength, extreme_strength.boost)

        extreme_defence = ExtremePotion("Defence", "defence", Herb("Lantadyme", 9), super_defence)
        extreme_defence.calculateBoost()
        alchemist.drinkPotion(extreme_defence)
        self.assertEqual(alchemist.defence, extreme_defence.boost)

        extreme_magic = ExtremePotion("Magic", "magic", Herb("Ground Mud Rune", 6), super_magic)
        extreme_magic.calculateBoost()
        alchemist.drinkPotion(extreme_magic)
        self.assertEqual(alchemist.magic, extreme_magic.boost)

        extreme_ranging = ExtremePotion("Ranging", "ranging", Herb("Grenwall Spike", 6), super_ranging)
        extreme_ranging.calculateBoost()
        alchemist.drinkPotion(extreme_ranging)
        self.assertEqual(alchemist.ranged, extreme_ranging.boost)

        extreme_necromancy = ExtremePotion("Necromancy", "necromancy", Herb("Ground Miasma Rune", 6), super_necromancy)
        extreme_necromancy.calculateBoost()
        alchemist.drinkPotion(extreme_necromancy)
        self.assertEqual(alchemist.necromancy, extreme_necromancy.boost)

    def test_collectReagent(self):
        reagent = Catalyst("Eye of Newt", 5, 7)
        lab = Laboratory([], [], [])
        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        alchemist.collectReagent(reagent, 3)
        self.assertEqual(3, len(alchemist.getLaboratory().catalysts))
        self.assertEqual("Eye of Newt", alchemist.getLaboratory().catalysts[0].getName())

    def test_refineReagents(self):
        lab = Laboratory([], initHerbs(), initCatalysts())
        alchemist = Alchemist(attack=0, strength=0, defence=0, magic=0, ranged=0, necromancy=0,
                              laboratory=lab, recipes=initRecipes())
        alchemist.refineReagents()
        self.assertEqual(alchemist.getLaboratory().herbs[0].grimy, False)
        self.assertEqual(alchemist.getLaboratory().herbs[0].potency, 10)
        self.assertEqual(alchemist.getLaboratory().catalysts[3].getQuality(), 6.1)
        self.assertEqual(alchemist.getLaboratory().catalysts[0].getQuality(), 8.1)

class TestHerb(unittest.TestCase):

    def test_init(self):
        herb = Herb("Irit", 4)
        self.assertEqual(herb.getName(), "Irit")
        self.assertEqual(herb.potency, 4)

    def test_refine(self):
        herb = Herb("Arbuck", 9)
        herb.refine()
        self.assertEqual(herb.potency, 9 * 2.5)
        self.assertEqual(herb.grimy, False)

    def test_set_get(self):
        herb = Herb("Arbuck", 9)
        self.assertEqual(herb.grimy, True)
        herb.grimy = False
        self.assertEqual(herb.grimy, False)

class TestCatalyst(unittest.TestCase):

    def test_init(self):
        catalyst = Catalyst("Eye of Newt", 5, 7)
        self.assertEqual(catalyst.getName(), "Eye of Newt")
        self.assertEqual(catalyst.potency, 5)

    def test_refine(self):
        catalyst = Catalyst("Eye of Newt", 5, 7)
        catalyst.refine()
        self.assertEqual(catalyst.getQuality(), 8.1)

class TestSuperPotion(unittest.TestCase):

    def test_init(self):
        super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        self.assertEqual(super_attack.getName(), "Super Attack")
        self.assertEqual(super_attack.getStat(), "attack")
        self.assertEqual(super_attack.boost, 0)

    def test_calculateBoost(self):
        super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        super_attack.calculateBoost()
        # self.__herb.potency + (self.__catalyst.potency * self.__catalyst.getQuality()) * 1.5
        self.assertEqual(super_attack.boost, 4 + 5 * 7 * 1.5)

    def test_set_get(self):
        super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        self.assertEqual(super_attack.getHerb().getName(), "Irit")
        self.assertEqual(super_attack.getCatalyst().getName(), "Eye of Newt")

class TestExtremePotion(unittest.TestCase):

    def test_init(self):
        super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        extreme_attack = ExtremePotion("Extreme Attack", "attack", Catalyst("Avantoe", 6, 3), super_attack)
        self.assertEqual(extreme_attack.getName(), "Extreme Attack")
        self.assertEqual(extreme_attack.getStat(), "attack")
        self.assertEqual(extreme_attack.boost, 0)

    def test_calculateBoost(self):
        super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        super_attack.calculateBoost()
        extreme_attack = ExtremePotion("Extreme Attack", "attack", Catalyst("Avantoe", 6, 3), super_attack)
        extreme_attack.calculateBoost()
        # (self.__reagent.potency * self.__potion.boost) * 3.0
        self.assertEqual(extreme_attack.boost, 6 * super_attack.boost * 3)

    def test_set_get(self):
        super_attack = SuperPotion("Super Attack", "attack", Herb("Irit", 4), Catalyst("Eye of Newt", 5, 7))
        extreme_attack = ExtremePotion("Extreme Attack", "attack", Catalyst("Avantoe", 6, 3), super_attack)
        self.assertEqual(extreme_attack.getReagent().getName(), "Avantoe")
        self.assertEqual(isinstance(extreme_attack.getReagent(), Reagent), True)

class TestLaboratory(unittest.TestCase):

    def test_init(self):
        herbs = initHerbs()
        catalysts = initCatalysts()
        lab = Laboratory(initOptions(), herbs, catalysts)
        for i, herb in enumerate(lab.herbs):
            self.assertEqual(herbs[i].getName(), lab.herbs[i].getName())
        for i, catalyst in enumerate(lab.catalysts):
            self.assertEqual(catalysts[i].getName(), lab.catalysts[i].getName())

    def test_mixPotion(self):
        herbs = initHerbs()
        catalysts = initCatalysts()
        lab = Laboratory([], herbs, catalysts)
        lab.mixPotion("Super Attack", "Super", "attack", "Irit", "Eye of Newt")
        self.assertEqual(len(lab.potions), 1)
        herbs_names = []
        for i in lab.herbs:
            herbs_names.append(i.getName())
        self.assertEqual("Irit" in herbs_names, False)
        self.assertEqual(lab.potions[0].getName(), "Super Attack")

        lab.mixPotion("Extreme Attack", "Extreme", "attack", "Avantoe", "Super Attack")
        self.assertEqual(len(lab.potions), 2)
        catalysts_names = []
        for i in lab.catalysts:
            catalysts_names.append(i.getName())
        self.assertEqual("Avantoe" in catalysts_names, False)
        self.assertEqual(lab.potions[1].getName(), "Extreme Attack")

    def test_addReagent(self):
        lab = Laboratory([], [], [])
        lab.addReagent(Herb("Lantadyme", 9), 3)
        lab.addReagent(Catalyst("Wine of Zamorak", 7, 6), 3)
        self.assertEqual(len(lab.herbs), 3)
        self.assertEqual(len(lab.catalysts), 3)
        self.assertEqual(lab.herbs[0].getName(), "Lantadyme")
        self.assertEqual(lab.herbs[1].getName(), "Lantadyme")
        self.assertEqual(lab.herbs[2].getName(), "Lantadyme")


if __name__ == '__main__':
    unittest.main()