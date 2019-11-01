class Speaker:

    discount_amount = .2
    inventory_count = 0 


    def __init__(self,lower_range=100,upper_range=20000,power=200,cost=500):
        self.lower_range = lower_range
        self.upper_range = upper_range
        self.power = power
        self.cost = cost
        self.range = [lower_range,upper_range]

        Speaker.inventory_count += 1
    
    def value(self):
        return self.power / self.cost
    
    def apply_discount(self,discount_amount = discount_amount):
        # applies the default discount amount unless value is passed in 
        return self.cost * (1 - discount_amount)

    def apply_discount2(self):
        # applies the default discount amount unless value is passed in 
        return self.cost * (1 - self.discount_amount)  

    @classmethod
    #overrides discount amount set by class variable above
    def set_discount_amount(cls,amount):
        cls.discount_amount = amount 

    @classmethod
    #creates new speaker from a string of attributes
    def from_string(cls,speaker_string):
        lower_range,upper_range,power,cost = speaker_string.split("-")
        return cls(lower_range,upper_range,power,cost)
    
    @staticmethod
    def is_wknd_rental(day):
        if datetime.datetime.weekday(day) == 4 or datetime.datetime.weekday(day) == 5:
            return False 
        else:
            return True


#testing class method for creating new Speaker from string below
speaker_string1 = "20-60-2000-4000"
deep_sub = Speaker.from_string(speaker_string1)

sub = Speaker(35,70,3400,2000)
top = Speaker (125,20000,1000,500)
# sub.discount_amount = .5

#testing class method for over-riding discount amount
# Speaker.set_discount_amount(.9)

import datetime

my_date = datetime.date(2017, 7,11)
print(Speaker.is_wknd_rental(my_date))






#print statements for later use

# print(deep_sub.range)
# print(sub.value())
# print(speaker.value(sub))
# print(sub.cost,sub.apply_discount(.8))
# print(sub.cost,sub.apply_discount2())
# print(Speaker.__dict__)
# print(sub.discount_amount,top.discount_amount)

# print(Speaker.inventory_count)

