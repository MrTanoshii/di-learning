class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].lower()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Animals grouped by first letter:")
        for letter, animals in sorted_animals.items():
            print(f"{letter}: {animals}")


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Bear")

ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()
