import random



class Product:
    """
    below are variables defined inside of a class
    """


    def __init__(self,name, price = 10, weight = 20, flammability = .5):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(random.randint(1000000, 9999999))

    def stealability(self):
        StealRatio = self.price / self.weight
        if StealRatio < 0.5:
            return "Not so stealable..."
        if StealRatio >= 0.5 and StealRatio < 1.0:
            return "Kinda stealable." 
        else:
            return "Very stealable!"

    def explode(self):
        ExplodeRatio = self.flammability * self.weight
        if ExplodeRatio < 10:
            return "...fizzle."
        if ExplodeRatio >= 10 and ExplodeRatio < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    """
    below are variables defined inside of the subclass
    """

    def __init__(self,name, price = 10, weight = 10, flammability = .5):
        super().__init__(name, price,weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
