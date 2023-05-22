from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

import math
import time

from src.Troop import *
from src.Building import *
from src.Map_Creation import createmap

import sys
import termios
import tty
import signal
import os
MAX_TROOPS = 15

class Get:
    """Class to get input."""
    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass


def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


def input_to(getch, troopnumber,king,timeout=0.5):
    """Taking input from user."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        signal.alarm(0)
        if (text == "1" or text == "2" or text == "3") and troopnumber < MAX_TROOPS: 
          print("deploy at "+text)

        return text
        
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None

def finddistance(a,b):
  dist = (((a[0] - b[0])**2) + ((a[1] - b[1])**2) )**(1/2)
  return dist

def updatepositions(hutlist,cannonlist,townhallpostions,townhall,barbarianlist,walllist,king):
  
  newhutlist = []
  for hut in hutlist:
    if hut.hp != 0:
      newhutlist.append(hut)
  hutlist = newhutlist

  newcannonlist = []
  for cannon in cannonlist:
    if cannon.hp != 0:
      newcannonlist.append(cannon)
      mindistance = math.inf
      target = " "
      for barbarian in barbarianlist:
        distance = finddistance((cannon.x,cannon.y),(barbarian.x,barbarian.y))
        if distance < cannon.range and distance < mindistance:
          target = barbarian
          mindistance = distance
      if king != " ":
        if king.hp > 0:
          distance = finddistance((cannon.x,cannon.y),(king.x,king.y))
          if distance < cannon.range and distance < mindistance:
            target = king
            mindistance = distance
      if target != " ":
        cannon.attack(target)
      else:
        cannon.hit(0)
  cannonlist = newcannonlist

  newwalllist = []
  for wall in walllist:
    if wall.hp != 0:
      newwalllist.append(wall)
  walllist = newwalllist

  if townhall.hp == 0:
    townhallpostions = []
    for i in range(4,8):
      for j in range(4,7):
        map[i][j] = " "
    
  if len(hutlist) == 0 and len(cannonlist) == 0 and len(townhallpostions) == 0:
    print("VICTORY!!")
    return False,0

  for barbarian in barbarianlist:
    nearestobject = ""
    nearestdistance = math.inf
    coordinate = (0,0)

    for hut in hutlist:
      distance = finddistance((hut.x,hut.y),(barbarian.x,barbarian.y))
      if distance <= nearestdistance:
        nearestobject = hut
        nearestdistance = distance
        coordinate = (hut.x,hut.y)

    for cannon in cannonlist:
      distance = finddistance((cannon.x,cannon.y),(barbarian.x,barbarian.y))
      if distance <= nearestdistance:
        nearestobject = cannon
        nearestdistance = distance
        coordinate = (cannon.x,cannon.y)

    
    for position in townhallpostions:
      distance = finddistance((position[0],position[1]),(barbarian.x,barbarian.y))
      if distance <= nearestdistance:
        nearestobject = townhall
        nearestdistance = distance
        coordinate = (position[0],position[1])

    if nearestdistance == math.inf:
      print("VICTORY!!")
      return False,1

    change = False 
    for wall in walllist:
      if wall.x == barbarian.x and wall.y == barbarian.y:
        barbarian.attack(wall)
        change = True
        break
    if change == False:
      barbarian.move(coordinate,nearestobject)
  
  if len(barbarianlist) == 0:
    return False,1  
  return True,1

def findbuilding(hutlist,cannonlist,townhallpostions,townhall,walllist,king):

  newhutlist = []
  for hut in hutlist:
    if hut.hp != 0:
      if hut.x == king.x and hut.y == king.y:
        king.attack(hut)
      newhutlist.append(hut)
  hutlist = newhutlist

  newcannonlist = []
  for cannon in cannonlist:
    if cannon.hp != 0:
      if cannon.x == king.x and cannon.y == king.y:
        king.attack(cannon)
      newcannonlist.append(cannon)
  cannonlist = newcannonlist

  newwalllist = []
  for wall in walllist:
    if wall.hp != 0:
      if wall.x == king.x and wall.y == king.y:
        king.attack(wall)
      newwalllist.append(wall)
  walllist = newwalllist

  
  if townhall.hp == 0:
    townhallpostions = []
  for position in townhallpostions:
    if position[0] == king.x and position[1] == king.y:
      king.attack(townhall)

  if len(hutlist) == 0 and len(cannonlist) == 0 and len(townhallpostions) == 0:
    return True

if __name__ == "__main__":

  name = round(time.time() * 1000)
  file = open("replays/{}.txt".format(name), "w")

  barbarianlist = []
  map,hutlist,cannonlist,townhallpostions,townhall,walllist = createmap()

  oldmap = []
  for row in map:
    addrow = []
    for elem in row:
      addrow.append(elem)
    oldmap.append(addrow)
  oldmap[5][1] = "1"
  oldmap[1][5] = "2"
  oldmap[8][9] = "3"
  map[5][1] = "1"
  map[1][5] = "2"
  map[8][9] = "3"

  updates = True
  timeelapsed = 0
  troopnumber = 0
  king = " "
  kinginput = "-"
  time0 = time.perf_counter()

  while updates:
    
    time1 = time.perf_counter()
    userinput = input_to(Get(),troopnumber,king)
    
    if troopnumber < MAX_TROOPS:
      if userinput == "1":
        barb = Barbarian()
        file.write("{}\t{}\n".format(time1 - time0,"1"))
        barb.spawn(1)
        barbarianlist.append(barb)
        troopnumber += 1
      elif userinput == "2":
        barb = Barbarian()
        file.write("{}\t{}\n".format(time1 - time0,"2"))
        barb.spawn(2)
        barbarianlist.append(barb)
        troopnumber += 1
      elif userinput == "3":
        barb = Barbarian()
        file.write("{}\t{}\n".format(time1 - time0,"3"))
        barb.spawn(3)
        barbarianlist.append(barb)
        troopnumber += 1
    if king == " ":
      if userinput == "4":
        king = King()
        file.write("{}\t{}\n".format(time1 - time0,"4"))
        king.spawn(1)
        print("spawn king at 1")

      elif userinput == "5":
        king = King()
        file.write("{}\t{}\n".format(time1 - time0,"5"))
        king.spawn(2)
        print("spawn king at 2")
      elif userinput == "6":
        king = King()
        file.write("{}\t{}\n".format(time1 - time0,"6"))
        king.spawn(3)
        print("spawn king at 3")
    else:
      if (userinput == "w" or userinput == "a" or userinput == "s" or userinput == "d" or userinput == " ") and king.hp > 0:
        kinginput = userinput

    newbarbarianlist = []
    for barbarian in barbarianlist:
      if barbarian.hp != 0:
        newbarbarianlist.append(barbarian)
        map[barbarian.y - 1][barbarian.x - 1] = barbarian
    barbarianlist = newbarbarianlist
    
    time2 = time.perf_counter()
    timeelapsed += time2 - time1
    if(timeelapsed > 1):
      os.system("clear")
      timeelapsed = 0

      if kinginput != "-":
        if kinginput == " ":
          print("attack")
          file.write("{}\t{}\n".format(time1 - time0,kinginput))
          findbuilding(hutlist,cannonlist,townhallpostions,townhall,walllist,king)
        else:
          file.write("{}\t{}\n".format(time1 - time0,kinginput))
          king.move(kinginput,walllist)
        kinginput = "-"

      if king != " ":
        if king.hp > 0:
          map[king.y - 1][king.x - 1] = king

      for a in map:
        for b in a:
          print(b,end=" ")
        print("")
      print("Alive: {}".format(len(barbarianlist)))
      print("Troops left: {}".format(MAX_TROOPS - troopnumber))
      map = []
      for row in oldmap:
        addrow = []
        for elem in row:
          addrow.append(elem)
        map.append(addrow)
      updates,listlen = updatepositions(hutlist,cannonlist,townhallpostions,townhall,barbarianlist,walllist,king)
      
      
      if listlen == 0:
        break

      if troopnumber < MAX_TROOPS and len(barbarianlist) == 0:
        updates = True
      if king != " ":
        print("king health: {}".format(king.hp))
      if updates == False and troopnumber == MAX_TROOPS and len(barbarianlist) == 0:
        if king != " ":
          if king.hp <= 0:
            print("DEFEAT!!")
            break
        updates = True

  print("Replay can be viewed at {}.txt".format(name))
  file.close()
          