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
        pass

    def test_refine(self):
        pass

    def test_set_get(self):
        pass

class TestCatalyst(unittest.TestCase):

    def test_init(self):
        pass

    def test_refine(self):
        pass

class TestSuperPotion(unittest.TestCase):

    def test_init(self):
        pass

    def test_calculateBoost(self):
        pass

    def test_set_get(self):
        pass

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