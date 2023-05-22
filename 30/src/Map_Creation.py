from src.Building import *

def createmap():
  map = []

  for i in range(0,12):
    row = []
    for j in range(0,11):
      row.append(" ")
    map.append(row)

  walllist = []
  for i in range(3,8):
    wall = Wall(3,i+1)
    wall.set_representation("—")
    map[2][i] = wall
    walllist.append(wall)

    wall = Wall(10,i+1)
    wall.set_representation("—")
    map[9][i] = wall
    walllist.append(wall)

  for i in range(3,9):
    wall = Wall(i+1,3)
    wall.set_representation("|")
    map[i][2] = wall
    walllist.append(wall)

    wall = Wall(i+1,9)
    wall.set_representation("|")
    map[i][8] = wall
    walllist.append(wall)

  wall = Wall(3,3)
  wall.set_representation("+")
  map[2][2] = wall
  walllist.append(wall)

  wall = Wall(3,9)
  wall.set_representation("+")
  map[2][8] = wall
  walllist.append(wall)

  wall = Wall(10,3)
  wall.set_representation("+")
  map[9][2] = wall
  walllist.append(wall)

  wall = Wall(10,9)
  wall.set_representation("+")
  map[9][8] = wall
  walllist.append(wall)

  cannonlist = []
  cannon = Cannon(4,5)
  map[3][4] = cannon
  cannonlist.append(cannon)

  cannon = Cannon(7,8)
  map[6][7] = cannon
  cannonlist.append(cannon)

  cannon = Cannon(9,5)
  map[8][4] = cannon
  cannonlist.append(cannon)

  hutlist = []
  hut = Hut(5,4)
  map[4][3] = hut
  hutlist.append(hut)

  hut = Hut(8,4)
  map[7][3] = hut
  hutlist.append(hut)

  hut = Hut(4,7)
  map[3][6] = hut
  hutlist.append(hut)

  hut = Hut(5,8)
  map[4][7] = hut
  hutlist.append(hut)

  hut = Hut(9,8)
  map[8][7] = hut
  hutlist.append(hut)

  townhallpostions = []
  townhall = Townhall(5,5)
  for i in range(4,8):
    for j in range(4,7):
      map[i][j] = townhall
      townhallpostions.append((j+1,i+1))

  for a in map:
    for b in a:
      print(b,end=" ")
    print("")
  
  return map,hutlist,cannonlist,townhallpostions,townhall,walllist
