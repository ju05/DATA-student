# Daily challenge: Old MacDonald’s Farm
# Declare a new class representing a farm.
# It stores the farm name and a dictionary that holds information about the animals.

class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.name = farm_name
        self.animals = {}

    # Define a method to add animals to the dictionary, increasing the count if the animal already exists.
    def add_animal(self, animal_type, count=1):
        # If the animal already exists, increase its count. Otherwise, add it as a new entry.
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals.update({animal_type: count})

    # Define a method that formats the animal data into aligned columns based on the longest animal name.
    def get_info(self):
        a = max(len(animal) for animal in self.animals.keys())
        output_string = self.name + " farm\n"
        for animal, amount in self.animals.items():
            output_string += animal + ' ' * (a - len(animal) + 1) + ': ' + str(amount) + '\n'
        # Add a right-aligned signature line to the output.
        output_string += f"\n{'E-I-E-I-0!':>15}"
        return output_string

    # Return a sorted list of the animal types in the dictionary.
    def get_animal_types(self):
        """Return a sorted list of the animal types in the dictionary."""
        return sorted(list(self.animals.keys()))

    # Return a string summarizing the animals on the farm, adding 's' for plural where needed.
    def get_short_info(self):
        list_animals_for_string = []
        for name in self.get_animal_types():
            if self.animals[name] == 1:
                list_animals_for_string.append(name)
            else:
                list_animals_for_string.append(name + 's')
        string_farm_info = f"{self.name} farm has {', '.join(list_animals_for_string)}."
        return string_farm_info


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 1)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
