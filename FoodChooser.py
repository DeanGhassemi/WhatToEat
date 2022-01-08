from __future__ import annotations
from typing import List, Optional
import noms


class Food:

    """ Information of food
    
    === Attributes ===

    _name: str
    _macronutrient: str
    _calories: int
    _carbs: int
    _fats: int
    _proteins: int

    """
    

    def __init__(self, name: str, macronutrient: str, calories=0, 
                 carbs=0, fats=0, protein=0) -> None:
        """
        Initialize and declare each attribute

        name: name of the food

        macronutrient: type of macronutrient

        calories: number of kcal

        carbs, fats and proteins are measured in grams
        
        Parameters:
            name: str
            macronutrient: str
            calories: int
            carbs: int
            fats: int
            proteins: int

        """
        self._name = name
        self._macronutrient = macronutrient
        self._calories = calories
        self._carbs = carbs
        self._fats = fats
        self._protein = protein
        
    def getName(self) -> str:
        return self._name   
        
    def getMacronutrient(self) -> str:
        return self._macronutrient

    def getCalories(self) -> int:
        return self._calories

    def getCarbs(self) -> int:
        return self._carbs

    def getFats(self) -> int:
        return self._fats

    def getProteins(self) -> int:
        return self._proteins


# ------------Functions below make the main function cleaner-------------------



#------------------------------End Of Functions--------------------------------


if __name__ == '__main__':

    print("Hello World")
    key = "VOcXLMciuzKMWU16JJ2VN7C3YEp00NB3J2SBX1ww"
    klient = noms.Client(key)
    search_results = klient.search_query("Raw Broccoli")
    print(search_results)
    
