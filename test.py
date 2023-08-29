from spacecraft import Spacecraft
import unittest 

class TestSpacecraftControl(unittest.TestCase):

     # test for forward movement ( f )
    def test_forward(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["f"]

        sp1 = Spacecraft(initial_position,initial_direction)

        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0,1,0))
        self.assertEqual(final_direction, 'n')
        
    # test for backward movement ( b )
    def test_backward(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["b"]
        sp1 = Spacecraft(initial_position,initial_direction)
        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0, -1, 0))
        self.assertEqual(final_direction, "n")
        
    # test for left movement ( l )
    def test_turn_left(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["l"]
        sp1 = Spacecraft(initial_position,initial_direction)
        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "w")

    # test for right movement ( r )    
    def test_turn_right(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["r"]
        sp1 = Spacecraft(initial_position,initial_direction)
        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "e")

    # test for up movement ( u )    
    def test_turn_up(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["u"]
        sp1 = Spacecraft(initial_position,initial_direction)
        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "u")

    # test for down movement ( d )    
    def test_turn_down(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["d"]
        sp1 = Spacecraft(initial_position,initial_direction)
        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, "d")

    # test for multiple commands    
    def test_multiple_commands(self):
        initial_position = (0, 0, 0)
        initial_direction = "n"
        commands = ["f", "r", "u", "b", "l"]
        sp1 = Spacecraft(initial_position,initial_direction)
        final_position, final_direction = sp1.navigate(commands)
        self.assertEqual(final_position, (0, 1, -1))
        self.assertEqual(final_direction, "n")
    

if __name__ == "__main__":
    unittest.main()