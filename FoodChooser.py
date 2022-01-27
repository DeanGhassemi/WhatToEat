from __future__ import annotations
from typing import Dict
import pprint, json


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
    

    def __init__(self, name: str, meal_of_day: str, meal_type: str,
                 time: int, calories: int, carbs: int, fats: int, protein: int,
                 ingredients: Dict[str, int]) -> None:
        """
        Initialize and declare each attribute
        
        Parameters:
            name: str
            meal_of_day: str
            meal_type: str
            time: int
            calories: int
            carbs: int
            fats: int
            proteins: int
            ingredients: Dict[str, int]

        """
        self._name = name
        self._meal_of_day = meal_of_day
        self._meal_type = meal_type
        self._time = time
        self._calories = calories
        self._carbs = carbs
        self._fats = fats
        self._protein = protein
        self._ingredients = ingredients
       
    def get_name(self) -> str:
        return self._name
    
    def get_meal_of_day(self) -> str:
        return self._meal_of_day
    
    def get_meal_type(self) -> str:
        return self._meal_type
    
    def get_time(self) -> str:
        return self._time

    def get_calories(self) -> int:
        return self._calories

    def get_carbs(self) -> int:
        return self._carbs

    def get_fats(self) -> int:
        return self._fats

    def get_proteins(self) -> int:
        return self._proteins


# ------------Functions below make the main function cleaner-------------------

def loopJSON() -> None:

    # For every food in data
    for detail in data['details']:
        mealobj = Meal(detail['meal'], detail['meal_of_day'],
                               detail['meal_type'], detail['time'],
                               detail['calories'], detail['carbs'], 
                               detail['fats'], detail['protein'], 
                               detail['ingredients'])
        
        meal_name = mealobj.get_name()
        meal_types[detail['meal_type']].append(meal_name)


#------------------------------End Of Functions--------------------------------


if __name__ == '__main__':


    
    # Meals
    calorie_surplus = []
    high_protein = []
    high_fats = []
    high_carbs = []
    
    meal_types = {
        "calorie surplus": calorie_surplus,
        "high protein": high_protein,
        "high fats": high_fats,
        "high carbs": high_carbs
    }
    f = open('data.json')
    data = json.load(f)
    loopJSON()
    pprint.pprint(meal_types)
    f.close()
