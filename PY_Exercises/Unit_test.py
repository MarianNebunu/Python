
from unittest import TestCase
from MyFirstClass import MyClass 

class PostTest(TestCase):
   def test_create_post(self):
     p = MyClass("Doe", "John", 30)
     self.assertEqual(p.Family_name, "Doe")
     self.assertEqual(p.First_name, "John")
     self.assertEqual(p.age, 30)  