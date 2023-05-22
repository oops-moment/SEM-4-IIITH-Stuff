# Assignment 4: Prisha

This repository contains the implementation for Assignment 4.

## Implementation

All the requirements mentioned in the assignment have been successfully implemented.

To run these tests, ensure that the required modules (`king`, `village`, and `points`) are imported. Then run the `unittest.main()` function.

The output of the tests will be written to the file `output.txt`. The status of tests can be seen from the console log, but the final result will be in `output.txt`, which is in the same directory as the `test.py` file.

Note that the full log can be seen on terminal whereas the final output can be seen only on output.txt as binary

## King Move Unit Tests

This test suite verifies the `move()` function of the `King` class in the `king` module. To run the test, place the file in the same directory as the `src` folder which contains the code base and execute `python3 test.py` from the command line.

### Test Cases

This suite contains the following test cases:

- **test_move_up()**: Tests if the king moves up correctly, which involves moving one cell up the current cell and hence decreasing the row index by 1.
- **test_move_down()**: Tests if the king moves down correctly, which involves moving one cell down the current cell and hence increasing the row index by 1.
- **test_move_left()**: Tests if the king moves left correctly, which involves moving one cell left to the current cell and hence decreasing the column index by 1.
- **test_move_right()**: Tests if the king moves right correctly, which involves moving one cell right to the current cell and hence increasing the column index by 1.

### Edge Cases

These test cases cover the following edge cases:

- The king cannot move off the game board. This holds true for each of the four corners of the board, where the king would hence stay at the same position.
- The king cannot move into a non-blank, non-spawn tile. This means the king cannot occupy a position that is already occupied by walls, huts, cannons, town halls, or other troops/buildings.
- The king cannot move through obstacles. It cannot skip buildings or any other obstacles and hence the position remains unchanged if such a case arises.
- The king's speed is correctly enforced. In the context of movement, the possibility of movement is considered after each unit step.

---

## BONUS


## King Move Unit Tests

This test suite verifies the `move()` function of the `King` class in the `king` module. To run the test, place the file in the same directory as the `src` folder which contains the code base and execute `python3 test.py` from the command line.

### Test Cases

This suite contains the following test cases:

- **test_attack_target()**: Tests if the king attacks the target correctly. It iterates over the cells of the game board, and attacks the target if it exists.


### Edge Cases

- The king cannot attack a target that is out of range. This means that the target should be within the range of the king's attack.
- The king cannot attack a target that is not within its line of sight. This means that the target should be within a straight line from the king's position and no other obstacles should obstruct the line of sight.
- The king cannot attack a target that is already destroyed. This means that the king should not attack a target that has already been destroyed, and should instead move on to the next target.
- The king cannot attack a target that does not exist. This means that the king should not attack a target if there is no target in the specified position.