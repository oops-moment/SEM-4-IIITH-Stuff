import unittest
import king
import village
import points as pt

V = village.createVillage(1)

class TestKingmove(unittest.TestCase):
    
    def test_move_up(self):
        vmap = V.map
        for i in range(0,18 ):
            for j in range(0,36):
                King = king.getHero(0)
                king_compare=king.King([i,j])
                king_compare.alive=False
                king_compare.move('up',V)
                if(king_compare.alive==False):
                    self.assertEqual(king_compare.position,[i,j])
                king_compare.alive=True
                king_compare.move('up',V)
                King.position[0]=i
                King.position[1]=j
                king_face=king_compare.facing
                King.facing='up'
                if(King.alive == False):
                   return
                for c in range(King.speed):
                    r = King.position[0] - 1
                    c = King.position[1]
                    if(r < 0):
                        continue
                    if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                            break
                    King.position[0] -= 1               
                self.assertEqual(king_compare.position,[King.position[0],King.position[1]])
                self.assertEqual(king_face,King.facing)
                self.assertEqual(pt.HERO_POS,king_compare.position)


    def test_move_down(self):
        vmap = V.map
        for i in range(0,18 ):
            for j in range(0,36):
                King = king.getHero(0)
                king_compare=king.King([i,j])
                king_compare.alive=False
                king_compare.move('down',V)
                if(king_compare.alive==False):
                    self.assertEqual(king_compare.position,[i,j])
                king_compare.alive=True
                king_compare.move('down',V)
                King.position[0]=i
                King.position[1]=j
                king_face=king_compare.facing
                King.facing='down'
                if(King.alive == False):
                   return
                for c in range(King.speed):
                    r = King.position[0] + 1
                    c = King.position[1]
                    if(r >= len(vmap)):
                     continue
                    if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                     break
                    King.position[0] += 1      

                self.assertEqual(king_compare.position,[King.position[0],King.position[1]])
                self.assertEqual(king_face,King.facing)
                self.assertEqual(pt.HERO_POS,king_compare.position)
    

    def test_move_left(self):
        vmap = V.map
        for i in range(0,18 ):
            for j in range(0,36):
                King = king.getHero(0)
                king_compare=king.King([i,j])
                king_compare.alive=False
                king_compare.move('left',V)
                if(king_compare.alive==False):
                    self.assertEqual(king_compare.position,[i,j])
                king_compare.alive=True
                king_compare.move('left',V)
                King.position[0]=i
                King.position[1]=j
                king_face=king_compare.facing
                King.facing='left'
                if(King.alive == False):
                   return
                for c in range(King.speed):
                    r = King.position[0]
                    c = King.position[1] - 1
                    if(c < 0):
                        continue
                    if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                         break
                    King.position[1] -= 1    
                self.assertEqual(king_compare.position,[King.position[0],King.position[1]])
                self.assertEqual(king_face,King.facing)
                self.assertEqual(pt.HERO_POS,king_compare.position)


    def test_move_right(self):
        vmap = V.map
        for i in range(0,18 ):
            for j in range(0,36):
                King = king.getHero(0)
                king_compare=king.King([i,j])
                king_compare.alive=False
                king_compare.move('right',V)
                if(king_compare.alive==False):
                    self.assertEqual(king_compare.position,[i,j])
                king_compare.alive=True
                king_compare.move('right',V)
                king_face=king_compare.facing
                King.facing='right'
                King.position[0]=i
                King.position[1]=j
                if(King.alive == False):
                   return
                for c in range(King.speed):
                    r = King.position[0]
                    c = King.position[1] + 1
                    if(c >= len(vmap[0])):
                        continue
                    if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                         break
                    King.position[1] += 1    
                self.assertEqual(king_compare.position,[King.position[0],King.position[1]])
                self.assertEqual(king_face,King.facing)
                self.assertEqual(pt.HERO_POS,king_compare.position)

                        

if __name__ == '__main__':
    # Run the tests
    program = unittest.main(exit=False)
    result = program.result
        
    # Write the result to output.txt
with open('output.txt', 'w') as f:
    f.write(str(result.wasSuccessful()))

