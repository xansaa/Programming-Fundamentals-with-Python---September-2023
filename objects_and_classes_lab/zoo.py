class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}"
        elif species == "fishe":
            result += f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}"
        elif species == "bird":
            result += f"Mammals in {self.name_zoo}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
input_count = int(input())

for num in range(input_count):
    species, name = input().split()
    zoo.add_animal(species, name)
searched_species = input()
print(zoo.get_info(searched_species))
