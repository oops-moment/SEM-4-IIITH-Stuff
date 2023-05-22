import unittest
import king
import village
import points as pt

V = village.createVillage(1)

class TestKingmove(unittest.TestCase):

    def test_attack_target_up(self):
     Kings = king.King([0,0])
     for i in range(0,18 ):
        for j in range(0,36):
            Kings.position[0]=i
            Kings.position[1]=j
            if(Kings.alive == False):
                 return
            a = Kings.position[0]
            b = Kings.position[1]
            Kings.facing='up'
            a -= 1
            if a < 0 or a >= pt.config['dimensions'][0] or b < 0 or b >= pt.config['dimensions'][1]:
                 continue           
            if V.map[a][b] != pt.BLANK and V.map[a][b] != pt.SPAWN:
                target = V.get_target(a,b)
                intial_health=target.health
                intial_king_health=Kings.health
                Kings.alive=False
                Kings.attack_target(target,Kings.attack)
                if(Kings.alive == False):
                    self.assertEqual(target.health,intial_health)
                    self.assertEqual(Kings.health,intial_king_health)       
                Kings.alive=True
                Kings.attack_target(target,Kings.attack)
                intial_health-=Kings.attack
                a=0                          #keeps track of destroyed
                if(intial_health<=0):
                    intial_health=0
                    a=1
                #  print(target.health,intial_health)
                if(a==1):
                        self.assertEqual(target.destroyed,True)
                else:
                        self.assertEqual(target.health,intial_health)
                                            

    def test_attack_target_down(self):
     Kings = king.King([0,0])
     for i in range(0,18 ):
        for j in range(0,36):
            Kings.position[0]=i
            Kings.position[1]=j
            if(Kings.alive == False):
                 return
            a = Kings.position[0]
            b = Kings.position[1]
            Kings.facing='down'
            a += 1
            if a < 0 or a >= pt.config['dimensions'][0] or b < 0 or b >= pt.config['dimensions'][1]:
                 continue           
            if V.map[a][b] != pt.BLANK and V.map[a][b] != pt.SPAWN:
                target = V.get_target(a,b)
                intial_health=target.health
                intial_king_health=Kings.health
                Kings.alive=False
                Kings.attack_target(target,Kings.attack)
                if(Kings.alive == False):
                    self.assertEqual(target.health,intial_health)
                    self.assertEqual(Kings.health,intial_king_health)       
                Kings.alive=True
                Kings.attack_target(target,Kings.attack)
                intial_health-=Kings.attack
                a=0                          #keeps track of destroyed
                if(intial_health<=0):
                    intial_health=0
                    a=1
                #  print(target.health,intial_health)
                if(a==1):
                        self.assertEqual(target.destroyed,True)
                else:
                        self.assertEqual(target.health,intial_health)


    def test_attack_target_left(self):
     Kings = king.King([0,0])
     for i in range(0,18 ):
        for j in range(0,36):
            Kings.position[0]=i
            Kings.position[1]=j
            if(Kings.alive == False):
                 return
            a = Kings.position[0]
            b = Kings.position[1]
            Kings.facing='left'
            b -= 1
            if a < 0 or a >= pt.config['dimensions'][0] or b < 0 or b >= pt.config['dimensions'][1]:
                 continue           
            if V.map[a][b] != pt.BLANK and V.map[a][b] != pt.SPAWN:
                target = V.get_target(a,b)
                intial_health=target.health
                intial_king_health=Kings.health
                Kings.alive=False
                Kings.attack_target(target,Kings.attack)
                if(Kings.alive == False):
                    self.assertEqual(target.health,intial_health)
                    self.assertEqual(Kings.health,intial_king_health)       
                Kings.alive=True
                Kings.attack_target(target,Kings.attack)
                intial_health-=Kings.attack
                a=0                          #keeps track of destroyed
                if(intial_health<=0):
                    intial_health=0
                    a=1
                #  print(target.health,intial_health)
                if(a==1):
                        self.assertEqual(target.destroyed,True)
                else:
                        self.assertEqual(target.health,intial_health)
    

    def test_attack_target_right(self):
     Kings = king.King([0,0])
     for i in range(0,18 ):
        for j in range(0,36):
            Kings.position[0]=i
            Kings.position[1]=j
            if(Kings.alive == False):
                 return
            a = Kings.position[0]
            b = Kings.position[1]
            Kings.facing='right'
            b += 1
            if a < 0 or a >= pt.config['dimensions'][0] or b < 0 or b >= pt.config['dimensions'][1]:
                 continue           
            if V.map[a][b] != pt.BLANK and V.map[a][b] != pt.SPAWN:
                target = V.get_target(a,b)
                intial_health=target.health
                intial_king_health=Kings.health
                Kings.alive=False
                Kings.attack_target(target,Kings.attack)
                if(Kings.alive == False):
                    self.assertEqual(target.health,intial_health)
                    self.assertEqual(Kings.health,intial_king_health)       
                Kings.alive=True
                Kings.attack_target(target,Kings.attack)
                intial_health-=Kings.attack
                a=0                          #keeps track of destroyed
                if(intial_health<=0):
                    intial_health=0
                    a=1

                if(a==1):
                        self.assertEqual(target.destroyed,True)
                else:
                        self.assertEqual(target.health,intial_health)

if __name__ == '__main__':
    # Run the tests
    program = unittest.main(exit=False)
    result = program.result
        
    # Write the result to output.txt
with open('output_bonus.txt', 'w') as f:
    f.write(str(result.wasSuccessful()))

