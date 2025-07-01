import unittest


class TestCalculator(unittest.TestCase):
  def test_add_zero(self):
    self.assertEqual(add(0, 0), 0)
    self.assertEqual(add(0, 5), 5)
    self.assertEqual(add(5, 0), 5)

  def test_subtract_zero(self):
      self.assertEqual(subtract(0, 0), 0)
      self.assertEqual(subtract(5, 0), 5)
      self.assertEqual(subtract(0, 5), -5)

  def test_multiply_zero(self):
      self.assertEqual(multiply(0, 5), 0)
      self.assertEqual(multiply(5, 0), 0)
  
  def test_divide_float(self):
      self.assertAlmostEqual(divide(5, 2), 2.5)
      self.assertAlmostEqual(divide(-5, 2), -2.5)
  
  def test_divide_by_zero_raises(self):
      with self.assertRaises(ZeroDivisionError):
          divide(1, 0)
  
  def test_add_floats(self):
      self.assertAlmostEqual(add(2.5, 3.1), 5.6)
    
  def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.asserEqual(add(-3, -2), -5)
    self.assertEqual(add(-5, 2), -3)

  def test_subtract(self):
    self.assertEqual(subtract(10, 8), 2)
    self.assertEqual(subtract(-10, -2), -8)
    self.assertEqual(subtract(-8, 2), -10)

  def test_multiply(self):
    self.assertEqual(multiply(3, 2), 6)
    self.assertEqual(multiply(-3, -4), 12)
    self.assertEqual(multiply(-3, 4), -12)
    
  def test_divide(self):
    self.assertEqual(divide(10, 2), 5)
    self.assertEqual(divide(10, -5), -2)
    self.assertEqual(divide(-9, -3), 3)   
