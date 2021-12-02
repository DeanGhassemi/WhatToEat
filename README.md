# WhatToEat Demo

This project is solving a problem I often have. When I get hungry, I usually do not know what to cook. To solve this problem, I am making a program that will choose what I should make and eat. The program will take an input of ingredients and then find a meal I know how to cook that has carbs, fats and protein. 

# Plan

## Components

It will be made using Python as it will be all done through the console. I plan on using a tree or graph data structure to catagorize each component (carbs, fats and proteins) to gain experience using the data structure. I will have the meal as the key and incredients as the value for a hashmap.

## Challenges

To figure out which foods is a carb, fat or protein, I will collect my own data and make a data sheet where my python program will read and look for it's type. The reason this is only a demo program is because I do not have an easy way to collect the data and it will be manually made. Not only that, it is only for breakfast. In later updates, it will include lunch, dinner, and hopefully a more efficient way to collect data. Stay tuned!


## Changes and Updates from the Plan

Using a JSON file to store information of foods. It's my data file.
I am using a TrieTree for autocorrect in case the user misspells the word. I will need another data file for a bunch of names of foods.

