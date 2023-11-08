"""
File: compassignmentmain.py
Description: The implementation of the behaviour of an alchemist who is owned by a laboratory. In the laboratory an alchemist can mix and drink potions as
well collect and refine reagents. Potions and reagents are stored in a laboratory.
Author: Yujin Chen
StudentID: 110357638
EmailID: cheyy364
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod
from typing import List

class Reagent(ABC):

    def __init__(self, name: str, potency: float):
        """
        Reagent class initialization function

        :param name: the name of reagent
        :type name: str
        :param potency: the potency of reagent
        :type potency: float
        """
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        """
        Abstract method of Reagent class
        :return:
        :rtype:
        """
        pass

    def getName(self) -> str:
        """

        :return: the name of reagent
        :rtype: str
        """
        return self.__name

    @property
    def potency(self) -> float:
        return self.__potency

    @potency.setter
    def potency(self, potency: float):
        self.__potency = potency


class Herb(Reagent):

    def __init__(self, name: str, potency: float, grimy: bool = True):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        pass

    @property
    def grimy(self) -> bool:
        return self.__grimy

    @grimy.setter
    def grimy(self, grimy: bool) -> bool:
        self.__grimy = grimy
        return self.__grimy


class Catalyst(Reagent):

    def __init__(self, name: str, potency: float, quality: float):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self) -> float:
        return self.__quality


class Potion(ABC):


    def __init__(self, name: str, stat: str):

        self.__name = name
        self.__stat = stat
        self.__boost = 0.

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self) -> str:
        return self.__name

    def getStat(self) -> str:
        return self.__stat

    @property
    def boost(self) -> float:
        return self.__boost

    @boost.setter
    def boost(self, boost: float):
        self.__boost = boost


class SuperPotion(Potion):

    def __init__(self, name: str, stat: str, herb: Herb, catalyst: Catalyst):
        super(SuperPotion, self).__init__(name, stat)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        self.boost = round(self.__herb.potency + (self.__catalyst.potency * self.__catalyst.getQuality()) * 1.5, 2)

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):

    def __init__(self, name: str, stat: str, reagent: Reagent, potion: Potion):
        super(ExtremePotion, self).__init__(name, stat)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        self.boost = round((self.__reagent.potency * self.__potion.boost) * 3.0, 2)

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion



class Laboratory:
    def __init__(self, potions: List[Potion], herbs: List[Herb], catalysts: List[Catalyst]):
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts

    @property
    def potions(self):
        return self.__potions

    @potions.setter
    def potions(self, potions: List[Potion]):
        self.__potions = potions

    @property
    def herbs(self):
        return self.__herbs

    @herbs.setter
    def herbs(self, herbs: List[Herb]):
        self.__herbs = herbs

    @property
    def catalysts(self):
        return self.__catalysts

    @catalysts.setter
    def catalysts(self, catalysts: List[Catalyst]):
        self.__catalysts = catalysts

    def mixPotion(self, name:str, type:str, stat:str, primarylngredient:str, secondarylngredient:str):
        pass


    def addReagent(self, reagent: Reagent, amount: int):
        pass


class Alchemist:

    def __init__(self, attack: int, strength: int, defence: int, magic: int, ranged: int, necromancy: int,
                 laboratory: Laboratory, recipes: {}):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = recipes

    @property
    def attack(self):
        return self.__attack

    @property
    def strength(self):
        return self.__strength

    @property
    def defence(self):
        return self.__defence

    @property
    def magic(self):
        return self.__magic

    @property
    def necromancy(self):
        return self.__necromancy

    @property
    def ranged(self):
        return self.__ranged

    def getLaboratory(self) -> Laboratory:
        return self.__laboratory

    def getRecipes(self) -> {}:
        return self.__recipes

    def mixPotion(self, recipe: str):
        pass


    def drinkPotion(self, potion: Potion):
        pass

    def collectReagent(self, reagent: Reagent, amount: int):
        self.getLaboratory().addReagent(reagent, amount)

    def refineReagents(self):
        for herb in self.getLaboratory().herbs:
            herb.refine()

        for catalyst in self.getLaboratory().catalysts:
            catalyst.refine()



