import unittest


class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2,3), 5)

  def test_subtract(self):
    self.assertEqual(subtract(10,8), 2)

  def test_multiply(self):
    self.asertEqual(multiply(3,2), 6)

  def test_divide(self):
    self.assertEqual(divide(10,2), 5)
