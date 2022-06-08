
class Trapeze:
	def __init__ (self, x, y, z, u, height):
		self.AB = x
		self.BC = y
		self.CD = z
		self.DA = u
		self.height = height

	def circuit1(self):
		return (self.AB + self.BC + self.CD + self.DA)

	def field1(self):
		return( ( self.AB + self.CD )/2 * self.height )

class Rectangle(Trapeze):
	def __init__ (self, x, y):
		self.AB = x
		self.BC = y
		self.CD = x
		self.DA = y
		self.height = y

	def circuit2(self):
		return( ( 2 * self.AB ) + ( 2 * self.BC ) )

	def field2(self):
		return( self.AB * self.BC  )


class Square(Rectangle):
	def __init__ (self, x):
		self.AB = x
		self.BC = x
		self.CD = x
		self.DA = x
		self.height = x

	def circuit3(self):
		return( 4 * self.AB )

	def field3(self):
		return( self.AB * self.AB )

import unittest


class TestEvaluations(unittest.TestCase):

	def test_trapeze_circuit(self):
		rob = Square(10)

		self.assertEqual( rob.circuit1(), rob.circuit2() )

	def test_rectangle_circuit(self):
		rob = Square(10)

		self.assertEqual( rob.circuit2(), rob.circuit3() )

	def test_trapeze_field(self):
		rob = Square(10)

		self.assertEqual( rob.field1(), rob.field2())

	def test_rectangle_field(self):
		rob = Square(10)

		self.assertEqual( rob.field2(), rob.field3())

if __name__ == '__main__':
    unittest.main()