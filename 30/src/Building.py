# from colorama import Fore, Back, Style, init
# init(autoreset=True)

# class Building:
#     def __init__(self, y, x):
#         self.max_health = 0
#         self.hp = 0
#         self.representation = " "
#         self.defaultrepresentation = " "
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return self.representation

#     def hit(self, damage):
#         self.hp = self.hp - damage
#         if self.hp <= 0:
#             self.hp = 0
#             self.representation = " "
#         elif self.hp <= 0.2 * self.max_health:
#             self.representation = Fore.RED + self.defaultrepresentation
#         elif self.hp > 0.2 * self.max_health and self.hp <= 0.5 * self.max_health:
#             self.representation = Fore.YELLOW + self.defaultrepresentation
#         else:
#             self.representation = Fore.GREEN + self.defaultrepresentation


# class Wall(Building):
#     def __init__(self, y, x):
#         super().__init__(y, x)
#         self.max_health = 800
#         self.hp = 800

#     def set_representation(self, representation):
#         self.representation = Fore.GREEN + representation
#         self.defaultrepresentation = representation


# class Hut(Building):
#     def __init__(self, y, x):
#         super().__init__(y, x)
#         self.max_health = 500
#         self.hp = 500
#         self.representation = Fore.GREEN + "H"
#         self.defaultrepresentation = "H"


# class Cannon(Building):
#     def __init__(self, y, x):
#         super().__init__(y, x)
#         self.max_health = 500
#         self.hp = 500
#         self.representation = Fore.GREEN + "C"
#         self.defaultrepresentation = "C"
#         self.damage_per_sec = 50
#         self.range = 6

#     def attack(self, troop):
#         self.representation = Back.LIGHTWHITE_EX + self.representation
#         troop.hit(self.damage_per_sec)


# class Townhall(Building):
#     def __init__(self, y, x):
#         super().__init__(y, x)
#         self.max_health = 1500
#         self.hp = 1500
#         self.representation = Fore.GREEN + "T"
#         self.defaultrepresentation = "T"

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

class Building():
  def __init__(self,y,x):
    self.max_health = 0
    self.hp = 0
    self.representation = " "
    self.defaultrepresentation = " "
    self.x = x
    self.y = y
  def __str__(self):
    return self.representation

  def hit(self,damage):
    self.hp = self.hp - damage
    if self.hp <= 0:
      self.hp = 0
      self.representation = " "
    elif self.hp <= 0.2 * self.max_health:
      self.representation = Fore.RED+self.defaultrepresentation
    elif self.hp > 0.2 * self.max_health and self.hp <= 0.5 * self.max_health:
      self.representation = Fore.YELLOW+self.defaultrepresentation
    else:
      self.representation = Fore.GREEN+self.defaultrepresentation


class Wall(Building):
  def __init__(self,y,x):
    super().__init__(y,x)
    self.max_health = 800
    self.hp = 800
  def set_representation(self,representation):
    self.representation =  Fore.GREEN+representation
    self.defaultrepresentation = representation

class Hut(Building):
  def __init__(self,y,x):
    super().__init__(y,x)
    self.max_health = 500
    self.hp = 500
    self.representation =  Fore.GREEN+"H"
    self.defaultrepresentation = "H"


class Cannon(Building):
  def __init__(self,y,x):
    super().__init__(y,x)
    self.max_health = 500
    self.hp = 500
    self.representation = Fore.GREEN+"C"
    self.defaultrepresentation = "C"
    self.damage_per_sec = 50
    self.range = 6
  
  def attack(self,troop):
    self.representation = Back.LIGHTWHITE_EX+self.representation
    troop.hit(self.damage_per_sec)


class Troop():
  def __init__(self, hp):
    self.hp = hp
  
  def hit(self, damage):
    self.hp -= damage


class Townhall(Building):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.max_health = 1500
        self.hp = 1500
        self.representation = Fore.GREEN + "T"
        self.defaultrepresentation = "T"


# codesmell : Feature Envy
# codesmell description : The attack method in Cannon is overly dependent on the Troop class
# suggesed refactoring : Move the attack method to the Troop class and have the Cannon class call the hit method on the Troop instance