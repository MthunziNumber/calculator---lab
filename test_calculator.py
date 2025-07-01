import unittest


class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3), 5)
    self.asserEqual(add(-3,-2), -5)
    self.assertEqual(add(-5,2), -3)

  def test_subtract(self):
    self.assertEqual(subtract(10,8), 2)
    self.assertEqual(subtract(-10, -2), -8)
    self.assertEqual(subtract(-8, 2), -10)

  def test_multiply(self):
    self.assertEqual(multiply(3,2), 6)
    self.assertEquals(multiply(-3, -4), 12)
    self.assertEquals(multiply(-3, 4), -12)
  def test_divide(self):
    self.assertEqual(divide(10,2), 5)
    self.assertEqual(divide(10, -5), -2)
    self.assertEqual(divide(-9, -3), 3)   
    self.assertEqual(divide(10,0), "division by zero is undefined")
