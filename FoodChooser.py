from __future__ import annotations
from typing import List, Optional

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
                 carbs=0, fats=0, proteins=0) -> None:
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
        self._proteins = proteins
    
    def getCalories(self) -> int:
        return self._calories
    
    def getCarbs(self) -> int:
        return self._carbs

    def getFats(self) -> int:
        return self._fats

    def getProteins(self) -> int:
        return self._proteins

if __name__ == '__main__':
    print("Instructions:")
    print("After entering an ingredient, click enter. " +
          "Then enter the next   one")
    print("When you are done, please type finished")
    print("What ingredients do you have?")
    ingredients = []
    finished = False
    while not finished:
        food = input("")
        if food == "finished":
            finished = True
        else:
            ingredients.append(food.strip())
    
