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


class TestAlchemist(unittest.TestCase):

    def test_init(self):
        pass

    def test_getLaboratory(self):
        pass

    def test_mixPotion(self):
        pass

    def test_drinkPotion(self):
        pass

    def test_collectReagent(self):
        pass

    def test_refineReagents(self):
        pass

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
        pass

    def test_calculateBoost(self):
        pass

    def test_set_get(self):
        pass

class TestLaboratory(unittest.TestCase):

    def test_init(self):
        pass

    def test_mixPotion(self):
        pass


    def test_addReagent(self):
        pass


if __name__ == '__main__':
    unittest.main()