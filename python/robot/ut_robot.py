
#requred package gore here
import  unittest 
from robot import Robot as rbt

#ut test class
class walk_test(unittest.TestCase):
    """Tests for robot walk task."""
    
    #walk unit test case
    def test_walk(self):
        print("\nIn unit test " + self._testMethodName)
        rb = rbt()
        res = rb.walk(3.5)
        if(not res):
            self.assertTrue(res, msg = "Task: walk() failed")
 
    #walk and carry test case
    def test_walk_and_carry(self):
        print("\nIn unit test " + self._testMethodName)
        rb = rbt()
        res = rb.walk_and_carry(2,3)
        if(not res):
            self.assertTrue(res, msg = "Task: walk_and_carry() failed")

    #carry test case
    def test_carry(self):
        print("\nIn unit test " + self._testMethodName)
        rb = rbt()
        res = rb.carry(12)
        if(not res):
            self.assertTrue(res, msg = "Task: carry() failed")

    #carry negative test case
    def test_carry_negative(self):
        print("\nIn unit test " + self._testMethodName)
        rb = rbt()
        res = rb.carry(-2)
        if(not res):
            self.assertTrue(res, msg = "Task: carry() failed")


if __name__ == '__main__':
    unittest.main()
