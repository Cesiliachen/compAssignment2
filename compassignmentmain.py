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
    """
    Reagent abstract class
    """
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
    """
    Subclass Herb of the Reagent abstract class
    """
    def __init__(self, name: str, potency: float, grimy: bool = True):
        """
        Initialization function of subclass Herb
        :param name: Herb's name
        :type name: str
        :param potency: the potenct of Herb
        :type potency: float
        :param grimy:
        :type grimy: bool
        """
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        """
        Herb's refine method
        :return: None
        :rtype:
        """
        self.__grimy = False
        self.potency = self.potency * 2.5
        print("leads to a not grimy herb,  multiply its existing potency by 2.5")

    @property
    def grimy(self) -> bool:
        return self.__grimy

    @grimy.setter
    def grimy(self, grimy: bool) -> bool:
        self.__grimy = grimy
        return self.__grimy


class Catalyst(Reagent):
    """
    Subclass Catalyst of the Reagent abstract class
    """
    def __init__(self, name: str, potency: float, quality: float):
        """
        Initialization function of subclass Catalyst
        :param name: the name of Catalyst
        :type name:  str
        :param potency: the potency of Catalyst
        :type potency: float
        :param quality: the quality of Catalyst
        :type quality: float
        """
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        """
        Catalyst's refine method
        :return: None
        :rtype:
        """
        if self.__quality < 8.9:
            self.__quality += 1.1
            print("the quality of catalyst " + self.getName() + "is increased by 1.1")
        else:
            self.__quality = 10
            print("it cannot be refined any further")

    def getQuality(self) -> float:
        """
        get quality of Catalyst
        :return: the quality of Catalyst
        :rtype: float
        """
        return self.__quality


class Potion(ABC):
    """
    Potion abstract class
    """

    def __init__(self, name: str, stat: str):
        """
        Potion class initialization method
        :param name: the name of Potion
        :type name: str
        :param stat: the attribute
        :type stat: str
        """
        self.__name = name
        self.__stat = stat
        self.__boost = 0.

    @abstractmethod
    def calculateBoost(self):
        """
        Potion's abstract method
        :return: None
        :rtype:
        """
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
    """
    A subclass of Potion, SuperPotion
    """
    def __init__(self, name: str, stat: str, herb: Herb, catalyst: Catalyst):
        """

        :param name: Potion's name
        :type name: str
        :param stat: the attribute
        :type stat: str
        :param herb: An instance of the Herb class
        :type herb: Herb
        :param catalyst: An instance of the Catalyst class
        :type catalyst: Catalyst
        """
        super(SuperPotion, self).__init__(name, stat)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        """
        Computational boost
        :return:
        :rtype:
        """
        self.boost = round(self.__herb.potency + (self.__catalyst.potency * self.__catalyst.getQuality()) * 1.5, 2)

    def getHerb(self):
        """
        get Herb
        :return:
        :rtype:
        """
        return self.__herb

    def getCatalyst(self):
        """
        get Catalyst
        :return:
        :rtype:
        """
        return self.__catalyst


class ExtremePotion(Potion):
    """
    A subclass of Potion ExtremePotion
    """
    def __init__(self, name: str, stat: str, reagent: Reagent, potion: Potion):
        """

        :param name: the name of Potion
        :type name: str
        :param stat: the attribute
        :type stat: str
        :param reagent: An instance of the Reagent class
        :type reagent: Reagent
        :param potion: An instance of the Potion class
        :type potion: Potion
        """
        super(ExtremePotion, self).__init__(name, stat)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        """
        Computational boost
        :return:
        :rtype:
        """
        self.boost = round((self.__reagent.potency * self.__potion.boost) * 3.0, 2)

    def getReagent(self):
        """
        get Reagent
        :return:
        :rtype:
        """
        return self.__reagent

    def getPotion(self):
        """
        get Potion
        :return:
        :rtype:
        """
        return self.__potion



class Laboratory:
    """
    The laboratory stores the potions, herbs, and catalysts.
    """
    def __init__(self, potions: List[Potion], herbs: List[Herb], catalysts: List[Catalyst]):
        """

        :param potions: List of subclasses of Potion
        :type potions:
        :param herbs: List of subclasses of Herb
        :type herbs:
        :param catalysts: List of subclasses of Catalyst
        :type catalysts:
        """
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
        """
        mix potions
        :param name: Potion's name
        :type name: str
        :param type: SuperPotion or ExtremePotion
        :type type: str
        :param stat: the attr
        :type stat: str
        :param primarylngredient: first gredient
        :type primarylngredient: str
        :param secondarylngredient: seconde gredient
        :type secondarylngredient: str
        :return:
        :rtype:
        """
        pass


    def addReagent(self, reagent: Reagent, amount: int):
        """
        add Reagent
        :param reagent: An instance of the Reagent class
        :type reagent: Reagent
        :param amount: the number of Reagent
        :type amount: int
        :return:
        :rtype:
        """
        pass


class Alchemist:
    """
    Alchemist class
    """
    def __init__(self, attack: int, strength: int, defence: int, magic: int, ranged: int, necromancy: int,
                 laboratory: Laboratory, recipes: {}):
        """

        :param attack: attack attribute
        :type attack: int
        :param strength: attack attribute
        :type strength: int
        :param defence: attack attribute
        :type defence: int
        :param magic: attack attribute
        :type magic: int
        :param ranged: attack attribute
        :type ranged: int
        :param necromancy: attack attribute
        :type necromancy: int
        :param laboratory:
        :type laboratory:
        :param recipes:
        :type recipes:
        """
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
        """
        mix Potion
        :param recipe: recipe of Potion
        :type recipe: str
        :return:
        :rtype:
        """
        pass


    def drinkPotion(self, potion: Potion):
        """
        drink Potion
        :param potion:
        :type potion:
        :return:
        :rtype:
        """
        pass

    def collectReagent(self, reagent: Reagent, amount: int):
        """
        collect Reagent
        :param reagent:
        :type reagent:
        :param amount:
        :type amount:
        :return:
        :rtype:
        """
        self.getLaboratory().addReagent(reagent, amount)

    def refineReagents(self):
        """
        refine Reagents
        :return:
        :rtype:
        """
        for herb in self.getLaboratory().herbs:
            herb.refine()

        for catalyst in self.getLaboratory().catalysts:
            catalyst.refine()



