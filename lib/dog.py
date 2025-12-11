#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
    "Mutt"
]

class Dog:
    def __init__(self, name="unknown", breed="Mutt"):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = name
        else:
            self.name = name
        
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = breed
        else:
            self.breed = breed
         
    def bark(self):
            print("Woof!")
    def sit(self):
            print(f"{self.name} sits down.")
    pass