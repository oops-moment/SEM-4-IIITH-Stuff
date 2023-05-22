from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)


class Troop:
    def __init__(self):
        self.max_health = 0
        self.hp = 0
        self.x = 0
        self.y = 0
        self.alive = False
        self.damage_per_sec = 0
        self.speed = 0
        self.representation = " "
        self.defaultrepresentation = " "

    def __str__(self):
        return self.representation

    def spawn(self, position):
        self.alive = True
        if position == 1:
            self.x = 2
            self.y = 6
        elif position == 2:
            self.x = 6
            self.y = 2
        elif position == 3:
            self.x = 10
            self.y = 9

    def hit(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0
            self.representation = " "
        elif self.hp <= 0.2 * self.max_health:
            self.representation = Style.DIM+self.defaultrepresentation
        elif self.hp > 0.2 * self.max_health and self.hp <= 0.5 * self.max_health:
            self.representation = Style.NORMAL+self.defaultrepresentation
        else:
            self.representation = Style.BRIGHT+self.defaultrepresentation

    def attack(self, building):
        building.hit(self.damage_per_sec)

class Barbarian(Troop):
    def __init__(self):
        super().__init__()
        self.max_health = 200
        self.hp = 200
        self.damage_per_sec = 30
        self.speed = 1
        self.representation = Style.BRIGHT+Fore.BLUE+"b"
        self.defaultrepresentation = Fore.BLUE+"b"

    def move(self, coordinate, building):
        if self.x < coordinate[0]:
            self.x += 1
        elif self.x > coordinate[0]:
            self.x -= 1

        if self.y < coordinate[1]:
            self.y += 1
        elif self.y > coordinate[1]:
            self.y -= 1

        if self.x == coordinate[0] and self.y == coordinate[1]:
            self.attack(building)

class King(Troop):
    def __init__(self):
        super().__init__()
        self.max_health = 1000
        self.hp = 1000
        self.damage_per_sec = 200
        self.speed = 1
        self.representation = Style.BRIGHT+Fore.MAGENTA+"k"
        self.defaultrepresentation = Fore.MAGENTA+"k"
        self.pos = "outside"

    def move(self, keyinput, walllist):
        newwalllist = []
        for wall in walllist:
            if wall.hp != 0:
                newwalllist.append(wall)
        walllist = newwalllist

        if keyinput == "w":
            if self.y > 1:
                self.y -= 1
                if self.pos == "outside" and self.x > 3 and self.x < 9 and self.y > 3 and self.y < 10:
                    self.y += 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.y -= 1
                elif self.pos == "inside" and (self.x < 3 or self.x > 9 or self.y < 3 or self.y > 10):
                    self.y += 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.y -= 1

        elif keyinput == "a":
            if self.x > 1:
                self.x -= 1
                if self.pos == "outside" and self.x > 3 and self.x < 9 and self.y > 3 and self.y < 10:
                    self.x += 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.x -= 1
                elif self.pos == "inside" and (self.x < 3 or self.x > 9 or self.y < 3 or self.y > 10):
                    self.x += 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.x -= 1

        elif keyinput == "s":
            if self.y < 12:
                self.y += 1
                if self.pos == "outside" and self.x > 3 and self.x < 9 and self.y > 3 and self.y < 10:
                    self.y -= 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.y += 1
                elif self.pos == "inside" and (self.x < 3 or self.x > 9 or self.y < 3 or self.y > 10):
                    self.y -= 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.y += 1

        elif keyinput == "d":
            if self.x < 11:
                self.x += 1
                if self.pos == "outside" and self.x > 3 and self.x < 9 and self.y > 3 and self.y < 10:
                    self.x -= 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.x += 1
                elif self.pos == "inside" and (self.x < 3 or self.x > 9 or self.y < 3 or self.y > 10):
                    self.x -= 1
                    change = False
                    for wall in walllist:
                        if self.x == wall.x and self.y == wall.y:
                            change = True
                    if not change:
                        self.x += 1

        if self.x > 3 and self.x < 9 and self.y > 3 and self.y < 10:
            self.pos = "inside"
        elif self.x < 3 or self.x > 9 or self.y < 3 or self.y > 10:
            self.pos = "outside"

