from __future__ import annotations
from typing import List, Optional
import TrieNode, TrieTree
import json


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

def startProgram() -> None:
    print("Instructions:")
    print("After entering an ingredient, click enter. " +

          "Then enter the next one")
    print("When you are done, please type done")
    print("What ingredients do you have?")

def loopJSON() -> None:

    # For every food in data
    for detail in data['details']:

        #Only create object if food is part of the ingredients

        if detail['food'] in lstIngredients:
            detail['food'] = Food(detail['food'], detail['macronutrient'], 
                                           detail['calories'], detail['carbs'], 
                                           detail['fats'], detail['protein'])

            # Add to sets
            foodName = detail['food'].getName()
            if detail['food'].getMacronutrient() == 'carb':
                carbs.add(foodName)
            elif detail['food'].getMacronutrient() == 'fat':
                fats.add(foodName)
            else:
                proteins.add(foodName)


#------------------------------End Of Functions--------------------------------


if __name__ == '__main__':

    startProgram()
    lstIngredients = []

    done = False

    while not done:
        food = input("")
        if food == "done":
            done = True
        else:
            lstIngredients.append(food.strip())

    f = open('ingredients.json')
    data = json.load(f)
    
    # Sets
    carbs = set([])
    fats = set([])
    proteins = set([])

    loopJSON()
        

    print(carbs)
    print(fats)
    print(proteins)

    f.close()
    
    

