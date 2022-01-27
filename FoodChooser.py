from __future__ import annotations
from typing import Dict


class Meal:

    """ Information of Meal
    
    Liquids are measured in tbsp
    Macronutrients are measured in grams
    Time is measured in minutes
    
    === Attributes ===

    _name: str
    _meal_of_day: str
    _meal_type: str
    _time: int
    _calories: int
    _carbs: int
    _fats: int
    _proteins: int
    _ingredients: Dict[str, int]

    """
    

    def __init__(self, name: str, meal_of_day: str, _meal_type: str,
                 _time: int, calories: int, carbs: int, fats: int, protein: int,
                 _ingredients: Dict[str, int]) -> None:
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

    print("Is this for breakfast, lunch or dinner?")
    meal_of_day = input("")
    f = open('data.json')
    data = json.load(f)
    
    # Meals
    calorie_surplus = []
    high_protein = []
    high_fats = []
    high_carbs = []
    
    meal_types = {
        "calorie surplus": calorie_surplus,
        "high in protein": high_in_protein,
        "high in fats": high_in_fats
    }

    f.close()
