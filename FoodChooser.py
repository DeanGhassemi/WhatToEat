from __future__ import annotations
from typing import List, Optional
import json


class Food:

    """ Information of food
    
    === Attributes ===

    _macronutrient: str
    _calories: int

    _carbs: int
    _fats: int
    _proteins: int

    """
    

    def __init__(self, macronutrient: str, calories=0, 
                 carbs=0, fats=0, protein=0) -> None:
        """
        Initialize and declare each attribute

        macronutrient: type of macronutrient

        calories: number of kcal

        carbs, fats and proteins are measured in grams
        
        Parameters:

            macronutrient: str
            calories: int

            carbs: int
            fats: int
            proteins: int

        """
        self._macronutrient = macronutrient
        self._calories = calories
        self._carbs = carbs
        self._fats = fats
        self._protein = protein
        
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
    for detail in ingredients['details']:

        #Only create object if food is part of the ingredients

        if detail['food'] in lstIngredients:
            detail['food'] = Food(detail['macronutrient'], 
                                           detail['calories'], detail['carbs'], 
                                           detail['fats'], detail['protein'])

            # Add to sets
            if detail['food'].getMacronutrient() == 'carb':
                carbs.add(detail['food'])
            elif detail['food'].getMacronutrient() == 'fat':
                fats.add(detail['food'])
            else:
                proteins.add(detail['food'])


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

    f = open('data.json')
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
    
    

