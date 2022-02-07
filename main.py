class dog:
    def __init__(self,breed,whatColor,hasaTail,itcanHunt,itisSmall):
      self.breed = breed
      self.color = whatColor
      self.tail = hasaTail
      self.hunt = itcanHunt
      self.size = itisSmall

Ians_dog = dog("Australian Shepherd","Black",True,False,False)

print(Ians_dog.breed)