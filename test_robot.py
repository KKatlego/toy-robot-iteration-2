import unittest
from unittest.mock import patch
from io import StringIO
import robot
import sys


class TestRobot(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\nhal\n"))
    def test_robot_name(self):
        Output = StringIO()
        sys.stdout = Output
        name = robot.get_robot_name()
        self.assertEqual("HAL", name)
        sys.stdout = sys.__stdout__
    

    @patch("sys.stdin", StringIO("OFf"))
    def test_get_input_command(self):
        Output = StringIO()
        sys.stdout = Output
        self.assertEqual(robot.get_input_command("HAL"), "OFf")
        sys.stdout = sys.__stdout__
        

    def test_check_valid_commands(self):
        Output = StringIO()
        sys.stdout = Output
        self.assertEqual(robot.check_valid_commands("forward", "HAL"), True)
        self.assertEqual(robot.check_valid_commands("Jump up", "HAL"), False)
        sys.stdout = sys.__stdout__


    def test_off_command(self):
        Output = StringIO()
        sys.stdout = Output
        self.assertEqual(robot.off_command("off", "HAL"), "off")
        sys.stdout = sys.__stdout__


    @patch("sys.stdin", StringIO("HAL\noff\n"))
    def test_off_command_output(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
            self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""", output.strip())


    def test_forward_command(self):
        Output = StringIO()
        sys.stdout = Output
        self.assertEqual(robot.forward_command("forward 10"), ("forward 10", ["forward", "10"], 10))
        sys.stdout = sys.__stdout__


    @patch("sys.stdin", StringIO("HAL\nforward 10\noff\n"))
    def test_print_moved_forward_output(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
            self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output.strip())


    def test_back_command(self):
        Output = StringIO()
        sys.stdout = Output
        self.assertEqual(robot.back_command("back 10"), ("back 10", ["back", "10"], 10))
        sys.stdout = sys.__stdout__


    @patch("sys.stdin", StringIO("HAL\nback 10\noff\n"))
    def test_print_moved_back_output(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
            self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""", output.strip())


    @patch("sys.stdin", StringIO("HAL\nright\noff\n"))
    def test_right_output(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output.strip("\n"))


    @patch("sys.stdin", StringIO("HAL\nleft\noff\n"))
    def test_left_output(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output.strip("\n"))



    def test_left_command(self):
        self.assertEqual(robot.left_command("left", 0), 270)
        self.assertEqual(robot.left_command("left", 90), 0)
        self.assertEqual(robot.left_command("left", 180), 90)
        self.assertEqual(robot.left_command("left", 270), 180)

    @patch("sys.stdin", StringIO("HAL\nsprint 5\noff\n"))
    def test_sprint_command_output(self):
        with patch('sys.stdout', new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,15).
HAL: What must I do next? HAL: Shutting down..""", output.strip())
        

    def test_track_position(self):
        Output = StringIO()
        sys.stdout = Output
        self.assertEqual(robot.track_position("HAL", 20, 0, 0, "forward", 0), (0,20))
        self.assertEqual(robot.track_position("HAL", 10, 0, 20, "back", 0), (0,10))
        self.assertEqual(robot.track_position("HAL", 10, 0, 10, "right", 90), (0,10))
        self.assertEqual(robot.track_position("HAL", 5, 0, 0, "sprint", 0), (0,15))
        sys.stdout = sys.__stdout__


    @patch("sys.stdin", StringIO("HAL\nforward 20\nback 10\nright\noff\n"))
    def test_track_position_output(self):
        with patch('sys.stdout', new = StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output.strip())
            

    @patch("sys.stdin", StringIO("HAL\nforward 201\nback 201\noff\n"))
    def test_robot_area(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot.robot_start()
            output = out.getvalue()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output.strip())


    def test_help_command(self):
        Output = StringIO()
        sys.stdout = Output 
        understand = "I can understand these commands:"
        off = "OFF  - Shut down robot"
        help_me = "HELP - provide information about commands"
        forward = "FORWARD  - Moves robot forward"
        back = "BACK  - Moves robot backward"
        right = "RIGHT  - Turns robot 90 degrees to the right"
        left = "LEFT  - Turns robot 90 degrees to the left"
        self.assertEqual(robot.help_command(), f"{understand}\n{off}\n{help_me}\n{forward}\n{back}\n{right}\n{left}")
        sys.stdout = sys.__stdout__
    

if __name__ == "__main__":
    unittest.main()